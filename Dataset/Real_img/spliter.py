# This script is used to generate two new .txt file from a train.txt file
# The idea is to read a .txt file that contains all the image data address locations and names
# and splits it into a train.txt and val.txt
# the split is random and we can decide the percentage of the split
# open the file and read how many lines are there in the file

import numpy as np
import random
import os
split_perc = 15

file = open("train.txt", "r")
x = file.readlines()
number_of_lines = len(x)
val_size = int((split_perc/100) * number_of_lines)
train_size = number_of_lines - val_size

print("Total number of Images : " + str(number_of_lines))
print("Split percentage : " + str(100 - split_perc) + ":" + str(split_perc) )
print("Number of training images : " + str(train_size))
print("Number of validation : " + str(val_size))

xtrain = open("xtrain.txt", "w")
xval = open("xval.txt", "w")

pool = np.linspace(0, number_of_lines -1, num=number_of_lines)
pool = [int(z) for z in pool]

val_pool = random.sample(pool, val_size)
train_pool = set(val_pool).symmetric_difference(pool)

## Writing the data of selected pool line to the .txt files
for a in val_pool:
    print("Writing to Validation test set: " + x[a])
    xval.write(x[a])
xval.close()

print("...................")
print("Write complete")

for a in train_pool:
    print("Writing to Training test set: " + x[a])
    xtrain.write(x[a])
xtrain.close()


print("...................")
print("Write complete")
print("Saving and Closing all files")


print("Total number of Images : " + str(number_of_lines))
print("Split percentage : " + str(100 - split_perc) + ":" + str(split_perc) )
print("Number of training images : " + str(train_size))
print("Number of validation : " + str(val_size))


file.close()
