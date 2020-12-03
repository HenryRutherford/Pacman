
class KB:
    def __init__(self, height, width):
        raise NotImplementedError

    def tell(self, x, y, state):
        raise NotImplementedError

    def ask(self, x, y):
        raise NotImplementedError


    def edit(self,x ,y ,state):
        raise NotImplementedError

class PropKB(KB):
    #0 = empty
    #1 = food
    #2 = pacman
    #3 = no fodd & ghost
    #4 = food & ghost
    #Every coordinates start off as 1
    def __init__ (self, height, width):
        self.array = [[1 for i in range(height)]for j in range(width)]

    def tell(self, x, y, state):
        self.array[x][y] = state

    def ask(self, x, y):
        return self.array[x][y];

    def edit(self, x, y, state):
        if state == 0:
            print("Successfully change from ", self.ask(x, y), " to ", state)
            self.tell(x, y, state)
        if state == 1:
            if self.ask(x, y) == 4 or self.ask(x, y) == 1:
                print("Successfully change from ", self.ask(x, y), " to ", state)
                self.tell(x, y, state)
        if state == 2:
            print("Successfully change from ", self.ask(x, y), " to ", state)
            self.tell(x, y, state)
        if state == 3:
            print("Successfully change from ", self.ask(x, y), " to ", state)
            self.tell(x, y, state)
        if state == 4:
            if self.ask(x, y) == 4 or self.ask(x, y) == 1:
                print("Successfully change from ", self.ask(x, y), " to ", state)
                self.tell(x, y, state)
    def print_kb(self):
        print (self.array)
