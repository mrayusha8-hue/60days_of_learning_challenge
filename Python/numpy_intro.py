import numpy as np

# 0-D ARRAY
arr = np.array(2)
print(arr)

# 1-D ARRAY
arr = np.array([4,5,6,7])
print(arr)

#Checking Dimension
arr = np.array(2)
print(arr.ndim)

arr = np.array([4,5,6,7])
print(arr.ndim)

#defining number of dimnensions using ndmin(Higher Dimesnional Array)
arr = np.array([4,5,6,7,], ndmin=4)
print(arr)

#Array Indexing

arr = np.array([4,5,6,7])
print(arr[2])

#Adding  two elements from array
arr = np.array([4,5,6,7])
print(arr[2] + arr[0])

#Accessing 2 dimensional array
arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print('2nd element on 1st row: ', arr[0, 1])

#Negative Indexing
arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print('second last element from first dim: ', arr[0, -2])

#Array_Slicing 
arr = np.array([1, 2, 3, 4, 5, 6, ])
print(arr[1:4])

#With Steps
arr = np.array([1, 2, 3, 4, 5, 6, ])
print(arr[1:4:3])
print(arr[1:-2])   #Negative Slicing

#For 2-D
arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print(arr[0, 1:-2]) 

#----Data Types -----
arr = np.array(['apple', 'banana', 'cherry'])
print(arr.dtype)

#Changing Datatypes
arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
a = arr.astype('f')
print(a)
print(a.dtype)


arr = np.array([-1, 0, 1])
a = arr.astype(bool)
print(a)