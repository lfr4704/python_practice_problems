def allMissing(inputArray, missingNo):
    b = [x for x in range(inputArray[0], len(inputArray) + missingNo + 1)]
    a = set(inputArray)
    print(list(a ^ set(b)))

# Driving code
inputArray = [1, 5, 7, 4, 8, 3]
inputArray2 = [1, 3, 4, 6]
allMissing(inputArray, 2)
