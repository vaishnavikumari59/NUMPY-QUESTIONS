import numpy as np
ele = eval(input('Enter a list\n'))
x = np.array(ele, dtype=np.str)
print("\nOriginal Array:")
print(x)
r = np.char.zfill(x, 5)
print("\nNumeric string of 5 digits with zeros:",r)
