class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def set_width(self, side):
        if self.width == self.height:
            self.width = side
            self.height = side
        else:
            self.width = side

    def set_height(self, side):
        if self.width == self.height:
            self.width = side
            self.height = side
        else:
            self.height = side

    def get_area(self):
        return self.width * self.height
    
    def get_perimeter(self):
        return (self.width * 2 + self.height * 2)
    
    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        
        pic = ''
        for _ in range(self.height):
            for _ in range(self.width):
                pic = pic + '*'
            pic = pic + '\n'
        return pic
    
    def get_amount_inside(self, shape):
        heightFit = self.height/shape.height
        widthFit = self.width/shape.width

        return int(heightFit) * int(widthFit)
        
    def __str__(self):
        if self.width == self.height:
            return "Square(side=" + str(self.width) + ")"
        else:
            return "Rectangle(width=" + str(self.width) + ", height=" + str(self.height) + ")"

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
    
    def set_side(self, side):
        self.set_height(side)
        self.set_width(side)
    