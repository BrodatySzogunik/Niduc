import random

def B8ZSScrambler(array, lastSymbol):
    consecZero = 0
    table = {
        "1": [0, 0, 0, 1, -1, 0, -1, 1],
        "-1": [0, 0, 0, -1, 1, 0, 1, -1]
    }

    for i in range(0,len(array)):
        if array[i] == 1:
            lastSymbol = 1
            consecZero = 0

        elif array[i] == -1:
            lastSymbol = -1
            consecZero = 0

        elif array[i] == 0:
            consecZero += 1

            if consecZero == 8:
                array = array[0:i - 7] + table[str(lastSymbol)] + array[i + 1:]
                consecZero = 0
    return array

def B8ZSDescrambler(array):
    for i in range(5,len(array)):
        if (array[i-1] == 1 and array[i-2] == 0 and array[i-3] == 1) or (array[i-1] == -1 and array[i-2] == 0 and array[i-3] == -1):
            array[i] = 0
            array[i-1] = 0
            array[i-3] = 0
            array[i-4] = 0
    return array

def B8ZSDataGenerator(array, procentageOfOnes):

    iterationVar = ((len(array) * procentageOfOnes) / 100)

    while (iterationVar > 0):
        indexForOne = random.randint(0, len(array) - 1)
        if array[indexForOne] == 0:
            array[indexForOne] = 1
            iterationVar = iterationVar - 1

    lastValue=-1
    for i in range(0,len(array)):
        if array[i] == 1:
            if lastValue == -1:
                array[i] = 1
                lastValue = 1
            else:
                array[i] = -1
                lastValue = -1
    return array

def trasmisionErrorGeneratorForB8(array):
    zerosCounter = 0
    for i in range(0, len(array)):
        if array[i] == 0:
            zerosCounter += 1
        elif (array[i] == 1 or array[i] == -1 or i == len(array)-1):
            if (zerosCounter >= 8):
                onesCount = random.randint(1, round(zerosCounter/2))
                # print(onesCount)
                while (onesCount > 0):
                    indexForTrue = random.randint(i - zerosCounter, i)
                    if (array[indexForTrue] == 0):
                        array[indexForTrue] = 1
                        onesCount -= 1
                zerosCounter = 0
            else:
                zerosCounter = 0
    return array