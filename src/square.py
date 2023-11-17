from rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, side_a):
        if side_a <= 0:
            raise ValueError("Нельзя построить квалрат")
        self.side_a = side_a

    def get_area(self):
        return self.side_a * 2

    def get_perimetr(self):
        return self.side_a * 4
