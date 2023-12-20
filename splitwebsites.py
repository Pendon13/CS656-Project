import matplotlib.pyplot as plt
import os

def splitRunFile(dataFile):

    dataFile = open(dataFile, "r")

    dataLines = dataFile.readlines()
    for line in dataLines:
        line = line.strip("\n")
        line = line.split("; ")
        protocol = line[0]
        website = line[1]
        rtt = line[2]
        website = website.strip("http://")
        path = "./websites/"+website+"/"
        print(protocol)
        print(website)
        print(rtt)
        if not os.path.exists(path):
           os.makedirs(path)
        filepath = path + protocol + ".txt"
        file = open(filepath, "a")
        file.write(rtt + "\n")
        file.close()

def getAverages(dataFile):

    dataFile = open(dataFile, "r")

    dataLines = dataFile.readlines()
    for line in dataLines:
        line = line.strip("\n")
        line = line.split("; ")
        protocol = line[0]
        website = line[1]
        rtt = line[2]
        website = website.strip("http://")
        path = "./websites/average/"
        print(protocol)
        print(website)
        print(rtt)
        if not os.path.exists(path):
           os.makedirs(path)
        



        filepath = path + "average.txt"
        file = open(filepath, "a")
        file.write(rtt + "\n")
        file.close()

# splitRunFile("run1.txt")


