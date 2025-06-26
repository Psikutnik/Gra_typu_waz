import pygame
from game.game import Game
from game.utils.visualizer import plot_scores
import json


def load_config():
    try:
        with open('config.json', 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {
            "width": 800,
            "height": 600,
            "fps": 10,
            "block_size": 20,
            "colors": {
                "background": (0, 55, 50),
                "snake": (0, 255, 0),
                "food": (255, 0, 0),
                "text": (255, 255, 255)
            }
        }


def main():
    config = load_config()
    pygame.init()

    screen = pygame.display.set_mode((config['width'], config['height']))
    pygame.display.set_caption('Snake Game')
    clock = pygame.time.Clock()

    game = Game(
        screen=screen,
        block_size=config['block_size'],
        colors=config['colors'],
        fps=config['fps']
    )

    try:
        game.run()
    finally:
        pygame.quit()
        plot_scores(game.high_scores.get_scores())


if __name__ == "__main__":
    main()