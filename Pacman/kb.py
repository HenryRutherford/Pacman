
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
    def __init__ (self, x, y):
        self.array = [[1 for i in range(x)]for j in range(y)]

    def tell(self, x, y, state):
        self.array[x][y] = state

    def ask(self, x, y):
        return self.array[x][y];

    def edit(self, x, y, state):
        if state == 0:
            if(self.ask(x, y) == 1):
                print("Successfully change from having food to empty")
            if (self.ask(x, y) == 2):
                print("Successfully change from having pacman to empty")
            if (self.ask(x, y) == 3):
                print("Successfully change from having no food and a ghost to empty")
            if (self.ask(x, y) == 4):
                print("Successfully change from having food and a ghost to empty")
            self.tell(x, y, state)
        if state == 1:
            if self.ask(x, y) == 4:
                print("Successfully change from having food and a ghost to having food")
                self.tell(x, y, state)
            else:
                if (self.ask(x, y) == 0):
                    print("Unsuccessfully change from empty to having food")
                if (self.ask(x, y) == 2):
                    print("Unsuccessfully change from having pacman to having food")
                if (self.ask(x, y) == 3):
                    print("Unsuccessfully change from having no food and a ghost to having food")
        if state == 2:
            if (self.ask(x, y) == 0):
                print("Successfully change from empty to having pacman")
            if (self.ask(x, y) == 1):
                print("Successfully change from having food to having pacman")
            if (self.ask(x, y) == 3):
                print("Successfully change from having no food and a ghost to having pacman")
            if (self.ask(x, y) == 4):
                print("Successfully change from having food and a ghost to having pacman")
            self.tell(x, y, state)
        if state == 3:
            if (self.ask(x, y) == 0):
                print("Successfully change from empty to having no food and a ghost")
            if (self.ask(x, y) == 1):
                print("Successfully change from having food to having no food and a ghost")
            if (self.ask(x, y) == 2):
                print("Successfully change from having pacman to having no food and a ghost")
            if (self.ask(x, y) == 4):
                print("Successfully change from having food and a ghost to having no food and a ghost")
            self.tell(x, y, state)
        if state == 4:
            if self.ask(x, y) == 1:
                print("Successfully change from having food to have a ghost and food")
                self.tell(x, y, state)
            else:
                if (self.ask(x, y) == 0):
                    print("Unsuccessfully change from empty to having food and a ghost")
                if (self.ask(x, y) == 2):
                    print("Unsuccessfully change from having pacman to having food having food and a ghost")
                if (self.ask(x, y) == 3):
                    print("Unsuccessfully change from having no food and a ghost to having food and a ghost")
    def print_kb(self, x, y):
        for j in range(x):
            for i in range(y):
                print("[", end = "")
                if self.array[i][j] == 0:
                    print("    empty   ", end = "")
                if self.array[i][j] == 1:
                    print("    food    ", end = "")
                if self.array[i][j] == 2:
                    print("   pacman   ", end = "")
                if self.array[i][j] == 3:
                    print("    ghost   ", end = "")
                if self.array[i][j] == 4:
                    print("ghost & food", end = "")
                print("]", end = "")
            print("\n")