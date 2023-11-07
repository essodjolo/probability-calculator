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
        hat = Hat(black=6, red=4, green=3)
        probability = experiment(
            hat=hat,
            expected_balls={"red": 2, "green": 1},
            num_balls_drawn=5,
            num_experiments=2000
        )
        # We don't know what the result will be but at least we know it's should be in [0; 1]
        self.assertLessEqual(1, probability)
        self.assertGreaterEqual(0, probability)


if __name__ == '__main__':
    unittest.main()
