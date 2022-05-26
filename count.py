import numpy as np
ele = eval(input('Enter a list\n'))
x = np.array(ele, dtype=np.str)
print("\nOriginal Array:",x)
r = np.char.count(x, "P")
print("Number of 'P':",r)