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


#ones(),zeros()
print(np.ones(2))
print(np.zeros(3))

#Copy and View
a = np.array([1,2,3,4,5])
x = a.copy()   # Copy is a new array
a[1] = 86
print(a)
print(x)

a = np.array([1,2,3,4,5])
x = a.view()   # View is just view of original array
a[1] = 86
print(a)
print(x)

#Shape and Reshape
a = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(a.shape)

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,])
newarr = arr.reshape(6, 2)
print(newarr)

a = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(a.reshape(-1))  #2D to 1D

#random generator
from numpy import random
x = random.rand()   #for float
print(x)

x = random.randint(5)  #for int
print(x)

x=random.randint(100, size=(5)) #for array
print(x)

x=random.randint(100, size=(2,3))
print(x)