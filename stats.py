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
    for character in statistics.keys():
        print(" \" ",character," \" ", " |  ",  statistics[character], end="\n")

if __name__ == "__main__":

    fileName = "testfile.txt"

    try:
        f = open(fileName, "r")
    except IOError as e:
        sys.exit("IO Error has occured. Try again ... ")
    except Exception as e:
        sys.exit("Exception has occured " + e)

    statistics = getStatistics(f)
    printStats(statistics)
