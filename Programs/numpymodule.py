import numpy as np 

# 0 Dimensional array
arr0 = np.array(42)

print(arr0)

#To Check the type of an array
print(type(arr0))

# 1 Dimensional array
  
arr1 = np.array([1,2,3,4,5])

print(arr1)

# 2 Dimensional array

arr2 = np.array([[1,2,3,4],[5,6,7,8]])

print(arr2)

# 3 Dimensional array

arr3 = np.array([[[1,2,3,4],[5,6,7,8]],[[1,2,3,4],[5,6,7,8]]])

print(arr3)

#checkig the Dimensions of the array

print(arr0.ndim)
print(arr1.ndim)
print(arr2.ndim)
print(arr3.ndim)

#Higher Dimensional Arrays

arr4 = np.array([1,2,3], ndmin= 5)

print("Dimension of Array 4 : ",arr4.ndim)