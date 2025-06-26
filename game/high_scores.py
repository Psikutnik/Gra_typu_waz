import json
from functools import reduce


class HighScores:
    def __init__(self, filename):
        self.filename = filename
        self.scores = self.load_scores()

    def load_scores(self):
        try:
            with open(self.filename, 'r') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_scores(self):
        with open(self.filename, 'w') as f:
            json.dump(self.scores, f, indent=4)

    def add_score(self, score):
        self.scores.append(score)
        self.scores.sort(reverse=True)
        self.scores = self.scores[:10]  # Keep only top 10
        self.save_scores()

    def get_scores(self):
        return self.scores

    def get_highest_score(self):
        return max(self.scores) if self.scores else 0

    def get_average_score(self):
        if not self.scores:
            return 0
        total = reduce(lambda x, y: x + y, self.scores)
        return total / len(self.scores)