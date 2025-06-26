import unittest
import time
import tracemalloc
from ..snake import Snake


class TestSnake(unittest.TestCase):
    def setUp(self):
        self.snake = Snake(20, 20, 10)  # width, height, block size

    # --- TESTY FUNKCJONALNE ---
    def test_initial_length(self):
        self.assertEqual(len(self.snake.body), 1)

    def test_move(self):
        initial_head = self.snake.body[0]
        self.snake.move()
        self.assertNotEqual(self.snake.body[0], initial_head)

    def test_grow(self):
        initial_length = len(self.snake.body)
        self.snake.grow()
        self.snake.move()
        self.assertEqual(len(self.snake.body), initial_length + 1)

    def test_collision(self):
        self.snake.body = [(5, 5), (5, 6), (5, 5)]
        self.assertTrue(self.snake.check_collision())

    # --- TESTY INTEGRACYJNE ---
    def test_move_and_grow_integration(self):
        self.snake.grow()
        self.snake.grow()
        self.snake.move()
        self.snake.move()
        self.assertEqual(len(self.snake.body), 3)

    def test_move_then_collision(self):
        self.snake.body = [(5, 5), (5, 6), (5, 7)]
        self.snake.direction = 'UP'  # zmienione z (0, -1) na 'UP'
        self.snake.move()  # should move into (5, 4)
        self.snake.direction = 'DOWN'  # zmiana kierunku na dół
        self.snake.move()  # should move back to (5, 5) - kolizja
        self.assertTrue(self.snake.check_collision())

    # --- TESTY GRANICZNE ---
    def test_move_to_edge(self):
        self.snake.body = [(19, 10)]
        self.snake.direction = 'RIGHT'  # zmienione z (1, 0) na 'RIGHT'
        self.snake.move()
        self.assertTrue(self.snake.body[0][0] >= 20 or self.snake.body[0][0] < 0 or
                        self.snake.body[0][1] >= 20 or self.snake.body[0][1] < 0)

    def test_grow_to_maximum_size(self):
        for _ in range(400):  # 20x20 grid (assuming one segment per block)
            self.snake.grow()
            self.snake.move()
        self.assertEqual(len(self.snake.body), 401)  # 400 growths + initial

    # --- TESTY WYDAJNOŚCI ---
    def test_performance_large_snake(self):
        for _ in range(10000):
            self.snake.grow()
        start = time.time()
        self.snake.move()
        end = time.time()
        self.assertLess(end - start, 0.1)  # powinno wykonać się w < 100 ms

    # --- TESTY PAMIĘCI ---
    def test_memory_usage(self):
        tracemalloc.start()
        for _ in range(10000):
            self.snake.grow()
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        self.assertLess(peak, 10**7)  # mniej niż 10 MB pamięci

    # --- TESTY JAKOŚCI KODU (proste heurystyki) ---
    def test_code_quality_snake_methods_exist(self):
        self.assertTrue(hasattr(self.snake, "move"))
        self.assertTrue(hasattr(self.snake, "grow"))
        self.assertTrue(hasattr(self.snake, "check_collision"))

    def test_no_duplicate_body_segments(self):
        self.snake.body = [(5, 5), (5, 6), (5, 7)]
        self.assertEqual(len(set(self.snake.body)), len(self.snake.body))

    def test_direction_is_valid(self):
        # Zmieniony test, aby sprawdzał stringi zamiast krotek
        self.assertIn(self.snake.direction, ['UP', 'DOWN', 'LEFT', 'RIGHT'])


if _name_ == '_main_':
    unittest.main()