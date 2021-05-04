class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width
        return width

    def set_height(self, height):
        self.height = height
        return height

    def get_area(self):
        height = self.height
        width = self.width
        return width * height

    def get_perimeter(self):
        height = self.height
        width = self.width
        return 2 * width + 2 * height

    def get_diagonal(self):
        height = self.height
        width = self.width
        return (width ** 2 + height ** 2) ** .5

    def get_picture(self):
        number_of_lines = self.height
        number_of_stars_in_line = ""
        for star in range(number_of_lines):
            number_of_stars_in_line += "*" * self.width + "\n"

        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        else:
            return number_of_stars_in_line

    def get_amount_inside(self, shape):
        self.shape = shape
        total = int(self.get_area()/shape.get_area())
        return total

    def __str__(self):
        return "{}(width={}, height={})".format(self.__class__.__name__, self.width, self.height)


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
        self.height = side
        self.width = side

    def __str__(self):
        return "{}(side={})".format(self.__class__.__name__, self.width)

    def set_side(self, side):
        self.width = side
        self.height = side
        return side

    def set_width(self, side):
        self.width = side
        self.height = side
        return side

    def set_height(self, side):
        self.width = side
        self.height = side
        return side


# rect = Rectangle(2,3)
# rect.set_width(7)
# rect.set_height(3)
# print(rect.get_picture())

import unittest

class UnitTests(unittest.TestCase):
    def setUp(self):
        self.rect = Rectangle(3, 6)
        self.sq = Square(5)

    def test_subclass(self):
        actual = issubclass(Square, Rectangle)
        expected = True
        self.assertEqual(actual, expected, 'Expected Square class to be a subclass of the Rectangle class.')

    def test_distinct_classes(self):
        actual = Square is not Rectangle
        expected = True
        self.assertEqual(actual, expected, 'Expected Square class to be a distinct class from the Rectangle class.')

    def test_square_is_square_and_rectangle(self):
        actual = isinstance(self.sq, Square) and isinstance(self.sq, Rectangle)
        expected = True
        self.assertEqual(actual, expected,
                         'Expected square object to be an instance of the Square class and the Rectangle class.')

    def test_rectangle_string(self):
        actual = str(self.rect)
        expected = "Rectangle(width=3, height=6)"
        self.assertEqual(actual, expected,
                         'Expected string representation of rectangle to be "Rectangle(width=3, height=6)"')

    def test_square_string(self):
        actual = str(self.sq)
        expected = "Square(side=5)"
        self.assertEqual(actual, expected, 'Expected string representation of square to be "Square(side=5)"')

    def test_area(self):
        actual = self.rect.get_area()
        expected = 18
        self.assertEqual(actual, expected, 'Expected area of rectangle to be 18')
        actual = self.sq.get_area()
        expected = 25
        self.assertEqual(actual, expected, 'Expected area of square to be 25')

    def test_perimeter(self):
        actual = self.rect.get_perimeter()
        expected = 18
        self.assertEqual(actual, expected, 'Expected perimeter of rectangle to be 18')
        actual = self.sq.get_perimeter()
        expected = 20
        self.assertEqual(actual, expected, 'Expected perimeter of square to be 20')

    def test_diagonal(self):
        actual = self.rect.get_diagonal()
        expected = 6.708203932499369
        self.assertEqual(actual, expected, 'Expected diagonal of rectangle to be 6.708203932499369')
        actual = self.sq.get_diagonal()
        expected = 7.0710678118654755
        self.assertEqual(actual, expected, 'Expected diagonal of square to be 7.0710678118654755')

    def test_set_atributes(self):
        self.rect.set_width(7)
        self.rect.set_height(8)
        self.sq.set_side(2)
        actual = str(self.rect)
        expected = "Rectangle(width=7, height=8)"
        self.assertEqual(actual, expected,
                         'Expected string representation of rectangle after setting new values to be "Rectangle(width=7, height=8)"')
        actual = str(self.sq)
        expected = "Square(side=2)"
        self.assertEqual(actual, expected,
                         'Expected string representation of square after setting new values to be "Square(side=2)"')
        self.sq.set_width(4)
        actual = str(self.sq)
        expected = "Square(side=4)"
        self.assertEqual(actual, expected,
                         'Expected string representation of square after setting width to be "Square(side=4)"')

    def test_rectangle_picture(self):
        self.rect.set_width(7)
        self.rect.set_height(3)
        actual = self.rect.get_picture()
        expected = "*******\n*******\n*******\n"
        self.assertEqual(actual, expected, 'Expected rectangle picture to be different.')

    def test_squaree_picture(self):
        self.sq.set_side(2)
        actual = self.sq.get_picture()
        expected = "**\n**\n"
        self.assertEqual(actual, expected, 'Expected square picture to be different.')

    def test_big_picture(self):
        self.rect.set_width(51)
        self.rect.set_height(3)
        actual = self.rect.get_picture()
        expected = "Too big for picture."
        self.assertEqual(actual, expected, 'Expected message: "Too big for picture."')

    def test_get_amount_inside(self):
        self.rect.set_height(10)
        self.rect.set_width(15)
        actual = self.rect.get_amount_inside(self.sq)
        expected = 6
        self.assertEqual(actual, expected, 'Expected `get_amount_inside` to return 6.')

    def test_get_amount_inside_two_rectangles(self):
        rect2 = Rectangle(4, 8)
        actual = rect2.get_amount_inside(self.rect)
        expected = 1
        self.assertEqual(actual, expected, 'Expected `get_amount_inside` to return 1.')

    def test_get_amount_inside_none(self):
        rect2 = Rectangle(2, 3)
        actual = rect2.get_amount_inside(self.rect)
        expected = 0
        self.assertEqual(actual, expected, 'Expected `get_amount_inside` to return 0.')


if __name__ == "__main__":
    unittest.main()
#
