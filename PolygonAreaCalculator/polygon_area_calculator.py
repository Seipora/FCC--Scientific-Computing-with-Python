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
