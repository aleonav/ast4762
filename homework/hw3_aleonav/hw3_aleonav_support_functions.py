"""Returns the square of the inputted variable that is type of
array_like, scalar (int, float, double, etc)
by using python's built in [x]**2 opperator.
"""

import os 
import numpy as np
import scipy as sp
import matplotlib as mpl
import matplotlib.pyplot as plt 
import astropy.io.fits as fits

def square(var1) :
    #this is our function's docstring!
    """Takes a scalar / array input and returns its square.

    Takes as input a scalar / array of any dimension or numerical type, and uses the built in **2
    to return its square.

    Parameters
    ----------
    var1 : array_like / scalar (int, float, double, etc)

    Returns
    -------
    output : array_like / scalar (int, float, double, etc)
        var1**2 of the input, var1. Matches its initial variable type.


    See Also
    --------
    ** : built in python square notation.
    np.square() : Numpy's square function
    math.pow(): math's power function, for math.pow(var1, 2)

    Notes
    -----
    Uses the simple built in python function to return var1**2, the square value of var1.

    Examples
    --------
    >>> var1 = np.array([1, 2, 3, 4])
    >>> var1_sq = square(var1)
    >>> print(var1_sq)
    [1, 4, 9, 16]

    >>> var2 = 3
    >>> var2_sq = square(var2)
    >>> print(var2_sq)
    9

    >>> var3 = 3.3
    >>> var3_sq = square(var3)
    >>> print(var3_sq)
    10.889999999999999

    Revisions
    ---------
    2026-09-15: Created square in it's current form
    """

    #square and return var1, no pass needed since it does something.
    return var1 **2

