import random
from collections import Counter


class Hat:
    def __init__(self, **kwargs: {str: int}):
        self.contents: list[str] = []
        for color, number in kwargs.items():
            for i in range(number):
                self.contents.append(color)

    def draw(self, num_balls_drawn: int) -> {str: int}:
        """
        This method should remove balls at random from contents and return those balls as a list of strings.
        The balls should not go back into the hat during the draw, similar to an urn experiment without replacement.
        If the number of balls to draw exceeds the available quantity, return all the balls.
        :param num_balls_drawn:
        :return: a dict a drawn balls
        """
        balls_drawn: {str: int} = {}
        if num_balls_drawn >= len(self.contents):
            balls_drawn = Counter(self.contents)
            self.contents = []
            return balls_drawn
        else:
            for i in range(num_balls_drawn):
                random_number = random.randrange(len(self.contents))
                color = self.contents[random_number]
                balls_drawn[color] = balls_drawn.get(color, 0) + 1
                self.contents.pop(random_number)
            return balls_drawn


def experiment(
        hat: 'Hat',
        expected_balls: {str: int},
        num_balls_drawn: int,
        num_experiments: int
):
    return 2
