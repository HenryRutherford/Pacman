from kb import *
x = 3
y = 4
kb = PropKB(x, y)
print("KB is initialized, every square is 1")
kb. edit (1, 2, 0)
kb. edit (1, 2, 3)
kb. edit (2, 1, 3)
kb. edit (2, 1, 4)
kb.print_kb()


