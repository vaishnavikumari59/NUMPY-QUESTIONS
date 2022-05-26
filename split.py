import numpy as np
ele = eval(input('Enter a list\n'))
x = np.array(ele, dtype=np.str)
print("Original Array:")
print(x)
r = np.char.splitlines(x)
print(r)
