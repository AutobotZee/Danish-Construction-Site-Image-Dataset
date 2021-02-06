# This script is used to generate a new .txt file from a train.txt file
# The idea is to check the test file to have same copy of images on training and test data

copy_counter = 0

file_train = open("web_train.txt", "r")
file_test = open("xval_web_1.txt", "r")
xtrain = open("xtrain_web_2.txt", "w")

x = file_train.readlines()
y = file_test.readlines()
number_of_lines = len(x)
val_size = len(y)

## Checking if the copy of ing train exists in test set .txt files
for i in x:
   ## print("Checking for copy of: " + i)
    copy_flag = False
    for j in y:
        if (i == j) and (i != '\n'):
            copy_counter += 1
            copy_flag = True
            break
        else:
            copy_flag = False

    if not copy_flag:
        xtrain.write(i)
    else:
        print("copy found, skipping the Image from training set:")
xtrain.close()
xtrain = open("excl_train.txt", "r")


z = xtrain.readlines()

print("...................")
print("Write complete")
print("Saving and Closing all files")


print("Total number of copy detected: " + str(copy_counter))
print("Total number of Validation images: " + str(val_size))

file_train.close()
file_test.close()
xtrain.close()
