import sys

""" Takes a file as argument """

def getStatistics(File):
    """ Takes a file in argument and returns statistics in the form of a dictionary"""
    statistics = {}
    while True:
        c = f.read(1)
        if not c :  break;
        if c in statistics :
            statistics[c] += 1
        else:
            statistics[c] = 1
    
    f.close()
    print("Finished generating statistics.")
    return statistics

def printStats(statistics):
    #TODO see how to print \n for exaample
    print("Printing statistics : ")
    
    orderedKeysList = getListKeysOrderedByValue(statistics)
    orderedKeysList.reverse()
    for character in orderedKeysList:
        print(" \" ",character," \" ", " |  ",  statistics[character], end="\n")

def printEncoding(encoding):
    for key in sorted(encoding):
        print(key, " : ", encoding[key])


def getCoding(statistics):
    """ Takes a dictionary of statistics, returns a dictionary of encodings """
    if type(statistics) != dict : raise ValueError
    #Make new dictionary to return with encoding
    encoding = {}
    
    while True:
        if len(statistics) <= 1 : break;
    
        listKeys = getListKeysOrderedByValue(statistics)

            # a, b, c 
            # keys[0] is the smallest key

        encoding = updateDictionaryCoding(encoding,listKeys[0],0)
        encoding = updateDictionaryCoding(encoding,listKeys[1],1)
        

        charactersTupple = tuple(listKeys[0]) + tuple (listKeys[1])
        #add new tupple
    
        statistics[charactersTupple] = statistics[listKeys[0]]+statistics[listKeys[1]]
    
        del statistics[listKeys[0]]
        del statistics[listKeys[1]]

    return encoding

def getListKeysOrderedByValue(dictionnary):
    """ Returns a list of ordered keys of a dictionary by values """
    if type(dictionnary) != dict : raise ValueError
    keys = dictionnary.keys()
    keys = list(keys)
    keys = sorted(keys, key=lambda value: dictionnary[value])
    return keys

def updateDictionaryCoding(dictionary, key, value):
    """ Udates the dictionary with the new 0 or 1 value at the end of a character """
    if type(key) == tuple:
        for i in key :
            dictionary[i].insert(0,value)
    else:
        if key in dictionary:
            dictionary[key].insert(0,value);
        else:
            dictionary[key] = list()
            dictionary[key].insert(0,value)
    return dictionary

if __name__ == "__main__":

    fileName = "testHuffman.txt"

    try:
        f = open(fileName, "r")
    except IOError as e:
        sys.exit("IO Error has occured. Try again ... ")
    except Exception as e:
        sys.exit("Exception has occured " + e)

    statistics = getStatistics(f)
    printStats(statistics)
    print("______________________________________________________________________________________________________________________________________________________")
    encoding = getCoding(statistics)
    printEncoding(encoding)
