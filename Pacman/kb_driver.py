from kb import *
x = 3
y = 4
kb = PropKB(x, y)
print("KB is initialized, every square have food")
#Our kb going to change everytime the pacman or the four ghost move, thus will change the board.
#These informations will be take into considerate when our agent deciding its next move
kb.edit (1, 2, 0)
kb.edit (1, 2, 3)
kb.edit (2, 1, 3)
kb.edit (2, 1, 4)
kb.edit (3, 2, 2)
kb.edit (0, 2, 4)
kb.edit (0, 0, 0)
kb.print_kb(x, y)


