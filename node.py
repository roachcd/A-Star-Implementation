class Node():
    def __init__(self, data, position, parent=None):
        self.parent = parent
        self.position = position
        self.is_start = False
        self.is_end = False
        self.is_wall = False

        if(data == 1):
            self.is_wall = True
        
        

        self.g = 0 #Distance from start node
        self.h = 0 #Estimated distance to end node
        self.f = 0 #Cost

    def set_start(self, value):
        self.is_start = value

    def set_end(self, value):
        self.is_end = value

    def set_parent(self, parent):
        self.parent = parent