def bitErrorRatio(inputArray, outputArray):
    errorCounter = 0
    for i in range(0, len(inputArray)):
        if inputArray[i] != outputArray[i]:
            errorCounter += 1
    return errorCounter/len(inputArray)
