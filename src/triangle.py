from figure import Figure
class Triangle(Figure):
    def __init__(self, side_a, side_b, base, height):
        super().__init__(name="Triangle")
        if side_a <= 0 or side_b <= 0 or base <= 0 or height <= 0:
            raise ValueError("Нельзя построить треугольник")
        self.side_a = side_a
        self.side_b = side_b
        self.base = base
        self.height = height

    def get_area(self):
        return self.height * self.base / 2

    def get_perimetr(self):
        return self.side_a + self.side_b + self.base




triangle = Triangle(13, 14, 15, 16)
print(triangle.get_area())
print(triangle.get_perimetr())