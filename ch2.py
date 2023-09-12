# ------------------------------------------
# 2.2 The NumPy Module
# ------------------------------------------

import numpy as np

A = np.array( [[1,2], [3,4], [5,6]])
print(A)

print(A[:,0])
print(A[0,:])
print(type(A[:,0]))

a = np.array( [[1, 2, 3]] )
print(a.shape)



B = np.array( [[1,2], [3,4], [5,6]])
C = np.array( [[1,2], [3,4], [5,6]])
D = B * C
print (D)

