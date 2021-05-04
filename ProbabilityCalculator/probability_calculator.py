# A program that will determine the approximate probability of drawing certain balls randomly from a hat.
# Class should take a variable number of arguments that specify the number of balls of each color that are in the hat.
# For example: hat1 = Hat(yellow=3, blue=2, green=6); hat3 = Hat(red=5, orange=4, black=1, blue=0, pink=2, striped=9)
# A hat will always be created with at least one ball.

# import copy
import random


class Hat:
    def __init__(self, **kwargs):
        self.balls = dict()
        for key, value in kwargs.items():
            self.balls[key] = value

# The arguments passed into the hat object upon creation should be converted to a contents instance variable.
# Contents should be a list of strings containing one item for each ball in the hat.
# Each item in the list should be a color name representing a single ball of that color.

        self.contents = list()
        for key, value in self.balls.items():
            keys = (key,) * value
            for item in keys:
                self.contents.append(item)

# The Hat class should have a draw method that accepts an argument indicating the number of balls to draw from the hat.
# This method should remove balls at random from contents and return those balls as a list of strings.
# The balls should not go back into the hat during the draw.
# If the number of balls to draw exceeds the available quantity, return all the balls.


    def draw(self, number):
        self.number = number
        self.returned_balls = list()
        if self.number >= len(self.contents):
            self.returned_balls.extend(self.contents)
        else:
            for x in range(self.number):
                random_draw = random.choice(self.contents)
                self.returned_balls.append(random_draw)
                self.contents.remove(random_draw)
                if len(self.contents) < self.number:
                    self.contents.clear()
                    for key, value in self.balls.items():
                        keys = (key,) * value
                        for item in keys:
                            self.contents.append(item)
                            continue
        return self.returned_balls

# Next, create an experiment function, not inside the Hat class.
# This function should accept the following arguments: hat, expected_balls, num_balls_drawn, num_experiments.
# hat: A hat object containing balls that should be copied inside the function.
# expected_balls: An object indicating the exact group of balls to attempt to draw from the hat for the experiment.
# For example: expected_balls {"blue":2, "red":1}.
# num_balls_drawn: The number of balls to draw out of the hat in each experiment.
# num_experiments: The number of experiments to perform.
# The experiment function should return a probability e.g.(n-times we get expected balls, m-number of experiments - N/M)


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    drawn_balls = dict()
    expected_balls_drawn = 0
    count = num_experiments

    while count > 0:
        Hat.draw(hat, num_balls_drawn)
        for ele in hat.returned_balls:
            if ele in drawn_balls.keys():
                drawn_balls[ele] += 1
            else:
                drawn_balls[ele] = 1
        if check_balls(expected_balls, drawn_balls) is None:
            expected_balls_drawn += 1
        drawn_balls.clear()
        count -= 1
    probability = expected_balls_drawn/num_experiments
    return probability

def check_balls(a,b):
    result = list()
    final_result = list()
    for x in a.keys():
        if x in b.keys():
            amount = a[x] - b[x]
            if amount <= 0:
                result.append("True")
            else:
                result.append("False")
        else:
            return False
    for x in result:
        if x == "False":
            final_result.append("False")
    for x in final_result:
        if x == "False":
            return False



# hat = Hat(blue=3,red=2,green=6)
# print(experiment(hat=hat, expected_balls={"blue":2,"green":1}, num_balls_drawn=4, num_experiments=10))

# hat = Hat(yellow=5,red=1,green=3,blue=9,test=1)
# hat = Hat(yellow=4,blue=3,test=1)
# print(experiment(hat=hat, expected_balls={"yellow":1,"blue":1,"test":1}, num_balls_drawn=3, num_experiments=100))

import unittest
class UnitTests(unittest.TestCase):
    def test_hat_class_contents(self):
        hat = Hat(red=3,blue=2)
        actual = hat.contents
        expected = ["red","red","red","blue","blue"]
        self.assertEqual(actual, expected, 'Expected creation of hat object to add correct contents.')

    def test_hat_draw(self):
        hat = Hat(red=5,blue=2)
        actual = hat.draw(2)
        expected = ['blue', 'red']
        self.assertEqual(actual, expected, 'Expected hat draw to return two random items from hat contents.')
        actual = len(hat.contents)
        expected = 5
        self.assertEqual(actual, expected, 'Expected hat draw to reduce number of items in contents.')

    def test_prob_experiment(self):
        hat = Hat(blue=3,red=2,green=6)
        probability = experiment(hat=hat, expected_balls={"blue":2,"green":1}, num_balls_drawn=4, num_experiments=1000)
        actual = probability
        expected = 0.272
        self.assertAlmostEqual(actual, expected, delta = 0.01, msg = 'Expected experiment method to return a different probability.')
        hat = Hat(yellow=5,red=1,green=3,blue=9,test=1)
        probability = experiment(hat=hat, expected_balls={"yellow":2,"blue":3,"test":1}, num_balls_drawn=20, num_experiments=100)
        actual = probability
        expected = 1.0
        self.assertAlmostEqual(actual, expected, delta = 0.01, msg = 'Expected experiment method to return a different probability.')


if __name__ == "__main__":
    unittest.main()
