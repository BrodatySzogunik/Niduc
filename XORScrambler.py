from bitarray.util import int2ba

def XORScrambler(array, scrambleKey):
    currentIndex = 0
    while(currentIndex < len(array)):
        array[currentIndex:(currentIndex+len(scrambleKey))] = array[currentIndex:(currentIndex+len(scrambleKey))] ^ scrambleKey
        currentIndex += len(scrambleKey)

def XORKeyGenerator(seed):
    generatedKey = seed

    generatedKey ^= generatedKey >> 3
    generatedKey ^= generatedKey << 2
    generatedKey ^= generatedKey >> 7
    return int2ba(generatedKey)