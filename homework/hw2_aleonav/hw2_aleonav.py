# %%
#Leo Murch
#hw2
#09/09/2026

# %%
#imports needed here:
import numpy as np
import matplotlib.pyplot as plt

# %%
print('Problem 1:\nall parts w/in log\n')

# %%
print('Problem 2:\n')

print('a)')
x = np.arange(0, 1001) #up to 10001
print('Need to go up to element 1001, not inclusive to the second value w/ arrays\n')

#use type for the type, min(), max() for the min/max values
print(type(x), '\nmin value:',x.min(), '\nmax value:', x.max() )


print('\nb)')
#theres np.interp to normalize an array between values
x = np.interp(x, (x.min(), x.max()), (0, 2*np.pi))
print('min value:',x.min(), '\nmax value:', x.max() )


print('\nc)')
y = np.sin(x) #arrays, so this should just work

print('\nd)')
print(x[234]) #element 234, don't need 234+1(th) element

# %%
print('Problem 3:')

print('a)')
#i'll use the lecture slide as a reference to remember good plotting
plt.figure(figsize = (16, 9))
plt.plot(x, y, color = 'red', linewidth = 3)
plt.yticks(np.arange(-1, 1, 0.5), fontsize = 16) #to make the grid boxes even
plt.xticks(fontsize = 16)
plt.xlabel('x', fontsize = 20)
plt.ylabel('y', fontsize = 20)
plt.grid() #cause i like it

print('\nb)')
#use savefig() to save as png with the right name
plt.savefig("hw2_problem3_graph1.png")

# %%
print('Problem 4:')
print('a)')
#use linspace for evenly spaced elements
r = np.linspace(-1, 1, 101) #inclusive @ endpoints, can just put 1

#make an r clip to later snip so i can plot both
r_clip = np.linspace(-1, 1, 101)

#i think ill use np.where to clip it and assign them
r_clip[np.where(r_clip < -0.5)] = -0.5
r_clip[np.where(r_clip > 0.5)] = 0.5
#printing it and it looks like it worked!

print('\nb)')
#make a new fig to plot the two of them together
plt.figure(figsize = (10,8))

#i need to save the two to different variables to plot both on the same thing
plt.plot(r_clip)
plt.plot(r)

plt.savefig('hw2_problem4_graph1.pdf')

# %%
print('Problem 5:')
#im saving this and doing it later

#now i do it
"""Astropy:
A free package for python targeted for interpereting astro data. Contrains many useful objects
for data analysis  like astropy.: constants, units, time, modeling, uncertainty, and etc.
File I/O is also handled with image and table data, built in text tables and different extension handling.
Computational objects for cosmology, fitting, data analysis and more are included.
"""

"""Astroquery:
A package of astropy targeted for importing databases. Can [from astroquery.x import x] to
get major archives of astro data to return tables. Built upon Astropy for ease of use.
"""


# %%



