import numpy as np
ele = eval(input('Enter a list\n'))
arr = np.array(ele,dtype=np.str)
print(arr)
lower_case = np.char.lower(arr)
upper_case = np.char.upper(arr)
swap_case = np.char.swapcase(arr)
title_case = np.char.title(arr)
capitalized_case = np.char.capitalize(arr)
print('\nLowered case :',lower_case)
print('\nUppered case :',upper_case)
print('\nSwap case :',swap_case)
print('\nTitle case :',title_case)
print('\nCapitalized case :',capitalized_case)