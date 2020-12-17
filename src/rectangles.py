from points import Point


class Rectangle:
    # renamed `broad` and `high` as they do not make sense in the context of a
    # rectangle
    def __init__(self, starting_point, width, height):
        self.starting_point = starting_point
        self.width = width
        self.height = height

        # calculate the top-right and bottom-left co-ordinates
        self.top_right = self.starting_point.x + self.width
        self.bottom_left = self.starting_point.y + self.height

    # changed to `calc_area` as `area` sounded too much like a property
    def calc_area(self):
        return self.width * self.height

    # moved method into Rectangle class and renamed to `print_coordinates`, as this
    # makes it clear what this method does
    def print_coordinates(self):
        print('Starting Point (X)): ' + str(self.starting_point.x))
        print('Starting Point (Y)): ' + str(self.starting_point.y))
        print('End Point X-Axis (Top Right): ' + str(self.top_right))
        print('End Point Y-Axis (Bottom Left): ' + str(self.bottom_left))


# renamed as `create_rectangle` which is a better name, could also be something like
# `build_rectangle`. This is more concise and tells us what the method does
def create_rectangle():
    starting_point = Point(50, 100)

    # renamed to `rectangle` to avoid the abbreviation
    react = Rectangle(starting_point, 90, 10)
    return react


rectangle = create_rectangle()

print(rectangle.calc_area())
rectangle.print_coordinates()
