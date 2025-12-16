#Write a function:
#`random_unit_vectors(num_vectors, dim)`
#that:
#a)creates a matrix M of shape (num_vectors, dim)using;
#M = np.random.randn(num_vectors, dim)
#b)normalizes each row so it has Euclidean norm 1,
#and c)returns the resulting matrix as a NumPy array.


import numpy as np

def random_unit_vectors(num_vectors, dim):
    M = np.random.randn(num_vectors, dim)
    
    l2 = np.linalg.norm(M, axis = 1,keepdims = True)
    
    M_norms = M / l2
    
    return M_norms
       


    
    
    
   
