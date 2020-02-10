import numpy as np
<<<<<<< HEAD

def Myfunction(my_matrix, my_matrix2):
    try:
        return my_matrix * my_matrix2
    except ValueError:
        print("matrices are not aligned")
        return None

my_matrix = np.identity(4)

my_matrix2 = np.random.random(size=(4,5))


print(Myfunction(my_matrix, my_matrix2))
=======
import pandas as pd
my_matrix = np.identity(4)

my_matrix2 = np.random.random(size=(5,4))

print(my_matrix.dot(my_matrix2))
>>>>>>> master
