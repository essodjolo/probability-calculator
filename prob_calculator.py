import random
from collections import Counter
from copy import copy


class Hat:
    """
    A hat will always be created with at least one ball.
    The arguments passed into the hat object upon creation should be converted to a contents instance variable.
    contents should be a list of strings containing one item for each ball in the hat.
    Each item in the list should be a color name representing a single ball of that color.
    For example, if the hat is {"red": 2, "blue": 1}, contents should be ["red", "red", "blue"].
    """
    def __init__(self, **kwargs: {str: int}):
        self.contents: list[str] = []
        for color, number in kwargs.items():
            for i in range(number):
                self.contents.append(color)

    def __repr__(self):
        return str(self.contents)

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


def convert_to_flattened_list(balls_dict: {str: int}, resulting_list: list[str]):
    for color, number in balls_dict.items():
        for i in range(number):
            resulting_list.append(color)


def experiment(
        hat: 'Hat',
        expected_balls: {str: int},
        num_balls_drawn: int,
        num_experiments: int
) -> float:

    # if no experiment is done then probability is set to 0
    if num_experiments == 0:
        return 0.0

    num_matching_balls: int = 0

    for i in range(num_experiments):
        copy_of_hat = copy(hat)
        actual_balls_drawn = copy_of_hat.draw(num_balls_drawn)

        score: int = 1
        for color, number in expected_balls.items():
            if number <= actual_balls_drawn.get(color, 0):
                score *= 1  # Should stay in this condition for ALL iteration to keep the value 1.
            else:
                score *= 0  # If we fall in this condition for at least one time, then score will be 0

        num_matching_balls += score

    probability = float(num_matching_balls/num_experiments)
    return probability
