"use strict";

const canvas = document.getElementById("game");
const ctx = canvas.getContext("2d");
const startOverlay = document.getElementById("start");
const finishOverlay = document.getElementById("finish");
const statsEl = document.getElementById("stats");
const playButton = document.getElementById("play");
const againButton = document.getElementById("again");
const runtimeStatus = document.getElementById("runtimeStatus");

const W = canvas.width;
const H = canvas.height;
const WORLD_W = 3200;
const WORLD_H = 2200;
const TAU = Math.PI * 2;
const keys = new Set();
const keyLatch = new Map();
let pressed = new Set();
let lastInput = "NONE";

function latchKey(key, milliseconds = 180) {
  keyLatch.set(key, performance.now() + milliseconds);
}

function inputDown(key) {
  return keys.has(key) || (keyLatch.get(key) ?? 0) > performance.now();
}
let running = false;
let paused = false;
let last = performance.now();
let elapsed = 0;
let shake = 0;
let flash = 0;
let credits = 0;
let shardCount = 0;
let stage = 0;
let message = "Find the cyan car";
let messageTime = 4;
let audio = null;

const camera = { x: 0, y: 0 };
const player = { x: 650, y: 1090, r: 15, speed: 230, angle: 0, inCar: false };
const car = { x: 770, y: 1090, angle: 0, speed: 0, w: 66, h: 34, boost: 100, colour: "#62f5ff" };
const mission = { pickup: { x: 2700, y: 390 }, delivery: { x: 450, y: 1790 } };

const roads = [
  { x: 0, y: 300, w: WORLD_W, h: 180, axis: "h" },
  { x: 0, y: 1000, w: WORLD_W, h: 180, axis: "h" },
  { x: 0, y: 1700, w: WORLD_W, h: 180, axis: "h" },
  { x: 350, y: 0, w: 180, h: WORLD_H, axis: "v" },
  { x: 1250, y: 0, w: 180, h: WORLD_H, axis: "v" },
  { x: 2150, y: 0, w: 180, h: WORLD_H, axis: "v" },
  { x: 2850, y: 0, w: 180, h: WORLD_H, axis: "v" },
];

const xBlocks = [[30, 320], [560, 1220], [1460, 2120], [2360, 2820], [3060, 3170]];
const yBlocks = [[30, 270], [510, 970], [1210, 1670], [1910, 2170]];
const buildings = [];
for (let c = 0; c < xBlocks.length; c += 1) {
  for (let r = 0; r < yBlocks.length; r += 1) {
    if (c === 1 && r === 2) continue;
    const [x1, x2] = xBlocks[c];
    const [y1, y2] = yBlocks[r];
    const bw = x2 - x1;
    const bh = y2 - y1;
    if (bw < 140 || bh < 140) continue;
    const pad = 26;
    if (bw > 430) {
      const gap = 34;
      const width = (bw - pad * 2 - gap) / 2;
      buildings.push({ x: x1 + pad, y: y1 + pad, w: width, h: bh - pad * 2, hue: (c * 67 + r * 31) % 360 });
      buildings.push({ x: x1 + pad + width + gap, y: y1 + pad, w: width, h: bh - pad * 2, hue: (c * 67 + r * 31 + 90) % 360 });
    } else {
      buildings.push({ x: x1 + pad, y: y1 + pad, w: bw - pad * 2, h: bh - pad * 2, hue: (c * 67 + r * 31) % 360 });
    }
  }
}
const arcade = buildings.find((b) => b.x > 1460 && b.y > 510 && b.y < 970);
if (arcade) arcade.label = "ARCADE";
const nexus = buildings.find((b) => b.x > 2360 && b.y > 1210 && b.y < 1670);
if (nexus) nexus.label = "NEXUS";
const park = { x: 590, y: 1260, w: 590, h: 350 };

const trafficPaths = [
  [{x:440,y:390},{x:2240,y:390},{x:2240,y:1090},{x:440,y:1090}],
  [{x:1340,y:1790},{x:2940,y:1790},{x:2940,y:390},{x:1340,y:390}],
  [{x:2240,y:1090},{x:2940,y:1090},{x:2940,y:1790},{x:2240,y:1790}],
];
const trafficColours = ["#ff5fd1", "#ffd86b", "#8cff9e", "#8d7cff", "#ffffff"];
const traffic = Array.from({ length: 10 }, (_, i) => {
  const path = trafficPaths[i % trafficPaths.length];
  const idx = i % path.length;
  return { x: path[idx].x + (i % 3) * 16, y: path[idx].y + (i % 2) * 16, path, target: (idx + 1) % path.length, speed: 118 + (i % 4) * 18, angle: 0, colour: trafficColours[i % trafficColours.length] };
});

const pedestrians = Array.from({ length: 36 }, (_, i) => ({
  x: 580 + (i * 149) % 2480,
  y: 510 + (i * 113) % 1320,
  vx: (Math.random() - 0.5) * 38,
  vy: (Math.random() - 0.5) * 38,
  timer: Math.random() * 3,
  colour: ["#ffc3d7", "#bddffe", "#caffbf", "#ffd6a5"][i % 4],
}));

const shards = [
  {x:1340,y:390},{x:2240,y:760},{x:2940,y:1090},{x:2240,y:1790},
  {x:1340,y:1790},{x:440,y:1450},{x:1340,y:1090},{x:2940,y:390},
].map((point, i) => ({ ...point, taken: false, phase: i * 0.7 }));
const particles = [];
const rain = Array.from({ length: 120 }, (_, i) => ({ x: (i * 97) % W, y: (i * 53) % H, speed: 420 + (i % 7) * 45, len: 7 + (i % 5) * 2 }));

function clamp(value, min, max) { return Math.max(min, Math.min(max, value)); }
function distance(ax, ay, bx, by) { return Math.hypot(ax - bx, ay - by); }
function lerp(a, b, t) { return a + (b - a) * t; }
function angleLerp(a, b, t) {
  let diff = ((b - a + Math.PI) % TAU) - Math.PI;
  if (diff < -Math.PI) diff += TAU;
  return a + diff * t;
}
function pointInRect(x, y, rect, margin = 0) {
  return x > rect.x - margin && x < rect.x + rect.w + margin && y > rect.y - margin && y < rect.y + rect.h + margin;
}
function hitsBuilding(x, y, radius) { return buildings.some((b) => pointInRect(x, y, b, radius)); }
function say(text, seconds = 2.4) { message = text; messageTime = seconds; }
function objective() {
  if (stage === 0) return { x: car.x, y: car.y, label: "YOUR CAR", colour: "#62f5ff" };
  if (stage === 1) return { ...mission.pickup, label: "DATA PICKUP", colour: "#62f5ff" };
  if (stage === 2) return { ...mission.delivery, label: "SAFEHOUSE", colour: "#8cff9e" };
  return null;
}
function tone(freq, duration = 0.07, volume = 0.035, type = "sine") {
  if (!audio) return;
  try {
    const osc = audio.createOscillator();
    const gain = audio.createGain();
    osc.type = type;
    osc.frequency.value = freq;
    gain.gain.value = volume;
    osc.connect(gain);
    gain.connect(audio.destination);
    const now = audio.currentTime;
    gain.gain.setValueAtTime(volume, now);
    gain.gain.exponentialRampToValueAtTime(0.0001, now + duration);
    osc.start(now);
    osc.stop(now + duration);
  } catch {}
}
function burst(x, y, colour, count = 24, force = 180) {
  for (let i = 0; i < count; i += 1) {
    const angle = Math.random() * TAU;
    const speed = force * (0.3 + Math.random() * 0.9);
    particles.push({ x, y, vx: Math.cos(angle) * speed, vy: Math.sin(angle) * speed, life: 0.5 + Math.random() * 0.6, maxLife: 1.1, colour, size: 2 + Math.random() * 5 });
  }
}

function reset() {
  Object.assign(player, { x: 650, y: 1090, angle: 0, inCar: false });
  Object.assign(car, { x: 770, y: 1090, angle: 0, speed: 0, boost: 100 });
  stage = 0;
  credits = 0;
  shardCount = 0;
  elapsed = 0;
  particles.length = 0;
  shards.forEach((s) => { s.taken = false; });
  running = true;
  paused = false;
  say("Find the cyan car and press E", 4);
  finishOverlay.classList.add("hidden");
}

function enterExit() {
  if (!running) return;
  if (player.inCar) {
    const exitX = car.x + Math.cos(car.angle + Math.PI / 2) * 50;
    const exitY = car.y + Math.sin(car.angle + Math.PI / 2) * 50;
    if (!hitsBuilding(exitX, exitY, player.r)) {
      player.inCar = false;
      player.x = exitX;
      player.y = exitY;
      car.speed *= 0.55;
      say("On foot", 1.2);
      tone(260, 0.06, 0.02, "square");
    }
    return;
  }
  if (distance(player.x, player.y, car.x, car.y) < 78) {
    player.inCar = true;
    player.x = car.x;
    player.y = car.y;
    if (stage === 0) {
      stage = 1;
      say("Drive to the DATA PICKUP beacon", 3.2);
      tone(520, 0.08, 0.04);
      setTimeout(() => tone(740, 0.1, 0.035), 90);
    }
  }
}

function updatePlayer(dt) {
  if (player.inCar) return;
  let dx = 0;
  let dy = 0;
  if (inputDown("w") || inputDown("arrowup")) dy -= 1;
  if (inputDown("s") || inputDown("arrowdown")) dy += 1;
  if (inputDown("a") || inputDown("arrowleft")) dx -= 1;
  if (inputDown("d") || inputDown("arrowright")) dx += 1;
  if (dx || dy) {
    const len = Math.hypot(dx, dy);
    dx /= len;
    dy /= len;
    player.angle = Math.atan2(dy, dx);
    const nx = clamp(player.x + dx * player.speed * dt, player.r, WORLD_W - player.r);
    const ny = clamp(player.y + dy * player.speed * dt, player.r, WORLD_H - player.r);
    if (!hitsBuilding(nx, player.y, player.r)) player.x = nx;
    if (!hitsBuilding(player.x, ny, player.r)) player.y = ny;
  }
}

function updateCar(dt) {
  if (!player.inCar) {
    car.speed *= Math.max(0, 1 - dt * 1.8);
    return;
  }
  const forward = inputDown("w") || inputDown("arrowup");
  const back = inputDown("s") || inputDown("arrowdown");
  const left = inputDown("a") || inputDown("arrowleft");
  const right = inputDown("d") || inputDown("arrowright");
  const boosting = inputDown("shift") && car.boost > 0 && car.speed > 80;

  if (forward) car.speed += 430 * dt;
  if (back) car.speed += car.speed > 25 ? -540 * dt : -310 * dt;
  if (!forward && !back) {
    const drag = 225 * dt;
    car.speed = Math.abs(car.speed) <= drag ? 0 : car.speed - Math.sign(car.speed) * drag;
  }
  if (boosting) {
    car.speed += 520 * dt;
    car.boost = Math.max(0, car.boost - 34 * dt);
    if (Math.random() < dt * 30) burst(car.x - Math.cos(car.angle) * 36, car.y - Math.sin(car.angle) * 36, "#62f5ff", 2, 80);
  } else {
    car.boost = Math.min(100, car.boost + 11 * dt);
  }

  car.speed = clamp(car.speed, -190, 560 + (boosting ? 220 : 0));
  const steer = (left ? -1 : 0) + (right ? 1 : 0);
  if (steer && Math.abs(car.speed) > 8) {
    car.angle += steer * 2.35 * clamp(Math.abs(car.speed) / 160, 0.28, 1.25) * dt * Math.sign(car.speed);
  }

  const oldX = car.x;
  const oldY = car.y;
  car.x = clamp(car.x + Math.cos(car.angle) * car.speed * dt, 28, WORLD_W - 28);
  car.y = clamp(car.y + Math.sin(car.angle) * car.speed * dt, 28, WORLD_H - 28);
  if (hitsBuilding(car.x, car.y, 29)) {
    car.x = oldX;
    car.y = oldY;
    car.speed *= -0.22;
    shake = Math.min(18, 6 + Math.abs(car.speed) * 0.03);
    flash = 0.3;
    tone(95, 0.08, 0.035, "sawtooth");
  }
  player.x = car.x;
  player.y = car.y;
  player.angle = car.angle;
}

function updateTraffic(dt) {
  for (const vehicle of traffic) {
    const target = vehicle.path[vehicle.target];
    const dx = target.x - vehicle.x;
    const dy = target.y - vehicle.y;
    const d = Math.hypot(dx, dy);
    vehicle.angle = angleLerp(vehicle.angle, Math.atan2(dy, dx), Math.min(1, dt * 5));
    vehicle.x += Math.cos(vehicle.angle) * vehicle.speed * dt;
    vehicle.y += Math.sin(vehicle.angle) * vehicle.speed * dt;
    if (d < 28) vehicle.target = (vehicle.target + 1) % vehicle.path.length;
    if (player.inCar && distance(vehicle.x, vehicle.y, car.x, car.y) < 48) {
      car.speed *= -0.18;
      shake = 10;
      flash = 0.35;
      burst((vehicle.x + car.x) / 2, (vehicle.y + car.y) / 2, "#ffd86b", 16, 140);
      tone(110, 0.07, 0.035, "square");
    }
  }
}

function updatePedestrians(dt) {
  for (const person of pedestrians) {
    person.timer -= dt;
    if (person.timer <= 0) {
      person.timer = 1.5 + Math.random() * 3;
      const angle = Math.random() * TAU;
      const speed = 14 + Math.random() * 28;
      person.vx = Math.cos(angle) * speed;
      person.vy = Math.sin(angle) * speed;
    }
    const nx = clamp(person.x + person.vx * dt, 20, WORLD_W - 20);
    const ny = clamp(person.y + person.vy * dt, 20, WORLD_H - 20);
    if (!hitsBuilding(nx, person.y, 7)) person.x = nx; else person.vx *= -1;
    if (!hitsBuilding(person.x, ny, 7)) person.y = ny; else person.vy *= -1;
    if (player.inCar && distance(person.x, person.y, car.x, car.y) < 66) {
      const angle = Math.atan2(person.y - car.y, person.x - car.x);
      person.vx = Math.cos(angle) * 120;
      person.vy = Math.sin(angle) * 120;
      person.timer = 0.5;
    }
  }
}

function updateShards() {
  const actor = player.inCar ? car : player;
  for (const shard of shards) {
    if (!shard.taken && distance(actor.x, actor.y, shard.x, shard.y) < 48) {
      shard.taken = true;
      shardCount += 1;
      credits += 250;
      burst(shard.x, shard.y, "#ff5fd1", 30, 210);
      shake = 5;
      tone(680, 0.06, 0.035);
      setTimeout(() => tone(920, 0.08, 0.03), 60);
      say(`Data shard ${shardCount}/8  +250 CR`, 1.8);
    }
  }
}

function updateMission() {
  if (stage === 1 && distance(car.x, car.y, mission.pickup.x, mission.pickup.y) < 95) {
    stage = 2;
    credits += 1000;
    burst(mission.pickup.x, mission.pickup.y, "#62f5ff", 65, 260);
    shake = 8;
    flash = 0.42;
    say("PACKAGE ACQUIRED — deliver to the SAFEHOUSE", 3.4);
    tone(520, 0.08, 0.04);
    setTimeout(() => tone(660, 0.08, 0.04), 80);
    setTimeout(() => tone(880, 0.12, 0.04), 160);
  }
  if (stage === 2 && distance(car.x, car.y, mission.delivery.x, mission.delivery.y) < 105) {
    stage = 3;
    credits += 3000;
    burst(mission.delivery.x, mission.delivery.y, "#8cff9e", 100, 330);
    shake = 12;
    flash = 0.65;
    tone(440, 0.11, 0.04);
    setTimeout(() => tone(660, 0.11, 0.04), 100);
    setTimeout(() => tone(880, 0.18, 0.05), 210);
    statsEl.textContent = `${credits.toLocaleString()} CR • ${shardCount}/8 shards • ${elapsed.toFixed(1)}s`;
    setTimeout(() => finishOverlay.classList.remove("hidden"), 700);
  }
}

function updateParticles(dt) {
  for (const particle of particles) {
    particle.x += particle.vx * dt;
    particle.y += particle.vy * dt;
    particle.vx *= Math.pow(0.07, dt);
    particle.vy *= Math.pow(0.07, dt);
    particle.life -= dt;
  }
  for (let i = particles.length - 1; i >= 0; i -= 1) {
    if (particles[i].life <= 0) particles.splice(i, 1);
  }
}

function updateCamera(dt) {
  const actor = player.inCar ? car : player;
  const lead = player.inCar ? clamp(car.speed * 0.32, -100, 170) : 0;
  const tx = actor.x + Math.cos(player.angle) * lead - W / 2;
  const ty = actor.y + Math.sin(player.angle) * lead - H / 2;
  const t = 1 - Math.pow(0.0008, dt);
  camera.x = lerp(camera.x, clamp(tx, 0, WORLD_W - W), t);
  camera.y = lerp(camera.y, clamp(ty, 0, WORLD_H - H), t);
}

function update(dt) {
  if (!running || paused) return;
  elapsed += dt;
  messageTime = Math.max(0, messageTime - dt);
  shake = Math.max(0, shake - dt * 28);
  flash = Math.max(0, flash - dt * 1.7);
  if (pressed.has("e")) enterExit();
  updatePlayer(dt);
  updateCar(dt);
  updateTraffic(dt);
  updatePedestrians(dt);
  updateShards();
  updateMission();
  updateParticles(dt);
  updateCamera(dt);
}

function drawRoads() {
  ctx.fillStyle = "#111923";
  ctx.fillRect(0, 0, WORLD_W, WORLD_H);
  ctx.fillStyle = "#202b36";
  roads.forEach((road) => ctx.fillRect(road.x, road.y, road.w, road.h));
  ctx.save();
  ctx.strokeStyle = "rgba(255,216,107,.6)";
  ctx.lineWidth = 3;
  ctx.setLineDash([26, 22]);
  for (const road of roads) {
    ctx.beginPath();
    if (road.axis === "h") {
      ctx.moveTo(road.x, road.y + road.h / 2);
      ctx.lineTo(road.x + road.w, road.y + road.h / 2);
    } else {
      ctx.moveTo(road.x + road.w / 2, road.y);
      ctx.lineTo(road.x + road.w / 2, road.y + road.h);
    }
    ctx.stroke();
  }
  ctx.restore();
}

function drawPark() {
  ctx.fillStyle = "#102c25";
  ctx.fillRect(park.x, park.y, park.w, park.h);
  for (let i = 0; i < 24; i += 1) {
    const x = park.x + 35 + (i * 97) % (park.w - 70);
    const y = park.y + 35 + (i * 61) % (park.h - 70);
    ctx.fillStyle = "#183f31";
    ctx.beginPath();
    ctx.arc(x, y, 18, 0, TAU);
    ctx.fill();
    ctx.fillStyle = "#2c7651";
    ctx.beginPath();
    ctx.arc(x - 3, y - 5, 13, 0, TAU);
    ctx.fill();
  }
}

function drawBuildings() {
  for (const b of buildings) {
    ctx.fillStyle = "#070c14";
    ctx.fillRect(b.x + 8, b.y + 10, b.w, b.h);
    const gradient = ctx.createLinearGradient(b.x, b.y, b.x + b.w, b.y + b.h);
    gradient.addColorStop(0, `hsl(${b.hue} 30% 18%)`);
    gradient.addColorStop(1, "#0a111d");
    ctx.fillStyle = gradient;
    ctx.fillRect(b.x, b.y, b.w, b.h);
    ctx.strokeStyle = `hsla(${b.hue},90%,65%,.25)`;
    ctx.strokeRect(b.x, b.y, b.w, b.h);

    const nx = Math.max(2, Math.floor(b.w / 58));
    const ny = Math.max(2, Math.floor(b.h / 48));
    for (let y = 0; y < ny; y += 1) {
      for (let x = 0; x < nx; x += 1) {
        const on = ((x * 3 + y * 5 + Math.floor(elapsed * 0.15)) % 7) < 3;
        ctx.fillStyle = on ? `hsla(${(b.hue + 45) % 360},100%,72%,.62)` : "rgba(150,180,210,.06)";
        ctx.fillRect(b.x + 18 + x * 52, b.y + 18 + y * 42, 13, 8);
      }
    }
    if (b.label) {
      ctx.save();
      ctx.shadowBlur = 18;
      ctx.shadowColor = `hsl(${b.hue} 100% 65%)`;
      ctx.fillStyle = `hsl(${b.hue} 100% 70%)`;
      ctx.font = "900 22px system-ui";
      ctx.textAlign = "center";
      ctx.fillText(b.label, b.x + b.w / 2, b.y + 34);
      ctx.restore();
    }
  }
}

function drawShard(shard) {
  if (shard.taken) return;
  ctx.save();
  ctx.translate(shard.x, shard.y);
  ctx.rotate(elapsed * 1.8 + shard.phase);
  ctx.shadowBlur = 26;
  ctx.shadowColor = "#ff5fd1";
  ctx.fillStyle = "#ff5fd1";
  ctx.beginPath();
  ctx.moveTo(0, -13);
  ctx.lineTo(10, 0);
  ctx.lineTo(0, 13);
  ctx.lineTo(-10, 0);
  ctx.closePath();
  ctx.fill();
  ctx.restore();
}

function drawPedestrian(person) {
  ctx.fillStyle = person.colour;
  ctx.beginPath();
  ctx.arc(person.x, person.y - 3, 5.5, 0, TAU);
  ctx.fill();
  ctx.fillStyle = "#202633";
  ctx.fillRect(person.x - 4, person.y + 2, 8, 12);
}

function drawVehicle(vehicle, width, height, isPlayer = false) {
  ctx.save();
  ctx.translate(vehicle.x, vehicle.y);
  ctx.rotate(vehicle.angle);
  ctx.fillStyle = "rgba(0,0,0,.45)";
  ctx.fillRect(-width / 2 + 5, -height / 2 + 7, width, height);
  ctx.shadowBlur = isPlayer ? 26 : 12;
  ctx.shadowColor = vehicle.colour;
  ctx.fillStyle = vehicle.colour;
  ctx.beginPath();
  ctx.roundRect(-width / 2, -height / 2, width, height, 9);
  ctx.fill();
  ctx.shadowBlur = 0;
  ctx.fillStyle = "#07111c";
  ctx.fillRect(-9, -height / 2 + 5, 24, height - 10);
  ctx.fillStyle = "#e9fdff";
  ctx.fillRect(width / 2 - 5, -height / 2 + 5, 4, 7);
  ctx.fillRect(width / 2 - 5, height / 2 - 12, 4, 7);
  ctx.fillStyle = "#ff365f";
  ctx.fillRect(-width / 2 + 1, -height / 2 + 5, 3, 7);
  ctx.fillRect(-width / 2 + 1, height / 2 - 12, 3, 7);
  ctx.restore();
}

function drawPlayer() {
  if (player.inCar) return;
  ctx.save();
  ctx.translate(player.x, player.y);
  ctx.rotate(player.angle);
  ctx.shadowBlur = 18;
  ctx.shadowColor = "#8cff9e";
  ctx.fillStyle = "#8cff9e";
  ctx.beginPath();
  ctx.arc(0, 0, 11, 0, TAU);
  ctx.fill();
  ctx.fillStyle = "#06200e";
  ctx.beginPath();
  ctx.arc(5, -3, 2.5, 0, TAU);
  ctx.fill();
  ctx.restore();
}

function drawObjective() {
  const target = objective();
  if (!target) return;
  const pulse = 1 + Math.sin(elapsed * 4) * 0.08;
  ctx.save();
  ctx.translate(target.x, target.y);
  ctx.strokeStyle = target.colour;
  ctx.lineWidth = 4;
  ctx.shadowBlur = 24;
  ctx.shadowColor = target.colour;
  ctx.beginPath();
  ctx.arc(0, 0, 38 * pulse, 0, TAU);
  ctx.stroke();
  ctx.globalAlpha = 0.35;
  ctx.beginPath();
  ctx.arc(0, 0, 66 * pulse, 0, TAU);
  ctx.stroke();
  ctx.restore();
}

function drawParticles() {
  for (const particle of particles) {
    ctx.globalAlpha = clamp(particle.life / particle.maxLife, 0, 1);
    ctx.fillStyle = particle.colour;
    ctx.shadowBlur = 10;
    ctx.shadowColor = particle.colour;
    ctx.fillRect(particle.x - particle.size / 2, particle.y - particle.size / 2, particle.size, particle.size);
  }
  ctx.globalAlpha = 1;
  ctx.shadowBlur = 0;
}

function drawWorld() {
  ctx.save();
  ctx.translate(-camera.x, -camera.y);
  drawRoads();
  drawPark();
  drawBuildings();
  shards.forEach(drawShard);
  drawObjective();
  pedestrians.forEach(drawPedestrian);
  traffic.forEach((vehicle) => drawVehicle(vehicle, 56, 30));
  drawVehicle(car, car.w, car.h, true);
  drawPlayer();
  drawParticles();
  ctx.restore();
}

function drawNight() {
  const gradient = ctx.createLinearGradient(0, 0, 0, H);
  gradient.addColorStop(0, "rgba(3,8,25,.10)");
  gradient.addColorStop(1, "rgba(4,3,16,.33)");
  ctx.fillStyle = gradient;
  ctx.fillRect(0, 0, W, H);
  const actor = player.inCar ? car : player;
  const sx = actor.x - camera.x;
  const sy = actor.y - camera.y;
  const glow = ctx.createRadialGradient(sx, sy, 20, sx, sy, 270);
  glow.addColorStop(0, "rgba(86,240,255,.05)");
  glow.addColorStop(1, "rgba(0,0,0,0)");
  ctx.fillStyle = glow;
  ctx.fillRect(0, 0, W, H);
}

function drawRain(dt) {
  ctx.save();
  ctx.strokeStyle = "rgba(158,224,255,.18)";
  ctx.lineWidth = 1;
  for (const drop of rain) {
    drop.y += drop.speed * dt;
    drop.x -= drop.speed * 0.16 * dt;
    if (drop.y > H + 20) { drop.y = -20; drop.x = Math.random() * W; }
    if (drop.x < -20) drop.x = W + 20;
    ctx.beginPath();
    ctx.moveTo(drop.x, drop.y);
    ctx.lineTo(drop.x - drop.len * 0.35, drop.y + drop.len);
    ctx.stroke();
  }
  ctx.restore();
}

function drawMinimap() {
  const w = 220, h = 155, x = W - w - 18, y = 18, sx = w / WORLD_W, sy = h / WORLD_H;
  ctx.save();
  ctx.fillStyle = "rgba(3,8,18,.82)";
  ctx.strokeStyle = "rgba(98,245,255,.25)";
  ctx.beginPath();
  ctx.roundRect(x, y, w, h, 12);
  ctx.fill();
  ctx.stroke();
  ctx.clip();
  ctx.fillStyle = "#29333d";
  roads.forEach((road) => ctx.fillRect(x + road.x * sx, y + road.y * sy, road.w * sx, road.h * sy));
  ctx.fillStyle = "#101923";
  buildings.forEach((b) => ctx.fillRect(x + b.x * sx, y + b.y * sy, Math.max(2, b.w * sx), Math.max(2, b.h * sy)));
  const target = objective();
  if (target) {
    ctx.fillStyle = target.colour;
    ctx.beginPath();
    ctx.arc(x + target.x * sx, y + target.y * sy, 4, 0, TAU);
    ctx.fill();
  }
  const actor = player.inCar ? car : player;
  ctx.fillStyle = "#fff";
  ctx.beginPath();
  ctx.arc(x + actor.x * sx, y + actor.y * sy, 4, 0, TAU);
  ctx.fill();
  ctx.restore();
  ctx.fillStyle = "rgba(240,250,255,.65)";
  ctx.font = "700 10px system-ui";
  ctx.textAlign = "right";
  ctx.fillText("CITY MAP", x + w - 10, y + h - 8);
}

function drawHud() {
  const target = objective();
  ctx.save();
  ctx.fillStyle = "rgba(3,8,18,.82)";
  ctx.strokeStyle = "rgba(98,245,255,.22)";
  ctx.beginPath();
  ctx.roundRect(18, 18, 370, 126, 14);
  ctx.fill();
  ctx.stroke();
  ctx.fillStyle = "#62f5ff";
  ctx.font = "900 11px system-ui";
  ctx.textAlign = "left";
  ctx.fillText("NEON CITY // TECHNOLOGY PREVIEW", 34, 42);
  ctx.fillStyle = "#f2f9ff";
  ctx.font = "900 22px system-ui";
  const title = stage === 0 ? "GET TO THE CAR" : stage === 1 ? "RETRIEVE THE PACKAGE" : stage === 2 ? "DELIVER TO SAFEHOUSE" : "MISSION COMPLETE";
  ctx.fillText(title, 34, 70);
  if (target) {
    const actor = player.inCar ? car : player;
    ctx.fillStyle = "#93a6ba";
    ctx.font = "700 13px system-ui";
    ctx.fillText(`${target.label} • ${Math.round(distance(actor.x, actor.y, target.x, target.y) / 8)} m`, 34, 95);
  }
  ctx.fillStyle = "#ffd86b";
  ctx.font = "800 13px system-ui";
  ctx.fillText(`${credits.toLocaleString()} CR   •   DATA ${shardCount}/8`, 34, 119);

  if (player.inCar) {
    const speed = Math.round(Math.abs(car.speed) * 0.33);
    ctx.fillStyle = "rgba(3,8,18,.82)";
    ctx.beginPath();
    ctx.roundRect(18, H - 114, 318, 96, 14);
    ctx.fill();
    ctx.fillStyle = "#f4fbff";
    ctx.font = "900 34px system-ui";
    ctx.fillText(String(speed).padStart(3, "0"), 34, H - 62);
    ctx.fillStyle = "#93a6ba";
    ctx.font = "800 11px system-ui";
    ctx.fillText("KM/H", 110, H - 63);
    ctx.fillText("BOOST", 34, H - 38);
    ctx.fillStyle = "rgba(255,255,255,.09)";
    ctx.fillRect(88, H - 47, 218, 10);
    const boostGradient = ctx.createLinearGradient(88, 0, 306, 0);
    boostGradient.addColorStop(0, "#62f5ff");
    boostGradient.addColorStop(1, "#ff5fd1");
    ctx.fillStyle = boostGradient;
    ctx.fillRect(88, H - 47, 218 * (car.boost / 100), 10);
  } else if (distance(player.x, player.y, car.x, car.y) < 95) {
    ctx.fillStyle = "rgba(3,8,18,.84)";
    ctx.beginPath();
    ctx.roundRect(18, H - 74, 230, 48, 12);
    ctx.fill();
    ctx.fillStyle = "#fff";
    ctx.font = "800 15px system-ui";
    ctx.fillText("E  ENTER VEHICLE", 34, H - 44);
  }

  if (messageTime > 0) {
    const alpha = clamp(messageTime, 0, 1);
    ctx.globalAlpha = alpha;
    ctx.font = "900 20px system-ui";
    const boxWidth = ctx.measureText(message).width + 42;
    ctx.fillStyle = "rgba(3,8,18,.88)";
    ctx.beginPath();
    ctx.roundRect(W / 2 - boxWidth / 2, H - 78, boxWidth, 48, 12);
    ctx.fill();
    ctx.fillStyle = "#fff";
    ctx.textAlign = "center";
    ctx.fillText(message, W / 2, H - 47);
    ctx.globalAlpha = 1;
  }

  if (paused) {
    ctx.fillStyle = "rgba(0,0,0,.56)";
    ctx.fillRect(0, 0, W, H);
    ctx.fillStyle = "#fff";
    ctx.textAlign = "center";
    ctx.font = "1000 54px system-ui";
    ctx.fillText("PAUSED", W / 2, H / 2);
    ctx.font = "700 16px system-ui";
    ctx.fillStyle = "#93a6ba";
    ctx.fillText("Press P to continue", W / 2, H / 2 + 34);
  }
  ctx.restore();
}

function render(dt) {
  const sx = shake > 0 ? (Math.random() - 0.5) * shake : 0;
  const sy = shake > 0 ? (Math.random() - 0.5) * shake : 0;
  ctx.save();
  ctx.translate(sx, sy);
  ctx.fillStyle = "#04070d";
  ctx.fillRect(-20, -20, W + 40, H + 40);
  drawWorld();
  drawNight();
  ctx.restore();
  drawRain(dt);
  drawMinimap();
  drawHud();
  if (flash > 0) {
    ctx.fillStyle = `rgba(255,255,255,${flash * 0.22})`;
    ctx.fillRect(0, 0, W, H);
  }
}

let tickTimer = null;
let tickCount = 0;

function tick() {
  const now = performance.now();
  const dt = Math.min(0.04, Math.max(0.001, (now - last) / 1000));
  last = now;

  try {
    update(dt);
    render(dt);
    pressed = new Set();
    tickCount += 1;

    if (tickCount % 20 === 0 && runtimeStatus) {
      const mode = player.inCar ? "CAR" : "ON FOOT";
      runtimeStatus.textContent = `ENGINE OK • ${mode} • ${Math.round(1 / dt)} FPS • INPUT ${lastInput}`;
      runtimeStatus.classList.remove("error");
    }
  } catch (error) {
    if (runtimeStatus) {
      runtimeStatus.textContent = `RUNTIME ERROR: ${error?.message ?? error}`;
      runtimeStatus.classList.add("error");
    }
    console.error("Neon City runtime error", error);
  }
}

function startTicker() {
  if (tickTimer !== null) return;
  last = performance.now();
  tick();
  tickTimer = window.setInterval(tick, 16);
}

function normaliseKey(event) {
  const codeMap = {
    KeyW: "w",
    KeyA: "a",
    KeyS: "s",
    KeyD: "d",
    KeyE: "e",
    KeyP: "p",
    KeyR: "r",
    ShiftLeft: "shift",
    ShiftRight: "shift",
    ArrowUp: "arrowup",
    ArrowDown: "arrowdown",
    ArrowLeft: "arrowleft",
    ArrowRight: "arrowright",
  };
  return codeMap[event.code] ?? event.key.toLowerCase();
}

document.addEventListener("keydown", (event) => {
  const key = normaliseKey(event);
  if (["w", "a", "s", "d", "e", "p", "r", "shift", "arrowup", "arrowdown", "arrowleft", "arrowright"].includes(key)) {
    event.preventDefault();
  }
  if (!keys.has(key)) pressed.add(key);
  keys.add(key);
  latchKey(key);
  lastInput = key.toUpperCase();
  if (key === "p" && running) paused = !paused;
  if (key === "r" && running) reset();
}, true);

document.addEventListener("keyup", (event) => {
  keys.delete(normaliseKey(event));
}, true);

window.addEventListener("blur", () => {
  keys.clear();
  pressed.clear();
});

canvas.addEventListener("pointerdown", () => canvas.focus());

playButton.addEventListener("click", () => {
  try { audio ??= new AudioContext(); } catch { audio = null; }
  startOverlay.classList.add("hidden");
  reset();
  canvas.focus();
});
againButton.addEventListener("click", () => {
  finishOverlay.classList.add("hidden");
  reset();
});

camera.x = clamp(player.x - W / 2, 0, WORLD_W - W);
camera.y = clamp(player.y - H / 2, 0, WORLD_H - H);
startTicker();
