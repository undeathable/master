# Numpy notebook

d = {}
d['fish'] = 'wet'
print d['fish']
print d.get('fish', 'N/A')
try:
	print d['monkey']
except:
	print 'error!'
print d.get('monkey', 'N/A') #  Get an element with a default; prints "N/A"

'''
Numpy
It provides a high-performance multidimensional array object,
	and tools for working with these arrays.
'''

import numpy as np 

#------------------ Part 1 : Arrays ------------------------#
'''
Arrays is a grid of values of the same type.
The number of dimensions is the rank of the array.
the shape of an array is a tuple of integers giving the size of the array along each dimension
'''

'''
for arrays from lower dimensional to high dimensional : column -> row -> width -> ...
1d array: ([1, 2, 3, 4, ...]) -> 1 row n columns
2d array or matrix: ([[1, 2, 3, ...], [4, 5, 6, ...], ...]) -> n row & m columns
r2 = np.array([[1, 2, 3], [4, 5, 6]])
print r2.shape # consequence: row = 2, column = 3
3d array: ([[[1, 2, 3, ...], [4, 5, 6, ...], ...], [[7, 8, 9, ...], [10, 11, 12, ...], ...]])
r3 = np.array([[[1, 2, 3, 1], [4, 5, 6, 1], [0, 0, 0, 1]], [[7, 8, 9, 1], [10, 11, 12, 1], [0, 0, 0, 1]]])
print r3.shape # consequence: width:2 -> row: 3 -> column: 4
'''

a = np.array([1, 2, 3]) # Create a rank 1 array
print type(a)
print a.shape # the shape of an array is a tuple of integers giving the size of the array along each dimension
print [ele for ele in a]

b = np.array([[1, 2, 3], [4, 5, 6]])
print b.shape # row = 2, column = 3
print b[0, 0], b[0, 1], b[1, 0]

print np.array([[1,2.0],[0,0],(1+1j,3.)])

# Numpy also provides many functions to create arrays:
a = np.zeros((3, 2)) # create 3 rows and 2 columns
print a 
print a[2, 1] # the 0 on the last row and last column

b = np.ones((1, 2))
print b

c = np.full((2, 2), 7) # create a constant array
print c

d = np.eye(2) # create 2x2 identity matrix
print d

e = np.random.random((2, 2)) # Create an array filled with random values
print e

f = np.arange(10) # arange() will create arrays with regularly incrementing values.
print f

g = np.arange(2, 10, dtype = float)
print g

h = np.arange(2, 3, 0.1) # step is 0.1
print h

i = np.linspace(1., 4., 6) # create 6 points between 1 and 4 including 4
print i

j = np.indices((2, 4))
print j

#------------------ Part 1 : Array indexing ------------------------#
# Slicing
a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]) # create 3x4 matrix, 2 "[" means 2 d
b = a[:2, 1:3] # take row 0, row 1; column 1 and column2 -> 2 by 2 2d matrix
print b
print a[0, 1]

'''
Two ways of accessing the data in the middle row of the array.
Mixing integer indexing with slices yields an array of lower rank,
while using only slices yields an array of the same rank as the
original array:
'''
row_r1 = a[1, :] # Rank 1 view of the second row of a
row_r2 = a[1:2, :] # Rank 2 view of the second row of a
print row_r1, row_r1.shape
print row_r2, row_r2.shape

col_r1 = a[:, 1]
col_r2 = a[:, 1:2]
print col_r1, col_r1.shape
print col_r2, col_r2.shape


