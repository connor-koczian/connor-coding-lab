import math
import random
import pygame


def main() -> None:
    pygame.init()
    pygame.font.init()

    # --- Screen Setup (Expanded Giant Arena) ---
    WIDTH = 1400
    HEIGHT = 950
    GRID_SIZE = 25
    BORDER_THICKNESS = 25

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Connor's Snake: Single Player Fruit Kingdom 🍎✨🍉")
    clock = pygame.time.Clock()

    # --- Fonts ---
    font_xl = pygame.font.SysFont("comicsansms", 60, bold=True)
    font_large = pygame.font.SysFont("comicsansms", 38, bold=True)
    font_medium = pygame.font.SysFont("comicsansms", 24, bold=True)
    font_small = pygame.font.SysFont("comicsansms", 18, bold=True)

    # --- Color Palette ---
    BG_COLOR = (15, 23, 42)          # Cosmic Navy
    BORDER_COLOR = (239, 68, 68)     # Danger Red Border
    BORDER_GLOW = (185, 28, 28)
    TEXT_COLOR = (248, 250, 252)
    GOLD = (250, 204, 21)
    CYAN = (34, 211, 238)
    PURPLE = (192, 132, 252)
    MELON_PINK = (251, 113, 133)
    MELON_RIND = (34, 197, 94)

    # Food Definitions: (name, credits, score, growth, spawn_interval_ms, max_count)
    FOOD_TYPES = {
        "apple": {
            "name": "Red Apple",
            "credits": 5,
            "score": 10,
            "growth": 1,
            "interval": 1500,       # Every 1.5s
            "max": 18,
            "color": (244, 63, 94),
        },
        "golden_apple": {
            "name": "Golden Apple",
            "credits": 20,
            "score": 50,
            "growth": 2,
            "interval": 5000,       # Every 5s
            "max": 6,
            "color": (250, 204, 21),
        },
        "berry": {
            "name": "Cosmic Berry",
            "credits": 15,
            "score": 35,
            "growth": 1,
            "interval": 7000,       # Every 7s
            "max": 5,
            "color": (168, 85, 247),
        },
        "watermelon": {
            "name": "Mega Watermelon",
            "credits": 40,
            "score": 100,
            "growth": 3,
            "interval": 11000,      # Every 11s
            "max": 3,
            "color": MELON_PINK,
        },
        "diamond": {
            "name": "Diamond Star Fruit",
            "credits": 80,
            "score": 250,
            "growth": 4,
            "interval": 18000,      # Every 18s
            "max": 2,
            "color": (56, 189, 248),
        },
    }

    # Evolution Tiers (Bigger snake, thicker body, and epic armor!)
    TIERS = [
        {"name": "Baby Viper", "credits_needed": 0, "head": (74, 222, 128), "body": (34, 197, 94), "pad": 2, "speed": 8},
        {"name": "Cobra Striker", "credits_needed": 80, "head": (56, 189, 248), "body": (14, 165, 233), "pad": 0, "speed": 9},
        {"name": "Golden Python", "credits_needed": 200, "head": (250, 204, 21), "body": (234, 179, 8), "pad": -2, "speed": 10},
        {"name": "Shadow Hydra", "credits_needed": 450, "head": (192, 132, 252), "body": (147, 51, 234), "pad": -4, "speed": 11},
        {"name": "Mythic Solar Dragon", "credits_needed": 800, "head": (244, 63, 94), "body": (225, 29, 72), "pad": -6, "speed": 12},
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
        tier_index = 0
        game_over = False
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

        # Start with 5 apples + 1 golden apple
        for _ in range(5):
            pos = spawn_random_cell(occupied)
            food_items["apple"].append(pos)
            occupied.add(pos)

        pos_g = spawn_random_cell(occupied)
        food_items["golden_apple"].append(pos_g)
        occupied.add(pos_g)

        now = pygame.time.get_ticks()
        spawn_timers = {k: now for k in FOOD_TYPES}

        return (
            snake,
            change_x,
            change_y,
            score,
            credits,
            tier_index,
            game_over,
            banner_text,
            banner_timer,
            pending_growth,
            food_items,
            spawn_timers,
        )

    (
        snake,
        change_x,
        change_y,
        score,
        credits,
        tier_index,
        game_over,
        banner_text,
        banner_timer,
        pending_growth,
        food_items,
        spawn_timers,
    ) = reset_game()

    high_score = 0
    running = True

    while running:
        # --- Event Handling ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if game_over:
                    if event.key == pygame.K_SPACE:
                        (
                            snake,
                            change_x,
                            change_y,
                            score,
                            credits,
                            tier_index,
                            game_over,
                            banner_text,
                            banner_timer,
                            pending_growth,
                            food_items,
                            spawn_timers,
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
        if not game_over:
            current_time = pygame.time.get_ticks()

            # 1. Spawn Food Variety on Timers
            occupied = set(snake)
            for f_list in food_items.values():
                occupied.update(f_list)

            for f_type, f_data in FOOD_TYPES.items():
                if current_time - spawn_timers[f_type] >= f_data["interval"]:
                    spawn_timers[f_type] = current_time
                    if len(food_items[f_type]) < f_data["max"]:
                        new_f = spawn_random_cell(occupied)
                        food_items[f_type].append(new_f)
                        occupied.add(new_f)

            # 2. Move Snake Head
            head_x, head_y = snake[0]
            new_head = (head_x + change_x, head_y + change_y)

            # Wall Crash Check
            if not is_inside_arena(new_head):
                game_over = True

            # Self Crash Check
            if new_head in snake:
                game_over = True

            if not game_over:
                snake.insert(0, new_head)

                # 3. Check Eating Any Food
                eaten_type = None
                eaten_pos = None
                for f_type, f_list in food_items.items():
                    if new_head in f_list:
                        eaten_type = f_type
                        eaten_pos = new_head
                        break

                if eaten_type:
                    food_items[eaten_type].remove(eaten_pos)
                    f_info = FOOD_TYPES[eaten_type]
                    credits += f_info["credits"]
                    score += f_info["score"]
                    pending_growth += (f_info["growth"] - 1)  # -1 because insert already grew 1

                    # Banner Notification
                    if eaten_type == "diamond":
                        banner_text = f"💎 DIAMOND STAR FRUIT! +{f_info['credits']} CREDITS! 💎"
                        banner_timer = 35
                    elif eaten_type == "watermelon":
                        banner_text = f"🍉 MEGA WATERMELON! +{f_info['credits']} CREDITS! 🍉"
                        banner_timer = 25
                    elif eaten_type == "golden_apple":
                        banner_text = f"✨ GOLDEN APPLE! +{f_info['credits']} CREDITS! ✨"
                        banner_timer = 20
                    elif eaten_type == "berry":
                        banner_text = f"🍇 COSMIC BERRY! +{f_info['credits']} CREDITS! 🍇"
                        banner_timer = 18
                    else:
                        banner_text = f"🍎 RED APPLE! +{f_info['credits']} CREDITS! 🍎"
                        banner_timer = 12

                else:
                    if pending_growth > 0:
                        pending_growth -= 1
                    else:
                        snake.pop()

                # 4. Check Tier Evolution
                if tier_index + 1 < len(TIERS):
                    next_tier = TIERS[tier_index + 1]
                    if credits >= next_tier["credits_needed"]:
                        tier_index += 1
                        # Instant bonus growth on evolution
                        pending_growth += 4
                        banner_text = f"⭐ EVOLVED TO {TIERS[tier_index]['name'].upper()}! ⭐"
                        banner_timer = 45

                if score > high_score:
                    high_score = score

        # --- Drawing the World ---
        screen.fill(BG_COLOR)

        # 1. Solid Walls
        pygame.draw.rect(screen, BORDER_GLOW, (0, 0, WIDTH, HEIGHT), BORDER_THICKNESS)
        pygame.draw.rect(
            screen,
            BORDER_COLOR,
            (4, 4, WIDTH - 8, HEIGHT - 8),
            BORDER_THICKNESS - 8,
        )

        # 2. Draw Food Variety
        # Red Apples
        for ax, ay in food_items["apple"]:
            pygame.draw.circle(screen, FOOD_TYPES["apple"]["color"], (ax + GRID_SIZE // 2, ay + GRID_SIZE // 2), GRID_SIZE // 2 - 2)
            pygame.draw.circle(screen, (101, 163, 13), (ax + GRID_SIZE // 2 + 3, ay + 4), 3)

        # Cosmic Berries (Purple with Cyan core)
        for bx, by in food_items["berry"]:
            pygame.draw.circle(screen, PURPLE, (bx + GRID_SIZE // 2, by + GRID_SIZE // 2), GRID_SIZE // 2 - 2)
            pygame.draw.circle(screen, (232, 121, 249), (bx + GRID_SIZE // 2 - 2, by + GRID_SIZE // 2 - 2), 3)
            pygame.draw.circle(screen, (56, 189, 248), (bx + GRID_SIZE // 2, by + 4), 2)

        # Golden Apples (Shining Gold + sparkle)
        for gx, gy in food_items["golden_apple"]:
            pygame.draw.circle(screen, (253, 224, 71), (gx + GRID_SIZE // 2, gy + GRID_SIZE // 2), GRID_SIZE // 2)
            pygame.draw.circle(screen, GOLD, (gx + GRID_SIZE // 2, gy + GRID_SIZE // 2), GRID_SIZE // 2 - 2)
            pygame.draw.circle(screen, (255, 255, 255), (gx + GRID_SIZE // 2 - 3, gy + GRID_SIZE // 2 - 3), 3)
            pygame.draw.circle(screen, (16, 185, 129), (gx + GRID_SIZE // 2 + 3, gy + 4), 3)

        # Watermelons (Green rind arc + pink wedge)
        for wx, wy in food_items["watermelon"]:
            pygame.draw.rect(screen, MELON_RIND, (wx + 2, wy + 4, GRID_SIZE - 4, GRID_SIZE - 6), border_radius=6)
            pygame.draw.rect(screen, MELON_PINK, (wx + 4, wy + 6, GRID_SIZE - 8, GRID_SIZE - 10), border_radius=4)
            # Seeds
            pygame.draw.circle(screen, (15, 23, 42), (wx + 9, wy + 11), 1)
            pygame.draw.circle(screen, (15, 23, 42), (wx + 15, wy + 11), 1)

        # Diamond Star Fruits (Cyan Diamond + white star spark)
        for dx, dy in food_items["diamond"]:
            pts = [
                (dx + GRID_SIZE // 2, dy + 2),
                (dx + GRID_SIZE - 2, dy + GRID_SIZE // 2),
                (dx + GRID_SIZE // 2, dy + GRID_SIZE - 2),
                (dx + 2, dy + GRID_SIZE // 2),
            ]
            pygame.draw.polygon(screen, CYAN, pts)
            pygame.draw.circle(screen, (255, 255, 255), (dx + GRID_SIZE // 2, dy + GRID_SIZE // 2), 4)

        # 3. Draw Player Snake (Size scales with Tier!)
        current_tier = TIERS[tier_index]
        pad = current_tier["pad"]
        for index, (sx, sy) in enumerate(snake):
            draw_x = sx + pad
            draw_y = sy + pad
            draw_w = GRID_SIZE - (2 * pad)
            draw_h = GRID_SIZE - (2 * pad)

            if index == 0:
                # Mythic / Titan Glowing Aura
                if tier_index >= 2:
                    aura_color = GOLD if tier_index < 4 else (255, 100, 100)
                    pygame.draw.rect(
                        screen,
                        aura_color,
                        (draw_x - 3, draw_y - 3, draw_w + 6, draw_h + 6),
                        border_radius=9,
                    )

                pygame.draw.rect(
                    screen,
                    current_tier["head"],
                    (draw_x, draw_y, draw_w, draw_h),
                    border_radius=8,
                )

                # Big expressive eyes
                eye_r = 4 if tier_index >= 2 else 3
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
                    current_tier["body"],
                    (draw_x, draw_y, draw_w, draw_h),
                    border_radius=6,
                )

        # 4. HUD / Dashboard
        tier_name = current_tier["name"]
        score_surf = font_medium.render(f"SCORE: {score}", True, TEXT_COLOR)
        cred_surf = font_medium.render(f"🪙 CREDITS: {credits}", True, GOLD)
        tier_surf = font_medium.render(f"⭐ {tier_name.upper()} (T{tier_index + 1})", True, CYAN)
        high_surf = font_medium.render(f"🏆 HIGH: {high_score}", True, (250, 204, 21))

        screen.blit(score_surf, (BORDER_THICKNESS + 20, BORDER_THICKNESS + 10))
        screen.blit(cred_surf, (BORDER_THICKNESS + 250, BORDER_THICKNESS + 10))
        screen.blit(tier_surf, (BORDER_THICKNESS + 520, BORDER_THICKNESS + 10))
        screen.blit(high_surf, (WIDTH - BORDER_THICKNESS - 220, BORDER_THICKNESS + 10))

        # Progress bar to next evolution
        if tier_index + 1 < len(TIERS):
            next_tier = TIERS[tier_index + 1]
            prev_req = current_tier["credits_needed"]
            next_req = next_tier["credits_needed"]
            progress = min(1.0, max(0.0, (credits - prev_req) / (next_req - prev_req)))
            bar_w = 200
            bar_h = 10
            bar_x = BORDER_THICKNESS + 520
            bar_y = BORDER_THICKNESS + 42
            pygame.draw.rect(screen, (51, 65, 85), (bar_x, bar_y, bar_w, bar_h), border_radius=5)
            pygame.draw.rect(screen, CYAN, (bar_x, bar_y, int(bar_w * progress), bar_h), border_radius=5)
            next_label = font_small.render(f"Next: {next_tier['name']} ({credits}/{next_req} CR)", True, (148, 163, 184))
            screen.blit(next_label, (bar_x + bar_w + 10, bar_y - 4))
        else:
            max_label = font_small.render("MAX TIER REACHED!", True, GOLD)
            screen.blit(max_label, (BORDER_THICKNESS + 520, BORDER_THICKNESS + 40))

        # 5. Banner Notification
        if banner_timer > 0:
            banner_timer -= 1
            banner_surf = font_large.render(banner_text, True, GOLD)
            screen.blit(
                banner_surf,
                banner_surf.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 160)),
            )

        # 6. Game Over Screen
        if game_over:
            overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
            overlay.fill((0, 0, 0, 195))
            screen.blit(overlay, (0, 0))

            go_text = font_xl.render("💥 GAME OVER 💥", True, BORDER_COLOR)
            screen.blit(
                go_text,
                go_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 90)),
            )

            stats_text = font_large.render(
                f"Credits: {credits}   |   Tier: {tier_name}",
                True,
                GOLD,
            )
            screen.blit(
                stats_text,
                stats_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 15)),
            )

            final_text = font_medium.render(f"Final Score: {score}   |   Best: {high_score}", True, TEXT_COLOR)
            screen.blit(
                final_text,
                final_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 45)),
            )

            replay_text = font_medium.render(
                "Press SPACEBAR to Play Again or ESC to Quit",
                True,
                CYAN,
            )
            screen.blit(
                replay_text,
                replay_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 105)),
            )

        pygame.display.flip()
        clock.tick(current_tier["speed"])

    pygame.quit()


if __name__ == "__main__":
    main()
