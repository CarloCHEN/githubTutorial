import numpy as np

def Myfunction(my_matrix, my_matrix2):
    return my_matrix * my_matrix2

my_matrix = np.identity(4)

my_matrix2 = np.array(range(100))


print(Myfunction(my_matrix, my_matrix2))