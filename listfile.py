import os

print ("the files n folders in {} are ".format(os.getcwd()))
items = os.listdir('.')
for item in items:
    print (item)