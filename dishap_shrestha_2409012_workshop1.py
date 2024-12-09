# -*- coding: utf-8 -*-
"""Dishap_Shrestha_2409012_Workshop1

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1MrKdhPrj1RwNaVpQMGmDBrThV-uUttTb
"""

import numpy as np

print(np.array([1,2,3])+np.array([1]))

#compatible for broadcast
#checking from the last either the dimension must be equal or 1
#5x3 5x1 1 and 3 aren't equal but one of them is One. 5 and 5 are equal.

"""Problem - 1: Array Creation:
Complete the following Tasks:
1. Initialize an empty array with size 2X2.
2. Initialize an all one array with size 4X2.
3. Return a new array of given shape and type, filled with fill value.{Hint: np.full}
4. Return a new array of zeros with same shape and type as a given array.{Hint: np.zeros like}
5. Return a new array of ones with same shape and type as a given array.{Hint: np.ones like}
6. For an existing list new_list = [1,2,3,4] convert to an numpy array.{Hint: np.array()}
"""

empty_array=np.empty((2,2));
print(empty_array)

ones_array=np.ones((4,2));
print(ones_array)

new_shape = (2, 5)  # Shape for the new array
fill_value = 7  # Value to fill in the new array
new_array = np.full(new_shape, fill_value, dtype=int)
print("\nNew Array (filled with value 7):")
print(new_array)

zeros_array=np.zeros_like(new_array)
print("The array of Zeros",zeros_array)

ones_array=np.ones_like(new_array)
print("The array of ones",ones_array)

new_list = [1,2,3,4]
new_array=np.array(new_list)
print(new_array)

"""4.1.1 Problem - 2: Array Manipulation: Numerical Ranges and Array indexing:
Complete the following tasks:
1. Create an array with values ranging from 10 to 49. {Hint:np.arrange()}.
2. Create a 3X3 matrix with values ranging from 0 to 8.
{Hint:look for np.reshape()}
3. Create a 3X3 identity matrix.{Hint:np.eye()}
4. Create a random array of size 30 and find the mean of the array.
{Hint:check for np.random.random() and array.mean() function}
5. Create a 10X10 array with random values and find the minimum and maximum values.
6. Create a zero array of size 10 and replace 5th element with 1.
7. Reverse an array arr = [1,2,0,0,4,0].
8. Create a 2d array with 1 on border and 0 inside.
9. Create a 8X8 matrix and fill it with a checkerboard pattern.
"""

#1
array1=np.arange(10,49)
print(array1)

#2
g_array=np.arange(0,9)
reshaped=g_array.reshape(3,3)
print(reshaped)

#3
array2=np.eye(3);
print(array2)

#4
array3=np.random.random(30);
print("the array with the size 30 is:")
print(array3)
print("the mean of the aaray3 is:")
print(np.mean(array3))

#5
array4=np.random.random((10,10))
maxValue=np.max(array4);
minValue=np.min(array4);
print("The maximum value is:",maxValue)
print("The minimum value is:",minValue)

#6
array5=np.zeros(10)
array5[4]=1
print(array5)

#7
array6=np.array([1,2,0,0,4,0])
reversedArray=array6[::-1]
print("the reversed array is ",reversedArray)

#8
array7=np.ones((5,5))
array7[1:-1,1:-1]=0 #usually starts with 0 so 1 is second, -1 is a shortcut to mean "the last one."
print(array7)

#9
array8=np.zeros((8,8))
array8[::2,1::2]=1
array8[1::2,::2]=1
print(array8)

"""For the following arrays:
x = np.array([[1,2],[3,5]]) and y = np.array([[5,6],[7,8]]);
v = np.array([9,10]) and w = np.array([11,12]);
Complete all the task using numpy:
1. Add the two array.
2. Subtract the two array.
3. Multiply the array with any integers of your choice.
4. Find the square of each element of the array.
5. Find the dot product between: v(and)w ; x(and)v ; x(and)y.
6. Concatenate x(and)y along row and Concatenate v(and)w along column.
{Hint:try np.concatenate() or np.vstack() functions.
7. Concatenate x(and)v; if you get an error, observe and explain why did you get the error?
"""

x=np.array([[1,2],[3,5]])
y = np.array([[5,6],[7,8]])
v = np.array([9,10])
w = np.array([11,12])

#1
addingArray=x+y
print(addingArray)

#2
subtractingArray=x-y
print(subtractingArray)

#3
multiplyingArray=x*3
print(multiplyingArray)

#4
squareArray=x**2
print(squareArray)

#5
dotProduct1=np.dot(v,w)
dotProduct2=np.dot(x,v)
dotProduct3=np.dot(x,y)
print(dotProduct1)
print(dotProduct2)
print(dotProduct3)

#6
concat1=np.concatenate((x,y),axis=0) #0=rows
stack1=np.vstack((v,w))
print(concat1)
print(stack1)

#7
concat2=np.concatenate((x,v),axis=0)
print(concat2)

"""It returns value error because all the input array should have same number of dimension.

• For the following arrays:
A = np.array([[3,4],[7,8]]) and B = np.array([[5,3],[2,1]]);
Prove following with Numpy:
1. Prove A.A−1 = I.
2. Prove AB ̸= BA.
3. Prove (AB)

T = BTAT
.

• Solve the following system of Linear equation using Inverse Methods.

2x − 3y + z = −1
x − y + 2z = −3
3x + y − z = 9

{Hint: First use Numpy array to represent the equation in Matrix form. Then Solve for: AX = B}
• Now: solve the above equation using np.linalg.inv function.{Explore more about ”linalg” function
of Numpy}
"""

A = np.array([[3,4],[7,8]])
B = np.array([[5,3],[2,1]])
I=np.eye(2,2)
InvA=np.linalg.inv(A)
if(np.allclose(np.dot(A,InvA),I)):
    print("A.A^-1=I")

AB=np.dot(A,B)
BA=np.dot(B,A)
if(not np.array_equal(AB,BA)):
    print("AB!=BA")

TransposeAB=np.transpose(np.dot(A,B))
BtAt=np.dot(np.transpose(B),np.transpose(A))
if(np.array_equal(TransposeAB,BtAt)):
    print("T=BTAT")
else:
    print("T!=BTAT")

#2
A = np.array([[2, -3, 1], [1, -1, 2], [3, 1, -1]])
B = np.array([-1, -3, 9])
X = np.linalg.inv(A).dot(B)
print(f"X={X[0]},Y={X[1]},Z={X[2]}")