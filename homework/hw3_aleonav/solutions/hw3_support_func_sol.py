"""This file contains all support functions for hw3_F25
"""

#Remember that all libraries needed from your functions should be
#imported at the start:

import matplotlib.pyplot as plt
import numpy as np

# These abbreviated names are not to be used in docstrings; users must
# be able to paste and execute docstrings after importing only the
# numpy module itself, unabbreviated.

def square(x):
    '''
    Squares its argument.

    Parameters
    ----------
    x : array_like
    Value to be squared.

    Returns
    -------
    output : same type as x, possibly promoted
    The (elementwise) square of x.

    Examples
    --------
    >>> import numpy as np
    >>> import square
    >>> square(np.arange(10.))
    array([ 0., 1., 4., 9., 16., 25., 36., 49., 64., 81.])

    Revisions
    ---------
    2007-09-11 0.1 jh@physics.ucf.edu Initial version
    2007-10-28 0.2 jh@physics.ucf.edu Updated header
    2008-11-01 0.3 kevin218@knights.ucf.edu Updated docstring
    2009-09-15 0.4 jh@physics.ucf.edu Updated docstring
    2024-09-10 0.5 tkaralidi@ucf.edu Updated docstring
    '''
    return x**2

def squareplot(lo, hi, n, savename=False):
    '''
    Plots the squares of n points evenly distributed from lo to hi, inclusive.

    Parameters
    ----------
    lo : scalar
        The low end of the range.
    hi : scalar
        The high end of the range.
    n : int
        The number of points in the range.
    saveneme : string (optional)
        The filename to which to save the plot.  Not saved if False.

    Returns
    -------
    none

    Examples
    --------
    >>> import matplotlib.pyplot as plt
    >>> squareplot(0, 8, 5)
    >>> plt.show()

    Revisions
    ---------
    2007-09-11 0.1  jh@physics.ucf.edu        Initial version
    2007-11-23 0.2  jh@physics.ucf.edu        Removed (misplaced) figure write
    2008-11-01 0.3  kevin218@knights.ucf.edu  Updated docstring
    2009-09-16 0.4  jh@physics.ucf.edu        Updated docstring
                                              arange->linspace, code cleanup
    2011-09-16 0.5  jh@physics.ucf.edu	      Added doc for savename.
    2024-09-10      tkaralidi@ucf.edu         Updated docstring and wrong call to square
    '''

    # get numbers to square and square them
    x, step = np.linspace(lo, hi, n, retstep=True)
    y       = square(x)

    # plot them
    plt.plot(x, y, 'o')

    # pad the axes (this block optional for hw3, just demos axis padding)
    xaxpad = step/2
    yaxpad = square(np.array([x.min(),
                                   x.min() + step / 2]))
    yaxpad = yaxpad[1] - yaxpad[0]
    plt.axis([x.min() - xaxpad, x.max() + xaxpad,
            y.min() - yaxpad, y.max() + yaxpad])

    # words
    plt.xlabel('Input')
    plt.ylabel('Output')
    plt.title('Square Function')

    # save file
    if savename:
        plt.savefig(savename)

    return
