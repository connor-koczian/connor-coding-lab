"use strict";
const canvas=document.getElementById("game"),ctx=canvas.getContext("2d");
const start=document.getElementById("start"),over=document.getElementById("gameOver"),play=document.getElementById("play"),again=document.getElementById("again"),runtime=document.getElementById("runtime"),resultStats=document.getElementById("resultStats");
const W=canvas.width,H=canvas.height,TAU=Math.PI*2,keys=new Set();
let running=false,paused=false,last=performance.now(),score=0,wave=1,combo=1,comboTimer=0,shake=0,flash=0,spawnTimer=0,shotTimer=0,boss=null,tickCount=0;
const arena={w:2400,h:1600},camera={x:0,y:0};
const snake={x:1200,y:800,a:0,speed:245,turn:3.2,hp:100,shield:100,dash:100,segments:[],trail:[]};
const enemies=[],shots=[],enemyShots=[],cores=[],particles=[],powerups=[];
function clamp(v,a,b){return Math.max(a,Math.min(b,v))}function dist(a,b,c,d){return Math.hypot(a-c,b-d)}
function burst(x,y,c,n=20,f=160){for(let i=0;i<n;i++){const a=Math.random()*TAU,s=f*(.25+Math.random());particles.push({x,y,vx:Math.cos(a)*s,vy:Math.sin(a)*s,life:.35+Math.random()*.55,max:.9,size:2+Math.random()*5,c})}}
function reset(){
  Object.assign(snake,{x:1200,y:800,a:0,speed:245,hp:100,shield:100,dash:100});
  snake.segments=Array.from({length:18},(_,i)=>({x:snake.x-i*15,y:snake.y}));
  snake.trail=[];enemies.length=shots.length=enemyShots.length=cores.length=particles.length=powerups.length=0;
  score=0;wave=1;combo=1;comboTimer=0;shake=0;flash=0;spawnTimer=.4;shotTimer=0;boss=null;running=true;paused=false;
  for(let i=0;i<22;i++)spawnCore();
}
function spawnCore(){cores.push({x:120+Math.random()*(arena.w-240),y:120+Math.random()*(arena.h-240),phase:Math.random()*TAU})}
function spawnEnemy(elite=false){
  const edge=Math.floor(Math.random()*4);let x,y;if(edge===0){x=40;y=Math.random()*arena.h}else if(edge===1){x=arena.w-40;y=Math.random()*arena.h}else if(edge===2){x=Math.random()*arena.w;y=40}else{x=Math.random()*arena.w;y=arena.h-40}
  enemies.push({x,y,vx:0,vy:0,r:elite?19:13,hp:elite?5:2,maxHp:elite?5:2,speed:elite?120:155,elite,fire:1+Math.random()*1.2,hue:elite?320:190});
}
function spawnBoss(){boss={x:arena.w/2,y:180,r:64,hp:120+wave*18,maxHp:120+wave*18,a:0,fire:.4,burst:2.8};burst(boss.x,boss.y,"#ff4fd8",80,260);shake=18}
function nearestEnemy(){
  let best=null,bd=Infinity;for(const e of enemies){const d=dist(snake.x,snake.y,e.x,e.y);if(d<bd){bd=d;best=e}}
  if(boss){const d=dist(snake.x,snake.y,boss.x,boss.y);if(d<bd)best=boss}return best
}
function firePlayer(){
  const t=nearestEnemy();if(!t)return;const a=Math.atan2(t.y-snake.y,t.x-snake.x);
  shots.push({x:snake.x+Math.cos(a)*24,y:snake.y+Math.sin(a)*24,vx:Math.cos(a)*620,vy:Math.sin(a)*620,life:1.2,r:5});burst(snake.x,snake.y,"#59f7ff",3,65)
}
function damage(amount){
  if(snake.shield>0){const used=Math.min(snake.shield,amount*1.4);snake.shield-=used;amount=Math.max(0,amount-used/1.4)}
  snake.hp-=amount;shake=12;flash=.35;if(snake.hp<=0)endRun()
}
function endRun(){running=false;resultStats.textContent=`Score ${score.toLocaleString()} • Wave ${wave} • Length ${snake.segments.length}`;over.classList.remove("hidden")}
function killEnemy(e){
  score+=Math.round((e.elite?400:150)*combo);combo=Math.min(8,combo+.25);comboTimer=3.5;burst(e.x,e.y,e.elite?"#ff4fd8":"#59f7ff",e.elite?28:16,190);
  if(Math.random()<.18)powerups.push({x:e.x,y:e.y,type:["shield","heal","rapid"][Math.floor(Math.random()*3)],life:9});
}
function updateSnake(dt){
  let turn=0;if(keys.has("a")||keys.has("arrowleft"))turn-=1;if(keys.has("d")||keys.has("arrowright"))turn+=1;snake.a+=turn*snake.turn*dt;
  const accelerating=keys.has("w")||keys.has("arrowup"),braking=keys.has("s")||keys.has("arrowdown");
  const target=accelerating?340:braking?170:245;snake.speed+=(target-snake.speed)*Math.min(1,dt*4);
  if(keys.has(" ")&&snake.dash>0){snake.speed+=420;snake.dash=Math.max(0,snake.dash-70*dt);if(Math.random()<dt*35)burst(snake.x-Math.cos(snake.a)*18,snake.y-Math.sin(snake.a)*18,"#ffd35c",2,75)}
  else snake.dash=Math.min(100,snake.dash+15*dt);
  snake.x=clamp(snake.x+Math.cos(snake.a)*snake.speed*dt,24,arena.w-24);snake.y=clamp(snake.y+Math.sin(snake.a)*snake.speed*dt,24,arena.h-24);
  snake.trail.unshift({x:snake.x,y:snake.y});if(snake.trail.length>500)snake.trail.pop();
  for(let i=0;i<snake.segments.length;i++){const p=snake.trail[Math.min(snake.trail.length-1,(i+1)*7)];if(p){snake.segments[i].x=p.x;snake.segments[i].y=p.y}}
  for(let i=cores.length-1;i>=0;i--){const c=cores[i];if(dist(snake.x,snake.y,c.x,c.y)<25){cores.splice(i,1);spawnCore();score+=Math.round(100*combo);combo=Math.min(8,combo+.15);comboTimer=3;snake.segments.push({x:snake.segments.at(-1)?.x??snake.x,y:snake.segments.at(-1)?.y??snake.y});snake.shield=Math.min(100,snake.shield+6);burst(c.x,c.y,"#79ff9b",16,150)}}
  for(let i=powerups.length-1;i>=0;i--){const p=powerups[i];p.life-=dt;if(p.life<=0){powerups.splice(i,1);continue}if(dist(snake.x,snake.y,p.x,p.y)<28){if(p.type==="shield")snake.shield=100;if(p.type==="heal")snake.hp=Math.min(100,snake.hp+35);if(p.type==="rapid")shotTimer=-1;score+=250;burst(p.x,p.y,"#ffd35c",28,190);powerups.splice(i,1)}}
}
function updateEnemies(dt){
  spawnTimer-=dt;if(spawnTimer<=0&&enemies.length<8+wave*2){spawnEnemy(Math.random()<Math.min(.1+.03*wave,.35));spawnTimer=Math.max(.28,1.15-wave*.06)}
  for(let i=enemies.length-1;i>=0;i--){const e=enemies[i],a=Math.atan2(snake.y-e.y,snake.x-e.x);e.vx+=(Math.cos(a)*e.speed-e.vx)*Math.min(1,dt*2.8);e.vy+=(Math.sin(a)*e.speed-e.vy)*Math.min(1,dt*2.8);e.x+=e.vx*dt;e.y+=e.vy*dt;
    if(e.elite){e.fire-=dt;if(e.fire<=0){const s=Math.atan2(snake.y-e.y,snake.x-e.x);enemyShots.push({x:e.x,y:e.y,vx:Math.cos(s)*300,vy:Math.sin(s)*300,life:3,r:6});e.fire=.9+Math.random()*.7}}
    if(dist(e.x,e.y,snake.x,snake.y)<e.r+15){damage(e.elite?18:10);burst(e.x,e.y,"#ff6b86",18,170);enemies.splice(i,1);continue}
  }
}
function updateBoss(dt){
  if(!boss&&score>0&&score>=(wave*2600)){spawnBoss()}
  if(!boss)return;const a=Math.atan2(snake.y-boss.y,snake.x-boss.x);boss.a+=dt;boss.x+=Math.cos(a+Math.sin(boss.a)*.7)*70*dt;boss.y+=Math.sin(a+Math.sin(boss.a)*.7)*70*dt;boss.fire-=dt;boss.burst-=dt;
  if(boss.fire<=0){const base=Math.atan2(snake.y-boss.y,snake.x-boss.x);for(let k=-1;k<=1;k++){const s=base+k*.18;enemyShots.push({x:boss.x,y:boss.y,vx:Math.cos(s)*340,vy:Math.sin(s)*340,life:3.6,r:7})}boss.fire=.65}
  if(boss.burst<=0){for(let k=0;k<14;k++){const s=k/14*TAU;enemyShots.push({x:boss.x,y:boss.y,vx:Math.cos(s)*230,vy:Math.sin(s)*230,life:4,r:6})}boss.burst=3.1;shake=8}
  if(dist(boss.x,boss.y,snake.x,snake.y)<boss.r+18)damage(30*dt);
}
function updateShots(dt){
  shotTimer-=dt;if(shotTimer<=0){firePlayer();shotTimer=.18}
  for(let i=shots.length-1;i>=0;i--){const s=shots[i];s.x+=s.vx*dt;s.y+=s.vy*dt;s.life-=dt;let hit=false;
    for(let j=enemies.length-1;j>=0&&!hit;j--){const e=enemies[j];if(dist(s.x,s.y,e.x,e.y)<s.r+e.r){e.hp--;hit=true;burst(s.x,s.y,"#59f7ff",7,90);if(e.hp<=0){killEnemy(e);enemies.splice(j,1)}}}
    if(!hit&&boss&&dist(s.x,s.y,boss.x,boss.y)<s.r+boss.r){boss.hp--;hit=true;burst(s.x,s.y,"#ff4fd8",5,80);if(boss.hp<=0){score+=5000;burst(boss.x,boss.y,"#ffd35c",120,340);boss=null;wave++;enemies.length=0;shake=24;flash=.8}}
    if(hit||s.life<=0)shots.splice(i,1);
  }
  for(let i=enemyShots.length-1;i>=0;i--){const s=enemyShots[i];s.x+=s.vx*dt;s.y+=s.vy*dt;s.life-=dt;if(dist(s.x,s.y,snake.x,snake.y)<s.r+13){damage(12);burst(s.x,s.y,"#ff6b86",12,110);enemyShots.splice(i,1)}else if(s.life<=0)enemyShots.splice(i,1)}
}
function updateParticles(dt){for(const p of particles){p.x+=p.vx*dt;p.y+=p.vy*dt;p.vx*=Math.pow(.08,dt);p.vy*=Math.pow(.08,dt);p.life-=dt}for(let i=particles.length-1;i>=0;i--)if(particles[i].life<=0)particles.splice(i,1)}
function update(dt){if(!running||paused)return;comboTimer-=dt;if(comboTimer<=0){combo=1;comboTimer=0}shake=Math.max(0,shake-dt*30);flash=Math.max(0,flash-dt*2);updateSnake(dt);updateEnemies(dt);updateBoss(dt);updateShots(dt);updateParticles(dt);camera.x+=(clamp(snake.x-W/2,0,arena.w-W)-camera.x)*Math.min(1,dt*5);camera.y+=(clamp(snake.y-H/2,0,arena.h-H)-camera.y)*Math.min(1,dt*5)}
function circle(x,y,r,c,glow=0){ctx.save();ctx.fillStyle=c;if(glow){ctx.shadowBlur=glow;ctx.shadowColor=c}ctx.beginPath();ctx.arc(x,y,r,0,TAU);ctx.fill();ctx.restore()}
function render(){
  const ox=(Math.random()-.5)*shake,oy=(Math.random()-.5)*shake;ctx.save();ctx.translate(ox,oy);ctx.fillStyle="#050812";ctx.fillRect(-20,-20,W+40,H+40);ctx.save();ctx.translate(-camera.x,-camera.y);
  ctx.strokeStyle="#0e2233";ctx.lineWidth=1;for(let x=0;x<arena.w;x+=80){ctx.beginPath();ctx.moveTo(x,0);ctx.lineTo(x,arena.h);ctx.stroke()}for(let y=0;y<arena.h;y+=80){ctx.beginPath();ctx.moveTo(0,y);ctx.lineTo(arena.w,y);ctx.stroke()}
  ctx.strokeStyle="#1d5f73";ctx.lineWidth=4;ctx.strokeRect(12,12,arena.w-24,arena.h-24);
  cores.forEach(c=>{const p=1+Math.sin(performance.now()/300+c.phase)*.18;circle(c.x,c.y,8*p,"#79ff9b",18)});
  powerups.forEach(p=>{circle(p.x,p.y,13,p.type==="heal"?"#ff6b86":p.type==="shield"?"#59f7ff":"#ffd35c",20);ctx.fillStyle="#07101a";ctx.font="900 11px system-ui";ctx.textAlign="center";ctx.fillText(p.type[0].toUpperCase(),p.x,p.y+4)});
  for(let i=snake.segments.length-1;i>=0;i--){const s=snake.segments[i],t=i/snake.segments.length;circle(s.x,s.y,8+5*(1-t),`hsl(${185+120*t} 95% ${58+8*t}%)`,i<8?10:0)}
  circle(snake.x,snake.y,15,"#ffffff",24);circle(snake.x+Math.cos(snake.a)*7,snake.y+Math.sin(snake.a)*7,5,"#59f7ff",12);
  enemies.forEach(e=>{circle(e.x,e.y,e.r,e.elite?"#ff4fd8":"#ff6b86",18);ctx.fillStyle="#10131b";ctx.fillRect(e.x-e.r*.45,e.y-e.r*.45,e.r*.9,e.r*.9)});
  if(boss){circle(boss.x,boss.y,boss.r,"#ff4fd8",34);circle(boss.x,boss.y,boss.r*.62,"#39133d",0);ctx.strokeStyle="#ffd35c";ctx.lineWidth=4;ctx.beginPath();ctx.arc(boss.x,boss.y,boss.r*.78,boss.a,boss.a+Math.PI*1.35);ctx.stroke()}
  shots.forEach(s=>circle(s.x,s.y,s.r,"#59f7ff",16));enemyShots.forEach(s=>circle(s.x,s.y,s.r,"#ff6b86",14));
  particles.forEach(p=>{ctx.globalAlpha=clamp(p.life/p.max,0,1);circle(p.x,p.y,p.size,p.c,8)});ctx.globalAlpha=1;ctx.restore();ctx.restore();
  ctx.fillStyle="rgba(3,8,18,.86)";ctx.beginPath();ctx.roundRect(18,18,370,128,14);ctx.fill();ctx.fillStyle="#59f7ff";ctx.font="900 11px system-ui";ctx.textAlign="left";ctx.fillText("SNAKE // OVERDRIVE",34,42);ctx.fillStyle="#fff";ctx.font="900 28px system-ui";ctx.fillText(score.toLocaleString(),34,76);ctx.fillStyle="#93a6ba";ctx.font="800 12px system-ui";ctx.fillText(`WAVE ${wave}   •   LENGTH ${snake.segments.length}   •   COMBO x${combo.toFixed(1)}`,34,100);
  const bar=(y,val,c,label)=>{ctx.fillStyle="#93a6ba";ctx.font="800 10px system-ui";ctx.fillText(label,34,y-4);ctx.fillStyle="#ffffff14";ctx.fillRect(88,y-12,250,8);ctx.fillStyle=c;ctx.fillRect(88,y-12,250*clamp(val/100,0,1),8)};bar(124,snake.hp,"#ff6b86","HULL");bar(142,snake.shield,"#59f7ff","SHIELD");
  ctx.fillStyle="#93a6ba";ctx.fillText("DASH",W-300,H-34);ctx.fillStyle="#ffffff14";ctx.fillRect(W-248,H-43,214,9);ctx.fillStyle="#ffd35c";ctx.fillRect(W-248,H-43,214*(snake.dash/100),9);
  if(boss){ctx.fillStyle="#ffffff14";ctx.fillRect(W/2-250,24,500,12);ctx.fillStyle="#ff4fd8";ctx.fillRect(W/2-250,24,500*(boss.hp/boss.maxHp),12);ctx.fillStyle="#fff";ctx.font="900 11px system-ui";ctx.textAlign="center";ctx.fillText("BOSS CORE",W/2,53)}
  if(paused){ctx.fillStyle="#000b";ctx.fillRect(0,0,W,H);ctx.fillStyle="#fff";ctx.font="1000 54px system-ui";ctx.textAlign="center";ctx.fillText("PAUSED",W/2,H/2)}
  if(flash>0){ctx.fillStyle=`rgba(255,255,255,${flash*.22})`;ctx.fillRect(0,0,W,H)}
}
function tick(){const now=performance.now(),dt=Math.min(.04,Math.max(.001,(now-last)/1000));last=now;try{update(dt);render();tickCount++;if(tickCount%20===0){runtime.textContent=`ENGINE OK • ${Math.round(1/dt)} FPS • ${enemies.length} HOSTILES`;runtime.classList.remove("error")}}catch(e){runtime.textContent=`RUNTIME ERROR: ${e?.message??e}`;runtime.classList.add("error");console.error(e)}}
setInterval(tick,16);
document.addEventListener("keydown",e=>{const map={KeyW:"w",KeyA:"a",KeyS:"s",KeyD:"d",Space:" ",ArrowUp:"arrowup",ArrowDown:"arrowdown",ArrowLeft:"arrowleft",ArrowRight:"arrowright",KeyP:"p",KeyR:"r"},k=map[e.code]??e.key.toLowerCase();if(["w","a","s","d"," ","arrowup","arrowdown","arrowleft","arrowright"].includes(k))e.preventDefault();keys.add(k);if(k==="p"&&running)paused=!paused;if(k==="r"&&running)reset()},true);
document.addEventListener("keyup",e=>{const map={KeyW:"w",KeyA:"a",KeyS:"s",KeyD:"d",Space:" ",ArrowUp:"arrowup",ArrowDown:"arrowdown",ArrowLeft:"arrowleft",ArrowRight:"arrowright"},k=map[e.code]??e.key.toLowerCase();keys.delete(k)},true);
window.addEventListener("blur",()=>keys.clear());
play.addEventListener("click",()=>{start.classList.add("hidden");reset();canvas.focus()});again.addEventListener("click",()=>{over.classList.add("hidden");reset();canvas.focus()});
render();