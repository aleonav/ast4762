# %%
#Leo Murch
#HW3
#09/16/2026

# %%
import numpy as np
import matplotlib.pyplot as plt
import os

# %%
print("Problem 2")

#import by beautifully complex function
from hw3_aleonav_support_functions import square

#part h;
test_square_1 = np.array([0,1,2,3,4,5,6,7,8,9])
print(square(test_square_1))

#part i;
test_square_2 = np.linspace(0.0, 25.0, 25).reshape(5,5) #need 25 even spaces between for 26 elements
print(square(test_square_2))

# %%
print("Problem 3")

from hw3_aleonav_support_functions import squareplot

squareplot(1, 7, 5, saveplot='hw3_problem3_graph1.pdf')

# %%



