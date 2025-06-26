import pygame
import sys
import json
from .snake import Snake
from .food import Food
from .high_scores import HighScores
from game.utils.helpers import draw_text



class Game:
    def __init__(self, screen, block_size, colors, fps):
        self.screen = screen
        self.block_size = block_size
        self.colors = colors
        self.fps = fps
        self.clock = pygame.time.Clock()
        self.width, self.height = screen.get_size()
        self.grid_width = self.width // block_size
        self.grid_height = self.height // block_size
        self.snake = Snake(self.grid_width, self.grid_height, block_size)
        self.food = Food(self.grid_width, self.grid_height, block_size, self.snake.body)
        self.score = 0
        self.game_over = False
        self.paused = False
        self.high_scores = HighScores('data/scores.json')

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.paused = not self.paused
                elif event.key == pygame.K_r and self.game_over:
                    self.reset()
                elif not self.game_over and not self.paused:
                    if event.key == pygame.K_UP and self.snake.direction != 'DOWN':
                        self.snake.direction = 'UP'
                    elif event.key == pygame.K_DOWN and self.snake.direction != 'UP':
                        self.snake.direction = 'DOWN'
                    elif event.key == pygame.K_LEFT and self.snake.direction != 'RIGHT':
                        self.snake.direction = 'LEFT'
                    elif event.key == pygame.K_RIGHT and self.snake.direction != 'LEFT':
                        self.snake.direction = 'RIGHT'

    def update(self):
        if self.game_over or self.paused:
            return

        self.snake.move()

        # Check collision with food
        if self.snake.body[0] == self.food.position:
            self.snake.grow()
            self.score += 10
            self.food.spawn(self.snake.body)

            # Increase speed every 50 points
            if self.score % 50 == 0:
                self.fps += 2

        # Check collision with walls or self
        if (self.snake.check_collision() or
                self.snake.body[0][0] < 0 or
                self.snake.body[0][0] >= self.grid_width or
                self.snake.body[0][1] < 0 or
                self.snake.body[0][1] >= self.grid_height):
            self.game_over = True
            self.high_scores.add_score(self.score)

    def draw(self):
        self.screen.fill(self.colors['background'])

        # Draw snake
        for segment in self.snake.body:
            pygame.draw.rect(
                self.screen,
                self.colors['snake'],
                (segment[0] * self.block_size, segment[1] * self.block_size,
                 self.block_size, self.block_size)
            )

        # Draw food
        pygame.draw.rect(
            self.screen,
            self.colors['food'],
            (self.food.position[0] * self.block_size, self.food.position[1] * self.block_size,
             self.block_size, self.block_size)
        )

        # Draw score
        draw_text(
            self.screen,
            f"Score: {self.score}",
            self.colors['text'],
            20,
            (10, 10)
        )

        # Draw high score
        draw_text(
            self.screen,
            f"High Score: {self.high_scores.get_highest_score()}",
            self.colors['text'],
            20,
            (10, 40)
        )

        if self.paused:
            draw_text(
                self.screen,
                "PAUSED - Press ESC to continue",
                self.colors['text'],
                36,
                (self.width // 2 - 180, self.height // 2 - 18)
            )

        if self.game_over:
            draw_text(
                self.screen,
                "GAME OVER - Press R to restart",
                self.colors['text'],
                36,
                (self.width // 2 - 180, self.height // 2 - 18)
            )

        pygame.display.flip()

    def reset(self):
        self.snake = Snake(self.grid_width, self.grid_height, self.block_size)
        self.food = Food(self.grid_width, self.grid_height, self.block_size, self.snake.body)
        self.score = 0
        self.game_over = False
        self.fps = 10

    def run(self):
        while True:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(self.fps)