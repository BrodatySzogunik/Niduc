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

def B8ZSDataGenerator(array, procentageOfOnes):
    ones = procentageOfOnes
    iterationVar = ((len(array) * ones) / 100)

    while(iterationVar > 0):
        indexForOne = random.randint(0, len(array) - 1)
        if array[indexForOne] == 0:
            array[indexForOne] = random.choice([1,-1])
            iterationVar = iterationVar - 1
    return array