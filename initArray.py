import random

def initArray(array,procentageOfOnes):

    percentageOfOnes = procentageOfOnes

    array.setall(False)

    iterationVar = ((len(array) * percentageOfOnes) / 100)

    while(iterationVar > 0):
        indexForOne = random.randint(0, len(array) - 1)
        if array[indexForOne] == False:
            array[indexForOne] = True
            iterationVar = iterationVar - 1

