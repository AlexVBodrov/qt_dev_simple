# el2 = Ellipse(x1, y1, x2, y2)
class Ellipse:
    
    def __init__(self, *args):
        self.is_coords = False
        if len(args) == 4:
            self.is_coords = True
            self.x1 = args[0]
            self.y1 = args[1]
            self.x2 = args[2]
            self.y2 = args[3]
    
    def __repr__(self) -> str:
        if self.is_coords:
            return f"{self.x1}, {self.y1}, {self.x2}, {self.y2}"
        else:
            return f"{Ellipse}()"
    
    def __bool__(self):
        return self.is_coords
    
    def get_coords(self):
        if self.is_coords == False:
            raise AttributeError('нет координат для извлечения')
        return (self.x1, self.y1, self.x2, self.y2)


lst_geom = [Ellipse(), Ellipse(), Ellipse(1, 1, 2, 2), Ellipse(1, 1, 2, 2)]
for i in lst_geom:
    if i:
        i.get_coords()