POLYNOMIAL_INDEX1 = 2
POLYNOMIAL_INDEX2 = 8

def MULScramble(array):
    currentIndex = POLYNOMIAL_INDEX2
    while(currentIndex < len(array)):
        array[currentIndex] = array[currentIndex] ^ (array[currentIndex-POLYNOMIAL_INDEX1] ^ array[currentIndex-POLYNOMIAL_INDEX2])
        currentIndex += 1

def MULDescramble(array):
    currentIndex = POLYNOMIAL_INDEX2
    oldArray = array.copy()
    while(currentIndex < len(oldArray)):
        array[currentIndex] = oldArray[currentIndex] ^ (oldArray[currentIndex-POLYNOMIAL_INDEX1] ^ oldArray[currentIndex-POLYNOMIAL_INDEX2])
        currentIndex += 1
    return array
