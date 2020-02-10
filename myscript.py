import numpy as np

def Myfunction(my_matrix, my_matrix2):
    try:
        return my_matrix * my_matrix2
    except ValueError:
        print("matrices are not aligned")
        return None

my_matrix = np.identity(4)

my_matrix2 = np.random.random(size=(4,5))


print(Myfunction(my_matrix, my_matrix2))