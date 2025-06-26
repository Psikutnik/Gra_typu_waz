import matplotlib.pyplot as plt
import os


def plot_scores(scores):
    if not scores:
        return

    plt.figure(figsize=(10, 5))
    plt.plot(scores, marker='o')
    plt.title('High Scores History')
    plt.xlabel('Game')
    plt.ylabel('Score')
    plt.grid(True)

    if not os.path.exists('assets'):
        os.makedirs('assets')

    plt.savefig('assets/plot.png')
    plt.close()