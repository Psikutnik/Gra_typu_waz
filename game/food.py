import random


class Food:
    def __init__(self, grid_width, grid_height, block_size, snake_body):
        self.grid_width = grid_width
        self.grid_height = grid_height
        self.block_size = block_size
        self.position = (0, 0)
        self.spawn(snake_body)

    def spawn(self, snake_body):
        available_positions = [
            (x, y) for x in range(self.grid_width)
            for y in range(self.grid_height)
            if (x, y) not in snake_body
        ]

        if available_positions:
            self.position = random.choice(available_positions)
        else:
            self.position = (-1, -1)  # No available positions