import numpy as np
import pandas as pd
my_matrix = np.identity(4)

my_matrix2 = np.random.random(size=(5,4))

print(my_matrix.dot(my_matrix2))