import numpy as np
ele_1 = eval (input("Enter list 1\n"))
ele_2 = eval (input("Enter list 2\n"))
arr_1=np.array(ele_1,dtype=np.str)
arr_2=np.array(ele_2,dtype=np.str)
print(arr_1)
print(arr_2)
new_array=np.char.add(arr_1,arr_2)  
print('Concatenated array :' , new_array)