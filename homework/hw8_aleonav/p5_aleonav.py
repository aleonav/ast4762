# %%
#Leo Murch
#Practicum 5
#ast4762
#10/19/26

# %%
#import everything from hw7, hw6:
print("Problem 1")
from hw7_aleonav import *
from hw6_aleonav import *

# %%
#normmedcomb:
from numpy.linalg import norm


print("Problem 2")
def normmedcomb(data, corner_coords = None):
    """
    Median-combine a stack of dark-subtracted frames after normalizing each one.

    Each frame is divided by the median of its normalization region so frames
    with different sky levels can be combined. The input array is not modified.

    Parameters
    ----------
    3darr : array
        3D array of dark-subtracted sky flux, shaped (nframes, ny, nx).
    corner_coords : tuple of tuple, optional
        Corners of the region used to compute each frame's normalization
        factor, given as ((y1, x1), (y2, x2)). Defaults to the whole frame.

    Returns
    -------
    combined : array
        Normalized, median-combined 2D image.
    factors : array
        1D array of the normalization factor for each frame.

    Examples
    --------
    >>> combined, factors = normmedcomb(obj_darksub,
    ...                                 ((225, 225), (-225, -225)))
    >>> print(factors)
    [1.02 0.98 1.01 ...]

    >>> combined, factors = normmedcomb(obj_darksub)
    >>> combined.shape
    (1024, 1024)
    """
    
    #check to see if the corner_coords is given or not:
    if corner_coords is None:
        region = data #region is the whole array, not to modify the data
    else:
        (y1, x1), (y2, x2) = corner_coords #unpack the given tuple
        region = data[:, y1:y2, x1:x2] #all images, from y1-y2, and x1-x2 only is the region.

    norm_factor = np.median(region, axis=(1,2)) #to take the avg of the image, not along the actual # of images
    scaled_data = data / norm_factor[:, None, None] #axis = 0
    med_combined = np.median(scaled_data, axis = 0) #same as above along each image

    return med_combined, norm_factor

# %%
print('Problem 3')
#do this here since we didn't actually do it in hw6
objsubdark = objdata - dark_median
region = ((255, 255), (-255, -255))

#call function:
sky_mednorm, norm_factors = normmedcomb(objsubdark, region)

#write to a fits file:
fits.writeto('sky_13s_mednorm.fits', sky_mednorm)

#NOTE
#i didnt put an overwrite in this one, so just add:
#  overwrite = True
#if you wanna try to reproduce the data again yourself.


# %%
print(norm_factors)
#[10906. 11098. 10578. 10599. 11088. 10665.  9956.  9955.  9899.]


