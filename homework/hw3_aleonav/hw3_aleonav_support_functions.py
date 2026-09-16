"""Returns the square of the inputted variable that is type of
array_like, scalar (int, float, double, etc)
by using python's built in [x]**2 opperator.
"""

import os 
import numpy as np
import matplotlib.pyplot as plt 

def square(var1):
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
    [1 4 9 16]

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

def squareplot(low_end, high_end, n_points, saveplot=False):
    """Plots the squares of evenly spaced numbers over a given range.

    Takes as input the low and high ends of a range (high end inclusive) and
    the number of points to plot. Builds an evenly spaced array x, calls
    square() once to get y = x**2, and plots y vs x. 
    If saveplot is not False,
    saves the figure to the filename given by saveplot.

    Parameters
    ----------
    low_end : scalar (int, float, double, etc)
        Low end of the range to plot.
    high_end : scalar (int, float, double, etc)
        High end of the range to plot. Inclusive.
    n_points : int
        Number of evenly spaced points from low_end to high_end, inclusive.
    saveplot : bool or str, optional
        If False (default), do not save the plot. If a string, save the plot
        as a PDF using that filename. Filename is not hardcoded.

    Returns
    -------
    None
        Displays (and optionally saves) a plot.

    See Also
    --------
    square : Function that returns the square of a scalar / array.
    np.linspace() : Numpy's evenly spaced array function.
    plt.plot() : Matplotlib's plot function.
    plt.savefig() : Matplotlib's save figure function.

    Notes
    -----
    Uses np.linspace to create x from low_end to high_end (inclusive) with
    n_points points, then calls square(x) exactly once to get y. The plot
    is labeled "Input" on the x-axis, "Output" on the y-axis, and titled
    "Square Function".

    Examples
    --------
    >>> squareplot(1, 7, 5)
    #plots the squares of 1, 2.5, 4, 5.5, and 7

    >>> squareplot(1, 7, 5, saveplot='squareplot_1to7.pdf')
    #same plot, saved to squareplot_1to7.pdf

    Revisions
    ---------
    2026-09-15: Created squareplot in its current form
    2026-09-15: changed plt.plot() to plt.scatter() to plot points
    instead of an interpolated line.
    """

    #linespace makes an inclusive spaced out array
    x = np.linspace(low_end, high_end, n_points)

    #call square to get the square of this array x
    y = square(x)

    #plot y/x
    plt.scatter(x,y)
    plt.xlabel('Input')
    plt.ylabel('Output')
    plt.title('Square Function')

    #do an ifstate to see if the saveplot variable is false or not
    if saveplot is not False: plt.savefig(saveplot)

    #show the plot regardless
    plt.show()

    pass