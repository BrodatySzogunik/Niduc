def NOTScrambler(array):
    currentIndex = 0
    while(currentIndex < len(array)):
        if array[currentIndex] == False:
            array[currentIndex] = True
        else:
            array[currentIndex] = False
        currentIndex += 2;