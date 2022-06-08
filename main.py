from bitarray import bitarray
from bitarray.util import int2ba

from MULScramble import MULScramble
from MULScramble import MULDescramble
from initArray import initArray
from bitErrorRatio import bitErrorRatio
from transmisionErrorGenerator import trasmisionErrorGenerator



mainData = bitarray(32)


mainData2 = bitarray(8)



initArray(mainData, 30)
initArray(mainData2,20)

# print(mainData)
# trasmisionErrorGenerator(mainData)
# print(mainData)
#
# print(mainData)
# MULScramble(mainData)
# trasmisionErrorGenerator(mainData)
# print(mainData)


def XORScramble(array, scrambleKey):
    currentIndex = 0
    while(currentIndex < len(array)):
        array[currentIndex:(currentIndex+len(scrambleKey))] = array[currentIndex:(currentIndex+len(scrambleKey))] ^ scrambleKey
        currentIndex += len(scrambleKey)

def XORShiftKeyGenerator(seed):
    generatedKey = seed

    generatedKey ^= generatedKey >> 3
    generatedKey ^= generatedKey << 2
    generatedKey ^= generatedKey >> 7
    # print(int2ba(generatedKey))
    return int2ba(generatedKey)




print(mainData)
XORScramble(mainData,XORShiftKeyGenerator(0X27))
print(mainData)
XORScramble(mainData,XORShiftKeyGenerator(0X27))
print(mainData)