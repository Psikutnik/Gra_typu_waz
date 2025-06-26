import random


class Snake:
    def __init__(self, grid_width, grid_height, block_size):
        self.grid_width = grid_width
        self.grid_height = grid_height
        self.block_size = block_size
        self.reset()

    def reset(self):
        start_x = self.grid_width // 2
        start_y = self.grid_height // 2
        self.body = [(start_x, start_y)]
        self.direction = random.choice(['UP', 'DOWN', 'LEFT', 'RIGHT'])
        self.grow_length = 0

    def move(self):
        head_x, head_y = self.body[0]

        if self.direction == 'UP':
            new_head = (head_x, head_y - 1)
        elif self.direction == 'DOWN':
            new_head = (head_x, head_y + 1)
        elif self.direction == 'LEFT':
            new_head = (head_x - 1, head_y)
        elif self.direction == 'RIGHT':
            new_head = (head_x + 1, head_y)

        self.body.insert(0, new_head)

        if self.grow_length > 0:
            self.grow_length -= 1
        else:
            self.body.pop()

    def grow(self):
        self.grow_length += 1

    def check_collision(self):
        return self.body[0] in self.body[1:]