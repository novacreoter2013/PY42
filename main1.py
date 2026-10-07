import numpy as np

a = np.arange(9,dtype = np.float64).reshape(3,3)
print("FIRST ARRAY :")
print(a)
print('\n')

b = np.array([10,10,10])
print('SECOND ARRAY :')
print(b)
print('\n')

print('ADD THE TWO ARRAYS :')
print(np.add(a,b))
print('\n')

print('SUBTRACT THE TWO ARRAYS :')
print(np.subtract(a,b))
print('\n')

print('MULTIPLY THE TWO ARRAYS:')
print(np.multiply(a,b))
print('\n')

print('DIVIDE THE TWO ARRAYS :')
print(np.divide(a,b))
print('\n')