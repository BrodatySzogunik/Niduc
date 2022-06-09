import random

def trasmisionErrorGenerator(array):
    zerosCounter = 0
    for i in range(0, len(array)):
        if array[i] == False:
            zerosCounter += 1
        elif (array[i] == True or i == len(array)-1):
            if (zerosCounter >= 8):
                onesCount = random.randint(1, round(zerosCounter/2))
                # print(onesCount)
                while (onesCount > 0):
                    indexForTrue = random.randint(i - zerosCounter, i)
                    if (array[indexForTrue] == False):
                        array[indexForTrue] = True
                        onesCount -= 1
                zerosCounter = 0
            else:
                zerosCounter = 0