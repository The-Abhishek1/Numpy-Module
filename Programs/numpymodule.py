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

#Working with Array Elements

print(arr3[1][0])
print(arr2[1])

#Negative indexing

print(arr3[-1,0])

#Array Slicing 1D
arr5  = np.array([1,2,3,4,5,6,7,8,9])
print("Array Slicing1:", arr5[1:4])
print("Array Slicing2:", arr5[4:])
#using Step value
print("Array Slicing3:", arr5[1:5:2])

# 2D array Slicing

print("2d array slicing:",arr2[1,1:3])

#checking the datatype of an array

print("data type array 5:", arr5.dtype)

#String Array 

string_arr1 = np.array(["Apple","Banana","Mango"])

print(string_arr1)

#Checking the datatype of string array
print("data type of string_arr1:",string_arr1.dtype)

#manually setting datatype of an array

string_arr2 = np.array([1,2,3,4], dtype='S')

print("Datatype of an array string_arr2:",string_arr2.dtype)