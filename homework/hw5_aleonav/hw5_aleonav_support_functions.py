"""
Carries out sigma rejection with specified sigma values and masking.
"""

import numpy as np

def sigrej(data, sigmas, mask=None):
    '''
    Reject outliers by iterative sigma clipping and return an updated mask.

    Each value in sigmas is one clipping pass.  Points farther than that
    many standard deviations from the mean of the currently good data
    are flagged bad.

    Parameters
    ----------
    data: ndarray
        Measurements to clip, any shape.
    sigmas: tuple of float
        Rejection limits, one per iteration.  Two 5-sigma passes are
        (5., 5.).
    mask: ndarray or None
        Boolean mask with the same shape as data.  True is good and
        False is bad.  If None, every point starts good.  Use this to
        mark points that were already bad, for example a faulty detector
        pixel or a cosmic-ray hit.

    Returns
    -------
    mask: ndarray
        Boolean mask, same shape as data.  True is still good and False
        is bad.  Points that fail a rejection limit are set to False.
        Points that started False stay False.

    Notes
    -----
    Only points that are True in the current mask enter the mean and
    standard deviation.  After each pass the mask is updated, and the
    next limit in sigmas is applied to the points that remain.

    Do not use numpy.ma.

    See Also
    --------
    astropy.stats.sigma_clip

    Examples
    --------
    >>> data = np.concatenate([np.random.poisson(10000, 396),
    ...                         np.random.unfiform.uniform(0, 1e6, 4)])
    >>> mask = sigrej(data, (5., 5.))
    >>> data[mask].mean()
    10011.689393939394
    '''
    
    #returning what sample[np.where()] part of the indecies, not the array itself for this
    #have to check to see if the mask bool array is provided first:

    if mask is None: #make a dummy array where all are True, (1 values)
        mask = np.ones(np.shape(data), dtype = bool)
    
    #i think ill add a return by modifying the sigma by calling it again to just do two passes
    if len(sigmas) == 0:
        return mask

    #if not the case, it's provided.
    good = data[np.where(mask)] #'good' points
    mean = np.mean(good) #dont rely off median like hw5, since taking the good values
    std = np.std(good)
    nsig = sigmas[0] #this is the 1st run, the second run will return the [1] indices,
    #and then the len will be 0.
    mask[np.where(np.abs(data - mean) > nsig * std)] = False #same method as hw5, but the opposite for False,
    #returning where it's greater than to modify the mask.

    return sigrej(data, sigmas[1:], mask) #this should save me more code for searching through the length,
    #i just keep returning for each pass until the len(sigmas) is 0, which makes it return that correct mask.

    #if this doesn't work then you won't see any of it lol