import sys

""" Takes a file as argument """

fileName = "testfile.txt"

try:
    f = open(fileName, "r")
except IOError as e:
    sys.exit("IO Error has occured. Try again ... ")

words = {}

print(type(words))

while True:
    c = f.read(1)
    if not c :  break;
    if c in words :
        words[c] += 1
    else:
        words[c] = 1

print("Finished generating statistics")
    
f.close()

print("Printing statistics : ")

for character in words.keys():
    print(" \" ",character," \" ", " |  ",  words[character], end="\n")
    
    
