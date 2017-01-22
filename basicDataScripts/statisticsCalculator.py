
from collections import Counter
import sys

def calculateMean(list):
    return sum(list) / len(list)
def calculateMedian(list):
    if len(list) % 2 == 0:
        position1 = len(list) / 2
        position2 = (len(list)/2) + 1
        position1 = int(position1) - 1
        position2 = int(position2) - 1
        return (list[position1] + list[position2])/2
    else:
        position = (len(list)+1) / 2
        position = int(position) - 1
        return list[position]
def calculateMode(list):
    c = Counter(list)
    numberFreq = c.most_common()
    maxNumber = numberFreq[0][1]

    modes = []
    for i in numberFreq:
        if i[1] == maxNumber:
            modes.append(i[0])
    return modes
def findDifference(list):
    mean = calculateMean(list)
    diff = []
    for num in list:
        diff.append(num-mean)
    return diff
def calculateVariance(list):
    diff = findDifference(list)
    squareDiff = []
    for i1 in diff:
        squaredDifference = i1**2
        squareDiff.append(squaredDifference)
    numerator = sum(squareDiff)
    return numerator / len(list)

def calculateStandardDeviation(list):
    variance = calculateVariance(list)
    return variance ** 0.5
print("          ------Statistics Calculator------\n")
file = input("Enter filename if available, otherwise enter 0: ")
if file != "0":
    lineList = []
    with open(file) as f:
        for line in f:
            lineList.append(float(line))
    print("\nMean:            %r" % calculateMean(lineList))
    print("\nMedian:          %r" % calculateMedian(lineList))
    print("\nMode:            %r" % calculateMode(lineList))
    print("\nVariance:        %r" % calculateVariance(lineList))
    print("\nStd Deviation:   %r" % calculateStandardDeviation(lineList))
else:
    g = 0
    while g != "-1":
        print("\n(1) - Mean\n(2) - Median\n(3) - Mode\n(4) - Variance\n(5) - Standard Deviation\n")
        g = input("Choose statistic calculation with a number, enter -1 to quit: ")
        if g == "-1":
            sys.exit(0)
        userListing = 0; userList = []
        while userListing != -1:
            userListing = float(input("Enter list number (Only one number, enter -1 to stop): "))
            if userListing != -1:
                userList.append(userListing)

        if g == "1":
            print("Mean:            %r" % calculateMean(userList))
        elif g == "2":
            print("Median:          %r" % calculateMedian(userList))
        elif g == "3":
            print("Mode:            %r" % calculateMode(userList))
        elif g == "4":
            print("Variance:        %r" % calculateVariance(userList))
        elif g == "5":
            print("Std Deviation:   %r" % calculateStandardDeviation(userList))