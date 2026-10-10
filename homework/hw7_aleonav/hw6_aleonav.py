# %%
#Leo Murch
#HW6 / Practicum 4
#Fall 2026

# %%
#do some imports:
import numpy as np
import astropy.io.fits as fits
import os

# %%
#Practicum Problem 2:
print('Problem 2')

#a)
#directory for where all of the data is within:
datadir = "hw6_data/"
#.fits extension
fext = ".fits"

# %%
#b)
#init the lists:
objfile = []
darkfile = []

#using the appropiate os command
for fname in os.listdir(datadir):
#two ifs to just see if it starts with 'dark' or 'stars' with the rdpharorcor
    if fname[:len('rdpharocor_dark')] == 'rdpharocor_dark':
        darkfile.append(fname[:-len(fext)]) #this is -5, but better practice to use the variable i think
    if fname[:len('rdpharocor_star')] == 'rdpharocor_star':
        objfile.append(fname[:-len(fext)]) 
#if it doesn't, just continue to go to go back and search through more
    else:
        continue

print(objfile, darkfile)
#if we want sorted:
objfile.sort()
darkfile.sort()
#i'll ask in class
#we do indeed sort them

# %%
#c)
#now i'll do the informative print statements:
print(f"\
Name of the data directory variable datadir: {datadir}\n\
Name of the file extension variable fext: {fext}\n\
The last elements of the lists are:\n\
objfile[-1]: {objfile[-1]}\n\
darkfile[-1]: {darkfile[-1]}")

# %%
#d) determining the sizes:
#i guess we just pick a random one that we want?
#need to use fits.getdata() to see the ny, nx
anyone = fits.getdata(datadir + objfile[3] + fext) #3 cause i like it
print(anyone.shape)

#returns the shape as 1024, 1024, so put both equal to that:
ny, nx = anyone.shape

# %%
#e) just the len() of each:
nobj = len(objfile)
ndark = len(darkfile)
#much more descriptive this way than just hardcoding them, better coding practice.

#informative print:
print(f"\
The number of rows and columns in each object file is {ny, nx} respectively.\n\
The number of files in each list:\n\
objfile size = {nobj}\n\
darkfile size = {ndark}")

# %%
print('Problem 3')
#a)
#init the two 3d arrays:
#i'll try the tab aligning for the data to easily see:
objdata =   np.zeros((nobj, ny, nx),    dtype = np.float64)
darkdata =  np.zeros((ndark, ny, nx),   dtype = np.float64)
print(f"\
Shapes of the two arrays:\n\
objdata has shape:\t{objdata.shape}\n\
darkdata has shape:\t{darkdata.shape}")

# %%
#b) populating the arrays:
from logging import raiseExceptions


for i in range(nobj):
    objdata[i,:,:] = fits.getdata(datadir +objfile[i] + fext) #'borrowed' method from in class
#get header outside for last:
objhead = fits.getheader(datadir + objfile[nobj-1] + fext)

#same for dark:
for i in range(ndark):
    darkdata[i,:,:] = fits.getdata(datadir +darkfile[i] + fext) #'borrowed' method from in class
#get header outside for last:
darkhead = fits.getheader(datadir + darkfile[ndark-1] + fext)

#still need to do the DATE-OBS for each
print("Date-OBS for objhead, darkhead:")
print(objhead['DATE-OBS'])
print(darkhead['DATE-OBS'])

# %%
#c) why not print TIME-OBS?
print(objhead['TIME-OBS'], darkhead["TIME-OBS"])
#there's nothing.
#Theyre blank for the images within the headers, apparently TIME-OBS is an older standard:
#https://listmgr.nrao.edu/pipermail/fitsbits/2002-January/001053.html
#found this on a mailing list, detailing the TIME vs DATE, to have a more combined
#standard for storing the date, and having FITS be modern and easier to parse by being combined.

# %%
#Leo Murch
#HW6 Part
#10/07/2026

# %%
print('Problem 2')
#a)
#using np.median along an axis (axis 0 for the n# of arrays) works

#b)
dark_median = np.median(darkdata, axis = 0)
print(f"Value of pixel index [217,184] of combined image is: {dark_median[217, 184]}")

# %%
#c) use .add_history() to append a HISTORY to the header
darkhead.add_history('Median-combined dark frame') #with what's specified in hw6

# %%
#d) make a new file dark_13s_med.fits and write this to it. 
#there's a function fits.writeto() to write data into a file name.
dark_median_fname = 'dark_13s_med'
fits.writeto(dark_median_fname + fext, dark_median, overwrite=True)
#this is a bit long but should work
fits.getheader(dark_median_fname + fext).add_history('Median-combined dark frame')

# %%
#e)
dark_sub_med = darkdata - dark_median #should be simple enough since theyre all arrays

#add to a file with .writeto() again,
fits.writeto("hw7_aleonav_prob2_graph1.fits", dark_sub_med[0], overwrite=True) #0th index for only the first file.

#printing the value of [217,184] both before and after:
print(f"The value of pixel [217,184] before and after subtraction:\n\
Before:\t{darkdata[0][217][184]}\n\
After:\t{dark_sub_med[0][217][184]}")
#makes sense, since the average is 19, and 24 - 19 = 5


