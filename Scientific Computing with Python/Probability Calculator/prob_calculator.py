import copy
import random

# Consider using the modules imported above.


class Hat:
    def __init__(self, **kwargs: list[int]) -> None:
        self.contents = []
        for key, value in kwargs.items():
            for i in range(value):
                self.contents.append(key)

    def draw(self, balls_removed: int) -> list[str] or None:
        if balls_removed > len(self.contents):
            return self.contents
        else:
            balls_chosen = []
            for i in range(balls_removed):
                ball = random.choice(self.contents)
                balls_chosen.append(ball)
                self.contents.remove(ball)
            return balls_chosen


def experiment(
    hat: object,
    expected_balls: dict,
    num_balls_drawn: int,
    num_experiments: int,
) -> float:
    successful = 0
    for i in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        balls = hat_copy.draw(num_balls_drawn)
        for key, value in expected_balls.items():
            if balls.count(key) < value:
                break
        else:
            successful += 1
    return successful / num_experiments
