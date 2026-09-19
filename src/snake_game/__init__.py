import math
import random
import pygame


def main() -> None:
    pygame.init()
    pygame.font.init()

    # --- Screen Setup ---
    WIDTH = 1000
    HEIGHT = 1000
    GRID_SIZE = 25
    BORDER_THICKNESS = 25

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Connor's Snake: Bot Hunter 🤖🐍")
    clock = pygame.time.Clock()

    # --- Fonts ---
    font_xl = pygame.font.SysFont("comicsansms", 56, bold=True)
    font_large = pygame.font.SysFont("comicsansms", 40, bold=True)
    font_medium = pygame.font.SysFont("comicsansms", 26, bold=True)
    font_small = pygame.font.SysFont("comicsansms", 20, bold=True)

    # --- Colors ---
    BG_COLOR = (15, 23, 42)          # Deep Space Navy
    BORDER_COLOR = (239, 68, 68)     # Danger Red Border
    BORDER_GLOW = (185, 28, 28)
    FOOD_COLOR = (244, 63, 94)       # Apple Red
    FOOD_STEM = (101, 163, 13)
    CREDIT_COLOR = (250, 204, 21)    # Shiny Gold
    CREDIT_CORE = (254, 240, 138)
    TEXT_COLOR = (248, 250, 252)
    CYAN = (34, 211, 238)
    PURPLE = (168, 85, 247)
    ORANGE = (251, 146, 60)

    # Evolution Tiers
    TIERS = [
        {"name": "Baby Viper", "credits_needed": 0, "color_head": (74, 222, 128), "color_body": (34, 197, 94), "pad": 2},
        {"name": "Cobra Striker", "credits_needed": 60, "color_head": (56, 189, 248), "color_body": (14, 165, 233), "pad": 0},
        {"name": "Titan Python", "credits_needed": 150, "color_head": (250, 204, 21), "color_body": (234, 179, 8), "pad": -2},
        {"name": "Apex Dragon", "credits_needed": 300, "color_head": (244, 63, 94), "color_body": (225, 29, 72), "pad": -4},
    ]

    BOT_COLORS = [
        {"name": "Cyber-Red", "head": (248, 113, 113), "body": (220, 38, 38)},
        {"name": "Shadow-Purple", "head": (192, 132, 252), "body": (147, 51, 234)},
        {"name": "Rust-Orange", "head": (251, 146, 60), "body": (234, 88, 12)},
    ]

    DIRECTIONS = [
        (GRID_SIZE, 0),
        (-GRID_SIZE, 0),
        (0, GRID_SIZE),
        (0, -GRID_SIZE),
    ]

    def is_inside_arena(pos: tuple[int, int]) -> bool:
        x, y = pos
        return (
            BORDER_THICKNESS <= x < WIDTH - BORDER_THICKNESS
            and BORDER_THICKNESS <= y < HEIGHT - BORDER_THICKNESS
        )

    def spawn_random_cell(occupied: set[tuple[int, int]]) -> tuple[int, int]:
        min_cell = BORDER_THICKNESS // GRID_SIZE
        max_cell_x = (WIDTH - BORDER_THICKNESS) // GRID_SIZE - 1
        max_cell_y = (HEIGHT - BORDER_THICKNESS) // GRID_SIZE - 1
        for _ in range(200):
            x = random.randint(min_cell, max_cell_x) * GRID_SIZE
            y = random.randint(min_cell, max_cell_y) * GRID_SIZE
            if (x, y) not in occupied:
                return (x, y)
        return (WIDTH // 2, HEIGHT // 2)

    class Bot:
        def __init__(self, bot_id: int, occupied: set[tuple[int, int]]):
            self.bot_id = bot_id
            self.info = BOT_COLORS[bot_id % len(BOT_COLORS)]
            self.respawn(occupied)

        def respawn(self, occupied: set[tuple[int, int]]):
            pos = spawn_random_cell(occupied)
            self.body = [pos, (pos[0] - GRID_SIZE, pos[1]), (pos[0] - 2 * GRID_SIZE, pos[1])]
            self.dir = random.choice(DIRECTIONS)
            self.alive = True
            self.respawn_timer = 0

        def update(self, player_snake: list[tuple[int, int]], other_bots: list["Bot"]):
            if not self.alive:
                self.respawn_timer -= 1
                if self.respawn_timer <= 0:
                    occupied = set(player_snake)
                    for b in other_bots:
                        if b.alive:
                            occupied.update(b.body)
                    self.respawn(occupied)
                return

            head_x, head_y = self.body[0]
            current_dir = self.dir

            # AI: Pick safe directions
            valid_dirs = []
            danger_cells = set(player_snake)
            for b in other_bots:
                if b != self and b.alive:
                    danger_cells.update(b.body)

            for d in DIRECTIONS:
                # Can't 180 directly
                if d[0] == -current_dir[0] and d[1] == -current_dir[1]:
                    continue
                next_pos = (head_x + d[0], head_y + d[1])
                if is_inside_arena(next_pos) and next_pos not in danger_cells and next_pos not in self.body:
                    valid_dirs.append(d)

            if valid_dirs:
                # 70% chance to continue same direction if safe
                if current_dir in valid_dirs and random.random() < 0.70:
                    self.dir = current_dir
                else:
                    self.dir = random.choice(valid_dirs)
            else:
                # Trapped! Keep current dir
                pass

            new_head = (head_x + self.dir[0], head_y + self.dir[1])
            self.body.insert(0, new_head)
            self.body.pop()

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
        kills = 0
        game_over = False
        banner_text = ""
        banner_timer = 0

        occupied = set(snake)
        food = spawn_random_cell(occupied)
        occupied.add(food)

        bots = [Bot(0, occupied), Bot(1, occupied), Bot(2, occupied)]
        credit_orbs: list[tuple[int, int]] = []

        return (
            snake,
            change_x,
            change_y,
            food,
            score,
            credits,
            tier_index,
            kills,
            game_over,
            banner_text,
            banner_timer,
            bots,
            credit_orbs,
        )

    (
        snake,
        change_x,
        change_y,
        food,
        score,
        credits,
        tier_index,
        kills,
        game_over,
        banner_text,
        banner_timer,
        bots,
        credit_orbs,
    ) = reset_game()

    high_score = 0
    running = True

    while running:
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
                            food,
                            score,
                            credits,
                            tier_index,
                            kills,
                            game_over,
                            banner_text,
                            banner_timer,
                            bots,
                            credit_orbs,
                        ) = reset_game()
                    elif event.key == pygame.K_ESCAPE:
                        running = False
                else:
                    # Arrow keys & WASD
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
            # 1. Move Player
            head_x, head_y = snake[0]
            new_head = (head_x + change_x, head_y + change_y)

            # Check Wall Crash
            if not is_inside_arena(new_head):
                game_over = True

            # Check Self Crash
            if new_head in snake:
                game_over = True

            # 2. Check Collision With Bot Bodies
            for bot in bots:
                if bot.alive:
                    if new_head in bot.body[1:]:
                        # Player hit bot body -> Crash!
                        game_over = True
                    elif new_head == bot.body[0]:
                        # Head-to-Head Clash! Player wins if equal/larger tier
                        bot.alive = False
                        bot.respawn_timer = 50
                        kills += 1
                        score += 50
                        banner_text = f"💥 HEAD-ON CRUSH! {bot.info['name']} ELIMINATED! 💥"
                        banner_timer = 30
                        # Drop credits where bot was
                        for bp in bot.body:
                            credit_orbs.append(bp)

            if not game_over:
                snake.insert(0, new_head)

                # Eat Normal Food
                if new_head == food:
                    score += 10
                    occupied = set(snake)
                    for b in bots:
                        if b.alive:
                            occupied.update(b.body)
                    food = spawn_random_cell(occupied)
                else:
                    snake.pop()

                # Collect Credit Orbs
                remaining_orbs = []
                for orb in credit_orbs:
                    if new_head == orb:
                        credits += 20
                        score += 30
                        banner_text = "🪙 +20 CREDITS! 🪙"
                        banner_timer = 15
                    else:
                        remaining_orbs.append(orb)
                credit_orbs = remaining_orbs

                # Check Evolution Level Up
                if tier_index + 1 < len(TIERS):
                    next_tier = TIERS[tier_index + 1]
                    if credits >= next_tier["credits_needed"]:
                        tier_index += 1
                        # Grow 4 extra segments as bonus
                        for _ in range(4):
                            snake.append(snake[-1])
                        banner_text = f"⭐ EVOLVED TO {TIERS[tier_index]['name'].upper()}! ⭐"
                        banner_timer = 40

                if score > high_score:
                    high_score = score

            # 3. Update Bots
            for bot in bots:
                bot.update(snake, bots)

                # Check if Bot Crashed Into Player Body (Player kills bot!)
                if bot.alive:
                    bot_head = bot.body[0]
                    # Did bot crash into player's body or out of bounds?
                    if bot_head in snake[1:] or not is_inside_arena(bot_head):
                        bot.alive = False
                        bot.respawn_timer = 45
                        kills += 1
                        score += 100
                        banner_text = f"⚔️ BOT TRAPPED! {bot.info['name']} KILLED! 🪙"
                        banner_timer = 35
                        # Drop glowing credits from bot's body!
                        for bp in bot.body:
                            if is_inside_arena(bp):
                                credit_orbs.append(bp)

        # --- Drawing ---
        screen.fill(BG_COLOR)

        # 1. Danger Walls
        pygame.draw.rect(screen, BORDER_GLOW, (0, 0, WIDTH, HEIGHT), BORDER_THICKNESS)
        pygame.draw.rect(
            screen,
            BORDER_COLOR,
            (4, 4, WIDTH - 8, HEIGHT - 8),
            BORDER_THICKNESS - 8,
        )

        # 2. Draw Credit Orbs (Glowing Coins)
        for orb_x, orb_y in credit_orbs:
            # Outer Gold Glow
            pygame.draw.circle(
                screen,
                CREDIT_COLOR,
                (orb_x + GRID_SIZE // 2, orb_y + GRID_SIZE // 2),
                GRID_SIZE // 2,
            )
            # Inner bright spark
            pygame.draw.circle(
                screen,
                CREDIT_CORE,
                (orb_x + GRID_SIZE // 2, orb_y + GRID_SIZE // 2),
                GRID_SIZE // 4,
            )

        # 3. Draw Food (Apple)
        fx, fy = food
        pygame.draw.circle(
            screen,
            FOOD_COLOR,
            (fx + GRID_SIZE // 2, fy + GRID_SIZE // 2),
            GRID_SIZE // 2 - 2,
        )
        pygame.draw.circle(
            screen,
            FOOD_STEM,
            (fx + GRID_SIZE // 2 + 3, fy + 4),
            3,
        )

        # 4. Draw Bots
        for bot in bots:
            if bot.alive:
                for b_idx, (bx, by) in enumerate(bot.body):
                    b_color = bot.info["head"] if b_idx == 0 else bot.info["body"]
                    pygame.draw.rect(
                        screen,
                        b_color,
                        (bx + 2, by + 2, GRID_SIZE - 4, GRID_SIZE - 4),
                        border_radius=5,
                    )
                    # Bot evil eyes
                    if b_idx == 0:
                        pygame.draw.circle(screen, (255, 255, 255), (bx + 8, by + 8), 3)
                        pygame.draw.circle(screen, (255, 255, 255), (bx + GRID_SIZE - 8, by + 8), 3)
                        pygame.draw.circle(screen, (0, 0, 0), (bx + 8, by + 8), 1)
                        pygame.draw.circle(screen, (0, 0, 0), (bx + GRID_SIZE - 8, by + 8), 1)

        # 5. Draw Player Snake (Grows visually chunkier by tier!)
        current_tier = TIERS[tier_index]
        pad = current_tier["pad"]  # Negative pad means it bulges BIGGER than grid cell!
        for index, (sx, sy) in enumerate(snake):
            draw_x = sx + pad
            draw_y = sy + pad
            draw_w = GRID_SIZE - (2 * pad)
            draw_h = GRID_SIZE - (2 * pad)

            if index == 0:
                # Head with glowing evolution outline
                if tier_index >= 2:
                    # Aura
                    pygame.draw.rect(
                        screen,
                        GOLD,
                        (draw_x - 3, draw_y - 3, draw_w + 6, draw_h + 6),
                        border_radius=8,
                    )

                pygame.draw.rect(
                    screen,
                    current_tier["color_head"],
                    (draw_x, draw_y, draw_w, draw_h),
                    border_radius=8,
                )

                # Eyes
                eye_r = 4 if tier_index >= 2 else 3
                if change_x > 0:
                    eye1 = (sx + GRID_SIZE - 6, sy + 6)
                    eye2 = (sx + GRID_SIZE - 6, sy + GRID_SIZE - 6)
                elif change_x < 0:
                    eye1 = (sx + 6, sy + 6)
                    eye2 = (sx + 6, sy + GRID_SIZE - 6)
                elif change_y < 0:
                    eye1 = (sx + 6, sy + 6)
                    eye2 = (sx + GRID_SIZE - 6, sy + 6)
                else:
                    eye1 = (sx + 6, sy + GRID_SIZE - 6)
                    eye2 = (sx + GRID_SIZE - 6, sy + GRID_SIZE - 6)

                pygame.draw.circle(screen, (15, 23, 42), eye1, eye_r)
                pygame.draw.circle(screen, (15, 23, 42), eye2, eye_r)
            else:
                pygame.draw.rect(
                    screen,
                    current_tier["color_body"],
                    (draw_x, draw_y, draw_w, draw_h),
                    border_radius=6,
                )

        # 6. HUD / Dashboard
        tier_name = current_tier["name"]
        score_surf = font_small.render(f"SCORE: {score}", True, TEXT_COLOR)
        cred_surf = font_small.render(f"🪙 CREDITS: {credits}", True, GOLD)
        kill_surf = font_small.render(f"⚔️ KILLS: {kills}", True, (244, 63, 94))
        tier_surf = font_small.render(f"⭐ {tier_name.upper()} (T{tier_index + 1})", True, CYAN)

        screen.blit(score_surf, (BORDER_THICKNESS + 15, BORDER_THICKNESS + 8))
        screen.blit(cred_surf, (BORDER_THICKNESS + 180, BORDER_THICKNESS + 8))
        screen.blit(kill_surf, (BORDER_THICKNESS + 400, BORDER_THICKNESS + 8))
        screen.blit(tier_surf, (WIDTH - BORDER_THICKNESS - 300, BORDER_THICKNESS + 8))

        # 7. Action Banner Notification
        if banner_timer > 0:
            banner_timer -= 1
            banner_surf = font_medium.render(banner_text, True, GOLD)
            screen.blit(
                banner_surf,
                banner_surf.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 140)),
            )

        # 8. Game Over Screen
        if game_over:
            overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
            overlay.fill((0, 0, 0, 195))
            screen.blit(overlay, (0, 0))

            go_text = font_xl.render("💥 MISSION FAILED 💥", True, BORDER_COLOR)
            screen.blit(
                go_text,
                go_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 90)),
            )

            stats_text = font_medium.render(
                f"Kills: {kills}   Credits: {credits}   Tier: {tier_name}",
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
                final_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 40)),
            )

            replay_text = font_small.render(
                "Press SPACEBAR to Hunt Again or ESC to Quit",
                True,
                CYAN,
            )
            screen.blit(
                replay_text,
                replay_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 105)),
            )

        pygame.display.flip()

        # Snake game ticks at comfortable 8 FPS
        clock.tick(8 + tier_index * 1.0)

    pygame.quit()


if __name__ == "__main__":
    main()
