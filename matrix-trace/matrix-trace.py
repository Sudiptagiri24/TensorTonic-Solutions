import numpy as np

def matrix_trace(A):
    """
    Compute the trace of a square matrix (sum of diagonal elements).
    """
    # Write code here
    A = np.array(A)
    s= 0
    for i in range(0,A.shape[0]):
        s += A[i,i]
    return s
    
    
