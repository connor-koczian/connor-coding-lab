import math
import random
import pygame


def main() -> None:
    pygame.init()
    pygame.font.init()

    # --- Screen Setup (Giant 1400x950 Arena) ---
    WIDTH = 1400
    HEIGHT = 950
    GRID_SIZE = 25
    BORDER_THICKNESS = 25

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Connor's Snake: The 3-Stage Grand Championship 🏆🐍")
    clock = pygame.time.Clock()

    # --- Fonts ---
    font_xl = pygame.font.SysFont("comicsansms", 64, bold=True)
    font_large = pygame.font.SysFont("comicsansms", 36, bold=True)
    font_medium = pygame.font.SysFont("comicsansms", 24, bold=True)
    font_small = pygame.font.SysFont("comicsansms", 18, bold=True)

    # --- 3-Stage World Campaign ---
    STAGES = [
        {
            "stage_num": 1,
            "name": "Stage 1: Emerald Realm",
            "target_credits": 25000,
            "border_color": (34, 197, 94),     # Emerald Green
            "border_glow": (22, 101, 52),
            "bg_color": (15, 23, 42),          # Space Navy
        },
        {
            "stage_num": 2,
            "name": "Stage 2: Neon Metropolis",
            "target_credits": 40000,
            "border_color": (34, 211, 238),    # Cyber Cyan
            "border_glow": (14, 116, 144),
            "bg_color": (20, 15, 38),          # Deep Cyber Purple
        },
        {
            "stage_num": 3,
            "name": "Stage 3: Mythic Dragon Lair (FINAL)",
            "target_credits": 50000,
            "border_color": (250, 204, 21),    # Radiant Gold
            "border_glow": (225, 29, 72),      # Fiery Crimson
            "bg_color": (28, 12, 24),          # Volcanic Shadow
        },
    ]

    # Food Definitions
    FOOD_TYPES = {
        "apple": {
            "name": "Red Apple",
            "credits": 5,
            "score": 10,
            "growth": 1,
            "interval": 1500,
            "max": 18,
            "color": (244, 63, 94),
        },
        "golden_apple": {
            "name": "Golden Apple",
            "credits": 20,
            "score": 50,
            "growth": 2,
            "interval": 5000,
            "max": 6,
            "color": (250, 204, 21),
        },
        "berry": {
            "name": "Cosmic Berry",
            "credits": 15,
            "score": 35,
            "growth": 1,
            "interval": 7000,
            "max": 5,
            "color": (168, 85, 247),
        },
        "watermelon": {
            "name": "Mega Watermelon",
            "credits": 40,
            "score": 100,
            "growth": 3,
            "interval": 11000,
            "max": 3,
            "color": (251, 113, 133),
        },
        "diamond": {
            "name": "Diamond Star Fruit",
            "credits": 80,
            "score": 250,
            "growth": 4,
            "interval": 18000,
            "max": 2,
            "color": (56, 189, 248),
        },
    }

    LEVEL_THEMES = [
        {"name": "Baby Viper", "head": (74, 222, 128), "body": (34, 197, 94)},
        {"name": "Cobra Striker", "head": (56, 189, 248), "body": (14, 165, 233)},
        {"name": "Golden Python", "head": (250, 204, 21), "body": (234, 179, 8)},
        {"name": "Shadow Hydra", "head": (192, 132, 252), "body": (147, 51, 234)},
        {"name": "Solar Dragon", "head": (244, 63, 94), "body": (225, 29, 72)},
        {"name": "Titan Behemoth", "head": (14, 165, 233), "body": (2, 132, 199)},
        {"name": "Cosmic Leviathan", "head": (244, 114, 182), "body": (219, 39, 119)},
        {"name": "Quantum Colossus", "head": (52, 211, 153), "body": (5, 150, 105)},
        {"name": "Void Overlord", "head": (168, 85, 247), "body": (88, 28, 135)},
        {"name": "APEX OMEGA DRAGON", "head": (251, 146, 60), "body": (234, 88, 12)},
    ]

    def is_inside_arena(pos: tuple[int, int]) -> bool:
        x, y = pos
        return (
            BORDER_THICKNESS <= x < WIDTH - BORDER_THICKNESS
            and BORDER_THICKNESS <= y < HEIGHT - BORDER_THICKNESS
        )

    def spawn_random_cell(occupied: set[tuple[int, int]]) -> tuple[int, int]:
        min_cell_x = BORDER_THICKNESS // GRID_SIZE
        max_cell_x = (WIDTH - BORDER_THICKNESS) // GRID_SIZE - 1
        min_cell_y = BORDER_THICKNESS // GRID_SIZE
        max_cell_y = (HEIGHT - BORDER_THICKNESS) // GRID_SIZE - 1
        for _ in range(300):
            x = random.randint(min_cell_x, max_cell_x) * GRID_SIZE
            y = random.randint(min_cell_y, max_cell_y) * GRID_SIZE
            if (x, y) not in occupied:
                return (x, y)
        return (WIDTH // 2, HEIGHT // 2)

    def reset_game():
        start_x = (WIDTH // 2 // GRID_SIZE) * GRID_SIZE
        start_y = (HEIGHT // 2 // GRID_SIZE) * GRID_SIZE
        snake = [
            (start_x, start_y),
            (start_x - GRID_SIZE, start_y),
            (start_x - 2 * GRID_SIZE, start_y),
        ]
        change_x = GRID_SIZE
        change_y = 0
        score = 0
        credits = 0
        growth_level = 1
        current_stage_idx = 0
        game_over = False
        game_won = False
        banner_text = ""
        banner_timer = 0
        pending_growth = 0

        occupied = set(snake)
        food_items: dict[str, list[tuple[int, int]]] = {
            "apple": [],
            "golden_apple": [],
            "berry": [],
            "watermelon": [],
            "diamond": [],
        }
        oranges: list[tuple[int, int]] = []

        for _ in range(5):
            pos = spawn_random_cell(occupied)
            food_items["apple"].append(pos)
            occupied.add(pos)

        pos_g = spawn_random_cell(occupied)
        food_items["golden_apple"].append(pos_g)
        occupied.add(pos_g)

        now = pygame.time.get_ticks()
        spawn_timers = {k: now for k in FOOD_TYPES}
        game_start_time = now

        return (
            snake,
            change_x,
            change_y,
            score,
            credits,
            growth_level,
            current_stage_idx,
            game_over,
            game_won,
            banner_text,
            banner_timer,
            pending_growth,
            food_items,
            oranges,
            spawn_timers,
            game_start_time,
        )

    (
        snake,
        change_x,
        change_y,
        score,
        credits,
        growth_level,
        current_stage_idx,
        game_over,
        game_won,
        banner_text,
        banner_timer,
        pending_growth,
        food_items,
        oranges,
        spawn_timers,
        game_start_time,
    ) = reset_game()

    high_score = 0
    running = True

    while running:
        current_time = pygame.time.get_ticks()
        current_stage = STAGES[current_stage_idx]

        # --- Event Handling ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if game_over or game_won:
                    if event.key == pygame.K_SPACE:
                        (
                            snake,
                            change_x,
                            change_y,
                            score,
                            credits,
                            growth_level,
                            current_stage_idx,
                            game_over,
                            game_won,
                            banner_text,
                            banner_timer,
                            pending_growth,
                            food_items,
                            oranges,
                            spawn_timers,
                            game_start_time,
                        ) = reset_game()
                    elif event.key == pygame.K_ESCAPE:
                        running = False
                else:
                    if (event.key == pygame.K_UP or event.key == pygame.K_w) and change_y == 0:
                        change_x = 0
                        change_y = -GRID_SIZE
                    elif (event.key == pygame.K_DOWN or event.key == pygame.K_s) and change_y == 0:
                        change_x = 0
                        change_y = GRID_SIZE
                    elif (event.key == pygame.K_LEFT or event.key == pygame.K_a) and change_x == 0:
                        change_x = -GRID_SIZE
                        change_y = 0
                    elif (event.key == pygame.K_RIGHT or event.key == pygame.K_d) and change_x == 0:
                        change_x = GRID_SIZE
                        change_y = 0

        # --- Game Logic ---
        if not game_over and not game_won:
            # 1. 10-Second Level-Up Rule (Snake Grows & Mythic Orange Spawns!)
            time_alive = current_time - game_start_time
            if time_alive >= growth_level * 10000:
                growth_level += 1
                pending_growth += 4
                credits += 25
                score += 100

                # Spawn Mythic Orange (+10,000 Credits)
                occupied = set(snake)
                for flist in food_items.values():
                    occupied.update(flist)
                occupied.update(oranges)
                new_orange = spawn_random_cell(occupied)
                oranges.append(new_orange)

                theme_idx = min(growth_level - 1, len(LEVEL_THEMES) - 1)
                theme_name = LEVEL_THEMES[theme_idx]["name"]
                banner_text = f"⚡ SIZE UP! {theme_name.upper()}! 🍊 MYTHIC ORANGE SPAWNED (+10,000 CR)! ⚡"
                banner_timer = 50

            # 2. Spawn Regular Food
            occupied = set(snake)
            for f_list in food_items.values():
                occupied.update(f_list)
            occupied.update(oranges)

            for f_type, f_data in FOOD_TYPES.items():
                if current_time - spawn_timers[f_type] >= f_data["interval"]:
                    spawn_timers[f_type] = current_time
                    if len(food_items[f_type]) < f_data["max"]:
                        new_f = spawn_random_cell(occupied)
                        food_items[f_type].append(new_f)
                        occupied.add(new_f)

            # 3. Move Snake Head
            head_x, head_y = snake[0]
            new_head = (head_x + change_x, head_y + change_y)

            # Wall Crash
            if not is_inside_arena(new_head):
                game_over = True

            # Self Crash
            if new_head in snake:
                game_over = True

            if not game_over:
                snake.insert(0, new_head)

                # 4. Check Eating Mythic Orange (+10,000 CR)
                eaten_orange = None
                for o in oranges:
                    if new_head == o:
                        eaten_orange = o
                        break

                # 5. Check Eating Regular Food
                eaten_type = None
                eaten_pos = None
                for f_type, f_list in food_items.items():
                    if new_head in f_list:
                        eaten_type = f_type
                        eaten_pos = new_head
                        break

                if eaten_orange:
                    oranges.remove(eaten_orange)
                    credits += 10000
                    score += 1000
                    pending_growth += 5
                    banner_text = "🍊 MYTHIC ORANGE! +10,000 CREDITS! 🍊"
                    banner_timer = 45
                elif eaten_type:
                    food_items[eaten_type].remove(eaten_pos)
                    f_info = FOOD_TYPES[eaten_type]
                    credits += f_info["credits"]
                    score += f_info["score"]
                    pending_growth += (f_info["growth"] - 1)

                    if eaten_type == "diamond":
                        banner_text = f"💎 DIAMOND STAR FRUIT! +{f_info['credits']} CR! 💎"
                        banner_timer = 30
                    elif eaten_type == "watermelon":
                        banner_text = f"🍉 MEGA WATERMELON! +{f_info['credits']} CR! 🍉"
                        banner_timer = 25
                    elif eaten_type == "golden_apple":
                        banner_text = f"✨ GOLDEN APPLE! +{f_info['credits']} CR! ✨"
                        banner_timer = 20
                    elif eaten_type == "berry":
                        banner_text = f"🍇 COSMIC BERRY! +{f_info['credits']} CR! 🍇"
                        banner_timer = 16
                    else:
                        banner_text = f"🍎 RED APPLE! +{f_info['credits']} CR! 🍎"
                        banner_timer = 12
                else:
                    if pending_growth > 0:
                        pending_growth -= 1
                    else:
                        snake.pop()

                if score > high_score:
                    high_score = score

                # 6. Check Level Progression: Level 1 (25k) -> Level 2 (40k) -> Final Level 3 (50k)
                stage_target = current_stage["target_credits"]
                if credits >= stage_target:
                    if current_stage_idx == 0:
                        # Move to Stage 2 (Goal: 40,000 Credits)
                        current_stage_idx = 1
                        banner_text = "🚀 STAGE 1 CLEAR (25,000 CR)! ENTERING STAGE 2 (GOAL: 40,000 CR)! 🚀"
                        banner_timer = 70
                    elif current_stage_idx == 1:
                        # Move to Stage 3 (Goal: 50,000 Credits)
                        current_stage_idx = 2
                        banner_text = "🔥 STAGE 2 CLEAR (40,000 CR)! ENTERING FINAL STAGE 3 (GOAL: 50,000 CR)! 🔥"
                        banner_timer = 70
                    elif current_stage_idx == 2:
                        # Reached 50,000 Credits on Final Stage -> YOU WIN!
                        game_won = True

        # --- Drawing the Arena ---
        current_stage = STAGES[current_stage_idx]
        screen.fill(current_stage["bg_color"])

        # 1. Solid Walls (Theme matches current stage!)
        pygame.draw.rect(screen, current_stage["border_glow"], (0, 0, WIDTH, HEIGHT), BORDER_THICKNESS)
        pygame.draw.rect(
            screen,
            current_stage["border_color"],
            (4, 4, WIDTH - 8, HEIGHT - 8),
            BORDER_THICKNESS - 8,
        )

        # 2. Draw Food Variety
        for ax, ay in food_items["apple"]:
            pygame.draw.circle(screen, FOOD_TYPES["apple"]["color"], (ax + GRID_SIZE // 2, ay + GRID_SIZE // 2), GRID_SIZE // 2 - 2)
            pygame.draw.circle(screen, (101, 163, 13), (ax + GRID_SIZE // 2 + 3, ay + 4), 3)

        for bx, by in food_items["berry"]:
            pygame.draw.circle(screen, (168, 85, 247), (bx + GRID_SIZE // 2, by + GRID_SIZE // 2), GRID_SIZE // 2 - 2)
            pygame.draw.circle(screen, (232, 121, 249), (bx + GRID_SIZE // 2 - 2, by + GRID_SIZE // 2 - 2), 3)
            pygame.draw.circle(screen, (56, 189, 248), (bx + GRID_SIZE // 2, by + 4), 2)

        for gx, gy in food_items["golden_apple"]:
            pygame.draw.circle(screen, (253, 224, 71), (gx + GRID_SIZE // 2, gy + GRID_SIZE // 2), GRID_SIZE // 2)
            pygame.draw.circle(screen, (250, 204, 21), (gx + GRID_SIZE // 2, gy + GRID_SIZE // 2), GRID_SIZE // 2 - 2)
            pygame.draw.circle(screen, (255, 255, 255), (gx + GRID_SIZE // 2 - 3, gy + GRID_SIZE // 2 - 3), 3)
            pygame.draw.circle(screen, (16, 185, 129), (gx + GRID_SIZE // 2 + 3, gy + 4), 3)

        for wx, wy in food_items["watermelon"]:
            pygame.draw.rect(screen, (34, 197, 94), (wx + 2, wy + 4, GRID_SIZE - 4, GRID_SIZE - 6), border_radius=6)
            pygame.draw.rect(screen, (251, 113, 133), (wx + 4, wy + 6, GRID_SIZE - 8, GRID_SIZE - 10), border_radius=4)
            pygame.draw.circle(screen, (15, 23, 42), (wx + 9, wy + 11), 1)
            pygame.draw.circle(screen, (15, 23, 42), (wx + 15, wy + 11), 1)

        for dx, dy in food_items["diamond"]:
            pts = [
                (dx + GRID_SIZE // 2, dy + 2),
                (dx + GRID_SIZE - 2, dy + GRID_SIZE // 2),
                (dx + GRID_SIZE // 2, dy + GRID_SIZE - 2),
                (dx + 2, dy + GRID_SIZE // 2),
            ]
            pygame.draw.polygon(screen, (34, 211, 238), pts)
            pygame.draw.circle(screen, (255, 255, 255), (dx + GRID_SIZE // 2, dy + GRID_SIZE // 2), 4)

        # 3. Draw Mythic Oranges (10,000 Credits!)
        for ox, oy in oranges:
            pygame.draw.circle(screen, (251, 146, 60), (ox + GRID_SIZE // 2, oy + GRID_SIZE // 2), GRID_SIZE // 2 + 2)
            pygame.draw.circle(screen, (249, 115, 22), (ox + GRID_SIZE // 2, oy + GRID_SIZE // 2), GRID_SIZE // 2 - 1)
            pygame.draw.circle(screen, (254, 215, 170), (ox + GRID_SIZE // 2 - 3, oy + GRID_SIZE // 2 - 3), 4)
            pygame.draw.circle(screen, (34, 197, 94), (ox + GRID_SIZE // 2 + 4, oy + 3), 3)

        # 4. Draw Player Snake — Scales with Growth Level
        theme_idx = min(growth_level - 1, len(LEVEL_THEMES) - 1)
        theme = LEVEL_THEMES[theme_idx]
        pad = max(-7, 2 - (growth_level - 1) * 1)

        for index, (sx, sy) in enumerate(snake):
            draw_x = sx + pad
            draw_y = sy + pad
            draw_w = GRID_SIZE - (2 * pad)
            draw_h = GRID_SIZE - (2 * pad)

            if index == 0:
                if growth_level >= 3:
                    aura_col = (250, 204, 21) if growth_level < 6 else ((244, 63, 94) if growth_level < 9 else (251, 146, 60))
                    pygame.draw.rect(
                        screen,
                        aura_col,
                        (draw_x - 3, draw_y - 3, draw_w + 6, draw_h + 6),
                        border_radius=10,
                    )

                pygame.draw.rect(
                    screen,
                    theme["head"],
                    (draw_x, draw_y, draw_w, draw_h),
                    border_radius=8,
                )

                eye_r = min(5, 3 + (growth_level // 3))
                if change_x > 0:
                    e1 = (sx + GRID_SIZE - 6, sy + 6)
                    e2 = (sx + GRID_SIZE - 6, sy + GRID_SIZE - 6)
                elif change_x < 0:
                    e1 = (sx + 6, sy + 6)
                    e2 = (sx + 6, sy + GRID_SIZE - 6)
                elif change_y < 0:
                    e1 = (sx + 6, sy + 6)
                    e2 = (sx + GRID_SIZE - 6, sy + 6)
                else:
                    e1 = (sx + 6, sy + GRID_SIZE - 6)
                    e2 = (sx + GRID_SIZE - 6, sy + GRID_SIZE - 6)

                pygame.draw.circle(screen, (15, 23, 42), e1, eye_r)
                pygame.draw.circle(screen, (15, 23, 42), e2, eye_r)
            else:
                pygame.draw.rect(
                    screen,
                    theme["body"],
                    (draw_x, draw_y, draw_w, draw_h),
                    border_radius=6,
                )

        # 5. HUD / Dashboard
        if not game_over and not game_won:
            time_alive = current_time - game_start_time
            time_until_next = max(0, (growth_level * 10000 - time_alive))
            seconds_left = math.ceil(time_until_next / 1000)
        else:
            seconds_left = 0

        stage_target = current_stage["target_credits"]
        stage_title = f"STAGE {current_stage_idx + 1}/3: {current_stage['name']}"

        stage_surf = font_medium.render(stage_title, True, current_stage["border_color"])
        cred_surf = font_medium.render(f"🪙 CREDITS: {credits:,} / {stage_target:,}", True, (250, 204, 21))
        size_surf = font_medium.render(f"⭐ SIZE: Lv {growth_level} ({theme['name']})", True, (34, 211, 238))
        orange_timer_surf = font_medium.render(f"⏳ NEXT ORANGE: {seconds_left}s", True, (253, 224, 71))
        score_surf = font_small.render(f"SCORE: {score:,}", True, (248, 250, 252))

        screen.blit(stage_surf, (BORDER_THICKNESS + 15, BORDER_THICKNESS + 8))
        screen.blit(cred_surf, (BORDER_THICKNESS + 450, BORDER_THICKNESS + 8))
        screen.blit(size_surf, (BORDER_THICKNESS + 820, BORDER_THICKNESS + 8))
        screen.blit(orange_timer_surf, (WIDTH - BORDER_THICKNESS - 230, BORDER_THICKNESS + 8))

        # 6. Banner Notification
        if banner_timer > 0:
            banner_timer -= 1
            banner_surf = font_large.render(banner_text, True, (250, 204, 21))
            screen.blit(
                banner_surf,
                banner_surf.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 160)),
            )

        # 7. GRAND VICTORY SCREEN (Reached 50,000 Credits on Final Stage 3!)
        if game_won:
            overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
            overlay.fill((10, 25, 47, 220))
            screen.blit(overlay, (0, 0))

            win_title = font_xl.render("🏆 YOU WIN! THE GAME HAS FINISHED! 🏆", True, (250, 204, 21))
            screen.blit(win_title, win_title.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 130)))

            congrats_text = font_large.render("👑 GRAND CHAMPION — ALL 3 LEVELS CONQUERED! 👑", True, (74, 222, 128))
            screen.blit(congrats_text, congrats_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 55)))

            stages_cleared = font_medium.render("Stage 1 (25,000 CR) ✅   Stage 2 (40,000 CR) ✅   Final Level 3 (50,000 CR) ✅", True, (34, 211, 238))
            screen.blit(stages_cleared, stages_cleared.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 10)))

            cred_text = font_large.render(f"Final Credits: {credits:,}   |   Final Score: {score:,}", True, (250, 204, 21))
            screen.blit(cred_text, cred_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 65)))

            replay_text = font_medium.render("Press SPACEBAR to Play Campaign Again or ESC to Quit", True, (248, 250, 252))
            screen.blit(replay_text, replay_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 130)))

        # 8. Game Over Screen
        elif game_over:
            overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
            overlay.fill((0, 0, 0, 195))
            screen.blit(overlay, (0, 0))

            go_text = font_xl.render("💥 GAME OVER 💥", True, (239, 68, 68))
            screen.blit(
                go_text,
                go_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 90)),
            )

            stats_text = font_large.render(
                f"Credits: {credits:,} / {stage_target:,}   |   Failed on {current_stage['name']}",
                True,
                (250, 204, 21),
            )
            screen.blit(
                stats_text,
                stats_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 15)),
            )

            final_text = font_medium.render(f"Final Score: {score:,}   |   Best: {high_score:,}", True, (248, 250, 252))
            screen.blit(
                final_text,
                final_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 45)),
            )

            replay_text = font_medium.render(
                "Press SPACEBAR to Try Again or ESC to Quit",
                True,
                (34, 211, 238),
            )
            screen.blit(
                replay_text,
                replay_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 105)),
            )

        pygame.display.flip()
        current_speed = min(15, 8 + (growth_level - 1) * 0.4)
        clock.tick(current_speed)

    pygame.quit()


if __name__ == "__main__":
    main()
