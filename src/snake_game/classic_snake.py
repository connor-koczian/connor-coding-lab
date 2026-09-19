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
    pygame.display.set_caption("Connor's Arcade Snake 🐍")
    clock = pygame.time.Clock()

    # --- Fonts ---
    font_large = pygame.font.SysFont("comicsansms", 64, bold=True)
    font_medium = pygame.font.SysFont("comicsansms", 36, bold=True)
    font_small = pygame.font.SysFont("comicsansms", 24, bold=True)

    # --- Colors ---
    BG_COLOR = (15, 23, 42)          # Deep Midnight Blue
    BORDER_COLOR = (239, 68, 68)     # Danger Red Solid Wall
    BORDER_GLOW = (185, 28, 28)
    SNAKE_HEAD = (74, 222, 128)      # Bright Neon Green
    SNAKE_BODY = (34, 197, 94)       # Arcade Green
    SNAKE_EYES = (15, 23, 42)
    FOOD_COLOR = (244, 63, 94)       # Juicy Red Apple
    FOOD_STEM = (101, 163, 13)       # Apple Leaf Green
    TEXT_COLOR = (248, 250, 252)
    GOLD = (250, 204, 21)
    CYAN = (34, 211, 238)

    def spawn_food(snake_body: list[tuple[int, int]]) -> tuple[int, int]:
        """Spawn food at a random grid spot inside the solid walls."""
        min_cell = BORDER_THICKNESS // GRID_SIZE
        max_cell_x = (WIDTH - BORDER_THICKNESS) // GRID_SIZE - 1
        max_cell_y = (HEIGHT - BORDER_THICKNESS) // GRID_SIZE - 1
        while True:
            fx = random.randint(min_cell, max_cell_x) * GRID_SIZE
            fy = random.randint(min_cell, max_cell_y) * GRID_SIZE
            if (fx, fy) not in snake_body:
                return (fx, fy)

    def reset_game():
        """Reset the game to starting state."""
        start_x = (WIDTH // 2 // GRID_SIZE) * GRID_SIZE
        start_y = (HEIGHT // 2 // GRID_SIZE) * GRID_SIZE
        snake = [
            (start_x, start_y),
            (start_x - GRID_SIZE, start_y),
            (start_x - (2 * GRID_SIZE), start_y),
        ]
        change_x = GRID_SIZE
        change_y = 0
        food = spawn_food(snake)
        score = 0
        level = 1
        game_over = False
        level_up_timer = 0
        return snake, change_x, change_y, food, score, level, game_over, level_up_timer

    snake, change_x, change_y, food, score, level, game_over, level_up_timer = reset_game()
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
                        snake, change_x, change_y, food, score, level, game_over, level_up_timer = reset_game()
                    elif event.key == pygame.K_ESCAPE:
                        running = False
                else:
                    # Arrow keys & WASD controls (no instant 180° into self)
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

        # --- Game Logic (Only runs when alive) ---
        if not game_over:
            head_x, head_y = snake[0]
            new_head = (head_x + change_x, head_y + change_y)

            # 1. Solid Wall Collision Check
            wall_left = BORDER_THICKNESS
            wall_right = WIDTH - BORDER_THICKNESS
            wall_top = BORDER_THICKNESS
            wall_bottom = HEIGHT - BORDER_THICKNESS

            if (
                new_head[0] < wall_left
                or new_head[0] >= wall_right
                or new_head[1] < wall_top
                or new_head[1] >= wall_bottom
            ):
                game_over = True

            # 2. Self Collision Check
            if new_head in snake:
                game_over = True

            if not game_over:
                snake.insert(0, new_head)

                # 3. Eat Food Check
                if new_head == food:
                    score += 10
                    if score > high_score:
                        high_score = score

                    # Level Up every 5 apples (50 points)!
                    new_level = 1 + (score // 50)
                    if new_level > level:
                        level = new_level
                        level_up_timer = 20  # Flash "LEVEL UP!" for ~20 frames

                    food = spawn_food(snake)
                else:
                    snake.pop()

        # --- Drawing the Arena ---
        screen.fill(BG_COLOR)

        # 1. Draw Solid Danger Walls
        pygame.draw.rect(screen, BORDER_GLOW, (0, 0, WIDTH, HEIGHT), BORDER_THICKNESS)
        pygame.draw.rect(
            screen,
            BORDER_COLOR,
            (4, 4, WIDTH - 8, HEIGHT - 8),
            BORDER_THICKNESS - 8,
        )

        # 2. Draw Food (Apple + Stem)
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

        # 3. Draw Snake Body & Head
        for index, (bx, by) in enumerate(snake):
            if index == 0:
                # Head
                pygame.draw.rect(
                    screen,
                    SNAKE_HEAD,
                    (bx + 1, by + 1, GRID_SIZE - 2, GRID_SIZE - 2),
                    border_radius=6,
                )
                # Snake eyes
                eye_radius = 3
                if change_x > 0:
                    eye1 = (bx + GRID_SIZE - 6, by + 6)
                    eye2 = (bx + GRID_SIZE - 6, by + GRID_SIZE - 6)
                elif change_x < 0:
                    eye1 = (bx + 6, by + 6)
                    eye2 = (bx + 6, by + GRID_SIZE - 6)
                elif change_y < 0:
                    eye1 = (bx + 6, by + 6)
                    eye2 = (bx + GRID_SIZE - 6, by + 6)
                else:
                    eye1 = (bx + 6, by + GRID_SIZE - 6)
                    eye2 = (bx + GRID_SIZE - 6, by + GRID_SIZE - 6)

                pygame.draw.circle(screen, SNAKE_EYES, eye1, eye_radius)
                pygame.draw.circle(screen, SNAKE_EYES, eye2, eye_radius)
            else:
                # Body segment
                pygame.draw.rect(
                    screen,
                    SNAKE_BODY,
                    (bx + 1, by + 1, GRID_SIZE - 2, GRID_SIZE - 2),
                    border_radius=4,
                )

        # 4. HUD / Scoreboard (Top Bar)
        score_surf = font_small.render(f"SCORE: {score}", True, TEXT_COLOR)
        level_surf = font_small.render(f"⭐ LEVEL: {level}", True, CYAN)
        high_surf = font_small.render(f"🏆 HIGH SCORE: {high_score}", True, GOLD)

        screen.blit(score_surf, (BORDER_THICKNESS + 15, BORDER_THICKNESS + 10))
        screen.blit(level_surf, (WIDTH // 2 - 70, BORDER_THICKNESS + 10))
        screen.blit(high_surf, (WIDTH - BORDER_THICKNESS - 240, BORDER_THICKNESS + 10))

        # 5. Flashy "LEVEL UP!" Pop-up Notification
        if level_up_timer > 0:
            level_up_timer -= 1
            lvl_text = font_medium.render(f"⚡ LEVEL {level}! SPEED BOOST! ⚡", True, GOLD)
            screen.blit(
                lvl_text,
                lvl_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 120)),
            )

        # 6. Game Over Screen
        if game_over:
            overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
            overlay.fill((0, 0, 0, 180))
            screen.blit(overlay, (0, 0))

            go_text = font_large.render("💥 GAME OVER 💥", True, BORDER_COLOR)
            screen.blit(
                go_text,
                go_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 70)),
            )

            final_text = font_medium.render(f"Final Score: {score}  |  Reached Level {level}", True, GOLD)
            screen.blit(
                final_text,
                final_text.get_rect(center=(WIDTH // 2, HEIGHT // 2)),
            )

            replay_text = font_small.render(
                "Press SPACEBAR to Play Again or ESC to Quit",
                True,
                TEXT_COLOR,
            )
            screen.blit(
                replay_text,
                replay_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 70)),
            )

        pygame.display.flip()

        # --- Dynamic Speed: Starts chill (7 FPS) and accelerates with each level! ---
        current_speed = 7 + (level - 1) * 1.5
        clock.tick(current_speed)

    pygame.quit()


if __name__ == "__main__":
    main()
