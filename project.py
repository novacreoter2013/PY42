import numpy as np

a = np.array([10, 20, 30, 40, 50])
b = np.array([2, 4, 5, 8, 10])

add_result = np.add(a, b)
sub_result = np.subtract(a, b)
mul_result = np.multiply(a, b)
div_result = np.divide(a, b)
pct_result = (a / np.sum(a)) * 100

print("Array A:", a)
print("Array B:", b)
print("Addition:", add_result)
print("Subtraction:", sub_result)
print("Multiplication:", mul_result)
print("Division:", div_result)
print("Percentage of total (Array A):", pct_result)