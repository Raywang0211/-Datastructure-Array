
##Array
from array import array

a = array("I",[1,2,3])
print(a[1])
for i in a:
    print(i)

print("append")
for j in range(5):
    a.append(10+j)
print(a)

print("POP")
for j in range(len(a)):
    print(a.pop())

##numpy.array()
import numpy as np

a = np.array([1,2,3,4])
print(a)
a = np.full((5, 3), [1, 2,3])
print(a)

a = np.array([1,2,3,4])
b = np.insert(a,0,5)
print(a)
print(b)

a = np.array([[1,2],[3,4]])
b = np.insert(a,2,[5,6],axis=0)
print(a)
print(b)

a = np.array([1,2,3,4])
b = np.delete(a,2)
print(a)
print(b)

a = np.array([[1,2],[3,4],[5,6]])
b = np.delete(a,1,axis=0)
print(a)
print(b)

##List
a = [1,2,3,"a","abc",[55,66],["123","abc"]]
print(a[0])
print(a[3])
print(a[4][1])