# %%
#Leo Murch
#HW4
#09/21/26

# %%
import numpy as np
import matplotlib.pyplot as plt


# %%
print('Problem 2')
#a)
#use numpy.random.normal(mu, sigma, N)
mu = 55
sigma = 13
N = 10000
sample = np.random.normal(mu, sigma, N)

# %%
#b)
#bins 0-100 1 unit
x = np.arange(101)

#do the plotting:
plt.figsize = ((4, 3))
plt.hist(sample, x) #hist for histogram
plt.title('Histogram of a Gaussian')
plt.xlabel('x')
plt.ylabel('N(x)')
plt.savefig('hw4_problem2_graph1.png')

# %%
#c) #make a function for the gaussian
#need to take the center of the bins as stated,


bins = np.arange(0.5,100.5,1)
p_x = (1/(sigma * np.sqrt(2*np.pi)) * np.exp(-0.5 * ( (bins - mu) / sigma )**2))
#scale with the # of draws N as the problem says to properly align:
gauss = N * p_x
plt.hist(sample, x)
plt.plot(bins, gauss)
#looks p good to me
plt.savefig('hw4_problem2_graph2.png')


# %%
#skipping problem 3 for now to make sure i finish the base assignment first

#i think ill just submit it w/out 3, I gotta do essays for a scholarship this week
#so ima bit tight on time.


