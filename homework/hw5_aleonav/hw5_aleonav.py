# %%
#Leo Murch
#AST4762
#Fall 2026
#Homework 5

# %%
import numpy as np
import matplotlib.pyplot as plt

# %%
#COPY PASTED CODE FROM 2B OF P3:

print("Problem 2")
#a)
#use np.random.poisson, random.uniform, and then assemble them togelther.
fish = np.random.poisson(10000, size = 396) #fish
unif = np.random.uniform(0, 1e6, size = 4) #importantly, not a fish (bad)

sample = np.concatenate([fish, unif]) #size 400 with the last 4 messed up
print(sample[-10:])

#mean and median of the sample:
print("Mean, Median of the sample is: ", np.mean(sample), np.median(sample))
#Median is def closer to N, at ~10000 while mean is like ~14500

#b) calc da stdev
sample_std = np.std(sample)
print("\nSample stdev: ", sample_std, "\n")

#do the masking of the data, from the L04 file:
clipped = sample[np.where(np.abs(sample - np.median(sample)) < 5 * np.sqrt(10000))] #clip where the sample is outside 5sigma
print("New samples data:\
\nMean: ", np.mean(clipped),
"\nMedian: ", np.median(clipped),
"\nStdev: ", np.std(clipped))

#now the mean and median line up to be much closer to each other, as well as the std going down signifigantly.
#Before there were very large outliers at the tail end up the data pulling the mean way higher (+ ~4500) from the median
#(which should be pretty closer to the median w/out outliers, since it follows a poisson dist.)

# %%
#okay i think i finally have a good function, let's see if it works
print('Problem 3')
from hw5_aleonav_support_functions import sigrej
#create a mask with the sample and tuple said before:
sigma_tup = (5.,5.)
mask = sigrej(sample, sigma_tup)
print(np.mean(sample[mask]))
#oh mah god it worked exactly the same as before

# %%



