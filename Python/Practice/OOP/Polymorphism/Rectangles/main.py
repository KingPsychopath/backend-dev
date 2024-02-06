
class Rectangle:
    def overlaps(self, rect):
        return (
            self.get_bottom_left()[0] <= rect.get_bottom_right()[0] # left x <= right x : left x is less than or equal to right x
            and self.get_bottom_right()[0] >= rect.get_bottom_left()[0] # right x >= left x : right x is greater than or equal to left x
            and self.get_top_left()[1] >= rect.get_bottom_left()[1] # top y >= bottom y : top y is greater than or equal to bottom y
            and self.get_bottom_right()[1] <= rect.get_top_right()[1] # bottom y <= top y :  bottom y is less than or equal to top y
        )

# Straight diagonal line representation of a rectangle
    def __init__(self, x1, y1, x2, y2): # Could also be written as __init__(self, bottom_left, top_right)
        # Could store bottom_left and top_right as tuples, but then we'd have to calculate the other points - it does save memory though
        self.bottom_left = (x1, y1)
        #self.top_left = (x1, y2)
        #self.bottom_right = (x2, y1)
        self.top_right = (x2, y2)

    def get_bottom_left(self):
        return self.bottom_left
    
    def get_top_left(self):
        # return self.top_left
        return self.bottom_left[0], self.top_right[1]

    def get_bottom_right(self):
        # return self.bottom_right
        return self.top_right[0], self.bottom_left[1]
    
    def get_top_right(self):
        return self.top_right