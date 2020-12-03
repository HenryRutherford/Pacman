
class KB:
    def __init__(self, width, height):
        raise NotImplementedError

    def tell(self, height, width):
        raise NotImplementedError

    def ask(self, height, width):
        raise NotImplementedError


    def retract(self, height,width):
        raise NotImplementedError

class PropKB(KB):
    def __init__ (self, height, width):
        self.array = [height][width]

    def  tell(self, height, width):
        self.array [height][width] = 1

    def ask(self, height ,width):
        if self.array[height][width] == 1:
            return 1
        else:
            return 0

    def retract(self, height, width):
        self.array[height][width] = 0