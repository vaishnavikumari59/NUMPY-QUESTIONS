import numpy as np
ele = eval(input('Enter a list\n'))
arr = np.array(ele, dtype=np.str)
print("Original Array:")
print(arr)
stripped = np.char.strip(arr)
print("\nRemove the leading and trailing whitespaces: ", stripped)
