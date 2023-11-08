import unittest
from prob_calculator import Hat, experiment


class MyTestCase(unittest.TestCase):
    def test_draw(self):
        hat = Hat(red=5, orange=4, black=1, blue=0, pink=2, striped=9)
        balls_drawn = hat.draw(3)
        # We don't know which balls will be drawn but at least we know we should have 3 of them in the dict.
        num_balls_drawn = sum(balls_drawn.values())
        self.assertEqual(3, num_balls_drawn)

        # If the number of balls to draw exceeds the available quantity, return all the balls.
        hat = Hat(red=5, orange=4, black=1, blue=0, pink=2, striped=9)
        balls_drawn = hat.draw(45)
        num_balls_drawn = sum(balls_drawn.values())
        self.assertEqual(21, num_balls_drawn)

    def test_experiment(self):
        # A case where we don't know the result for sure
        # At least we know that 0 <= probability <= 1
        hat = Hat(black=16, red=14, green=13)
        probability = experiment(
            hat=hat,
            expected_balls={"red": 2, "green": 1},
            num_balls_drawn=5,
            num_experiments=4500
        )
        # We don't know what the result will be but at least we know it's should be in [0; 1]
        self.assertLessEqual(probability, 1)
        self.assertGreaterEqual(probability, 0)

        # A case where we should have 0
        hat = Hat(black=6, red=4, green=3)
        probability = experiment(
            hat=hat,
            expected_balls={"red": 7},
            num_balls_drawn=2,
            num_experiments=3
        )
        self.assertEqual(0, probability)

        # A case where we should have 1
        hat = Hat(red=4)
        probability = experiment(
            hat=hat,
            expected_balls={"red": 2},
            num_balls_drawn=2,
            num_experiments=3
        )
        self.assertEqual(1, probability)


if __name__ == '__main__':
    unittest.main()
