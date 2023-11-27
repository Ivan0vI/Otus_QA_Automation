from src.figure import Figure


class Circle(Figure):
    pi = 3.14159

    def __init__(self, r, name):
        super().__init__(name="Circle")
        if r <= 0:
            raise ValueError("Нельзя создать круг")
        self.r = r

    def get_area(self):
        return self.pi * self.r * self.r

    def get_perimetr(self):
        return 2 * self.pi * self.r
