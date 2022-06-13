POLYNOMIAL_INDEX1 = 2
POLYNOMIAL_INDEX2 = 8

def ADDScrambler(array):
    tempArray = array.copy();
    currentIndex = POLYNOMIAL_INDEX2
    while(currentIndex < len(array)):
        tempArray[currentIndex] = tempArray[currentIndex-POLYNOMIAL_INDEX1] ^ tempArray[currentIndex-POLYNOMIAL_INDEX2];
        array[currentIndex] = array[currentIndex] ^ (tempArray[currentIndex-POLYNOMIAL_INDEX1] ^ tempArray[currentIndex-POLYNOMIAL_INDEX2])
        currentIndex += 1
