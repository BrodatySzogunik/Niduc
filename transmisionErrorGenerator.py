import random

def trasmisionErrorGenerator(array):
    zerosCounter = 0
    onesCount = 0
    indexForTrue =  0
    for i in range(0, len(array)):
        if array[i] == False:
            zerosCounter += 1;
        else:
            zerosCounter = 0

        if (zerosCounter == 8):
            onesCount = random.randint(0, 4)
            print(onesCount)
            while (onesCount > 0):
                indexForTrue = random.randint(0, len(array) - 1)
                if (array[indexForTrue] == False):
                    array[indexForTrue] = True
                    onesCount -= 1
            zerosCounter = 0



