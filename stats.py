import sys
import ast
#----------------------------------------  Helper functions  -----------------------------------------------#
def openFile(fileName):
    try:
        file = open(fileName, "r")
    except IOError as e:
        sys.exit("IO Error has occured. Try again ... ")
    except Exception as e:
        sys.exit("Exception has occured " + e)
    return file

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

def hasFoundValueInDict(dictionnary, searchedElem):
    for k,v in dictionnary.items():
        if v == searchedElem : 
            return k
    return False

#---------------------------------------- Printing functions -----------------------------------------------#

def printStats(statistics):
    #TODO see how to print \n in uninterpreted mode
    print("Printing statistics : ")
    orderedKeysList = getListKeysOrderedByValue(statistics)
    orderedKeysList.reverse()
    for character in orderedKeysList:
        print(" \" ",character," \" ", " |  ",  statistics[character], end="\n")

def printEncoding(encoding):
    for key in sorted(encoding):
        print(key, " : ", encoding[key])

#-------------------------------- Huffman Encoding functions -----------------------------------------------#
def getStatistics(fileName):
    """ Takes a file in argument and returns statistics in the form of a dictionary"""
    file = openFile(fileName)
    statistics = {}
    while True:
        c = file.read(1)
        if not c :  break;
        if c in statistics :
            statistics[c] += 1
        else:
            statistics[c] = 1
    file.close()
    return statistics

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

def encodeFile(fileName, destinationFileName):    

    statistics = getStatistics(fileName)
    encoding = getCoding(statistics)
    #must put the encoding as the first line of the file
 
    file = openFile(fileName)
        
    destinationFile = open(destinationFileName, 'w')
    destinationFile.write(str(encoding) + "\n") 
    #TODO change this to binary

    while True:
        c = file.read(1)
        if c == "" : break
        for i in encoding[c] : 
            destinationFile.write(str(i)) 
    destinationFile.close()
    file.close()

def decodeFile(codedFileName, destinationFileName):
    codedFile = openFile(codedFileName)
    dictString = codedFile.readline().strip()
    encoding = dict(ast.literal_eval(dictString))
    destinationFile = open(destinationFileName, 'w')
    
    myList = []
    while True:
        try:
            number = int(codedFile.read(1))
        except ValueError:
            break
        except Exception as e :
            sys.exit(e)
            print(e)
        myList.append(number)
        foundChar = hasFoundValueInDict(encoding, myList)
        if foundChar:
            destinationFile.write(foundChar)
            myList[:] = []     
        
    codedFile.close()
    destinationFile.close()

def isEgal(fileName1, fileName2):
    file1=open(fileName1, 'r')
    textFile1 = file1.read()
    file2 = open(fileName2, 'r')
    textFile2 = file2.read()
    return textFile1 == textFile2
    
if __name__ == "__main__":
    
    #fileNameToEncode = "testHuffman.txt"
    #destinationFileName = fileToDecode ="destinationHuffman.txt"
    #decodedFileName = "huffmanDecoded.txt"
    
    fileNameToEncode = "loremIpsum.txt"
    destinationFileName = fileToDecode ="destinationLoremIpsum.txt"
    decodedFileName = "loremIpsumDecoded.txt"
    
    encodeFile(fileNameToEncode ,destinationFileName)
    decodeFile(fileToDecode, decodedFileName)
    
    if isEgal(fileNameToEncode, decodedFileName):
        print("Huffman encoding and decoding succesfully performed")
    else:
        print("Files are not equal")
