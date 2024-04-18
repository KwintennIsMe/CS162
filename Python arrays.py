#Pushed to repo "CS162"
import numpy as np
import random

array = np.random.randint(1, 10, size=(5,5), dtype=int)
print(array)
print(array[1][2])
print(np.sum(array))

#Print the mean of each row
print(np.mean(array, axis=1))

#Print the max of each column
print(np.max(array, axis=0))