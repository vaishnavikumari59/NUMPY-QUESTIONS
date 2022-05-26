import numpy as np
element = eval (input('Enter a list\n'))
arr = np.array(element,dtype=np.str)
new_array = np.char.multiply(arr,3)  
print('3 times repeated array :', new_array)
