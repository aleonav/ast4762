#! /usr/bin/env python3

# UCF AST5765/4762 HW3 Solutions
# Joseph Harrington <jh@physics.ucf.edu>
# ...with contributions from Kevin Stevenson
#update by TK for wrong call of functions and for F25 Qs

import numpy as np
import matplotlib.pyplot as plt
import astropy.io.fits as fits

plt.ion()

print("Solutions")
print("AST 5765")
print("HW 3_F25")

# === Problem 1 ===



print("=== Problem 2 ===")

# see homework directory for file square.py; example:
from hw3_support_func_sol import square

# Test square
print(square(np.arange(10)))
# git add hw3_sol.py
# git commit -m "Problem 1 done."

# === Problem 2 ===

print("=== Problem 3 ===")

from hw3_support_func_sol import squareplot
squareplot(1, 7, 5, savename='hw3_sol_prob2_graph1.png')



print("=== Problem 4 ===")

# 6. Copy of log file should be in HW dir.
