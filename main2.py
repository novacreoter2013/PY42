import numpy as  np

arr = np.array([1,2,3,4,5,4,4])
x = np.where(arr == 4)
print(x)

arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])

arr = np.concatenate((arr1 , arr2))
print(arr)

arr3 = np.array([1,2,3])

for x in arr:
    print(x)


arr4 = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
newarr = arr4.reshape(4,3)
print(newarr)

arr5 = np.array([1,2,3,4] , dtype = 'S')
print(arr5)
print(arr5.dtype)
print(type(arr5))