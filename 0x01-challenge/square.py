#!/usr/bin/python3
"""zaeazeas"""


class square():
    """aaerrazeaze"""
    size = 0

    def __init__(self, *args, **kwargs):
        """aazeze"""
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.size ** 2

    def PermiterOfMySquare(self):
        """aazeze"""
        return 4 * self.size

    def __str__(self):
        """azazeae"""
        return "{}/{}".format(self.size, self.size)


if __name__ == "__main__":

    s = square(size=12)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
