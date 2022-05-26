import numpy as np
ele = eval(input('enter a list\n'))
arr = np.array(ele,dtype=np.str)
c = np.char.center(arr,15,fillchar="_")
l = np.char.ljust(arr,15,fillchar="_")
r = np.char.rjust(arr,15,fillchar="_")
print(f'Centered : {c}\nLeft Justified : {l}\nRight Justified : {r}')