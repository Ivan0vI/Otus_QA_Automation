from figure import Figure

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

    def add_area(self, other_figure):
        super().__init__(self.add_area)
        return self.get_area() + other_figure.get_area()


circle = Circle(5, "Circle")
other_figure = (1)
print(circle.get_area(), circle.name, circle.add_area())

