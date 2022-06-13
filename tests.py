import os

from bitarray import bitarray

from initArray import *
from bitErrorRatio import *
from transmisionErrorGenerator import *
from ADDScrambler import *
from MULScrambler import *
from XORScrambler import *
from NOTScrambler import *
from B8ZSScrambler import *

def singleTest(size, percentage):
    print('Creating new bitarray of size ' + str(size) + '!')
    test = bitarray(size)
    testB8ZS = [0] * int(size)
    print('Filling ' + str(percentage) + '% of signal with ones!')
    initArray(test, percentage)
    B8ZSDataGenerator(testB8ZS,percentage)
    print('Testing algoritms!')
    signalBER = 0
    addScramblerBER = 0
    mulScramblerBER = 0
    xorScramblerBER = 0
    notScramblerBER = 0
    b8zsScramblerBER = 0

    for i in range (0,10):
        signal = test.copy()
        trasmisionErrorGenerator(signal)
        signalBER += bitErrorRatio(test,signal)

        addScramblerSignal = test.copy()
        ADDScrambler(addScramblerSignal)
        trasmisionErrorGenerator(addScramblerSignal)
        ADDScrambler(addScramblerSignal)
        addScramblerBER += bitErrorRatio(test, addScramblerSignal)

        mulScramblerSignal = test.copy()
        MULScrambler(mulScramblerSignal)
        trasmisionErrorGenerator(mulScramblerSignal)
        MULDescrambler(mulScramblerSignal)
        mulScramblerBER += bitErrorRatio(test,mulScramblerSignal)

        xorScramblerSignal = test.copy()
        key = XORKeyGenerator(0x27)
        XORScrambler(xorScramblerSignal, key)
        trasmisionErrorGenerator(xorScramblerSignal)
        XORScrambler(xorScramblerSignal, key)
        xorScramblerBER += bitErrorRatio(test,xorScramblerSignal)

        notScrambleSignal = test.copy()
        NOTScrambler(notScrambleSignal)
        trasmisionErrorGenerator(notScrambleSignal)
        NOTScrambler(notScrambleSignal)
        notScramblerBER += bitErrorRatio(test,notScrambleSignal)

        B8ZSScrambleSignal = testB8ZS.copy()
        testB8ZS = B8ZSScrambler(testB8ZS,1)
        testB8ZS = trasmisionErrorGeneratorForB8(testB8ZS)
        testB8ZS = B8ZSDescrambler(testB8ZS)

        b8zsScramblerBER += bitErrorRatio(B8ZSScrambleSignal,testB8ZS)


    print('Saving results\n')
    with open('results.txt', 'a') as file:
        file.write('Result for size ' + str(size) + ' and ' + str(percentage) + '% of ones:\n')
        file.write("No Scrambler average BER: " + str(signalBER / 10) + "\n")
        file.write("ADDScrambler average BER: " + str(addScramblerBER / 10) + "\n")
        file.write("MULScrambler average BER: " + str(mulScramblerBER / 10) + "\n")
        file.write("XORScrambler average BER: " + str(xorScramblerBER / 10) + "\n")
        file.write("NOTScrambler average BER: " + str(notScramblerBER / 10) + "\n")
        file.write("B8ZSScrambler average BER: " + str(b8zsScramblerBER / 10) + "\n")
        file.write("\n")
    test.clear()

def runTests():
    if os.path.exists('results.txt'):
        os.remove('results.txt')
    singleTest(8192, 10)
    singleTest(8192, 20)
    singleTest(8192, 30)
    singleTest(8192, 40)
    singleTest(8192, 50)
    singleTest(8192, 60)
    singleTest(8192, 70)
    singleTest(8192, 80)
    singleTest(8192, 90)
    singleTest(16384, 10)
    singleTest(16384, 20)
    singleTest(16384, 30)
    singleTest(16384, 40)
    singleTest(16384, 50)
    singleTest(16384, 60)
    singleTest(16384, 70)
    singleTest(16384, 80)
    singleTest(16384, 90)
    singleTest(32768, 10)
    singleTest(32768, 20)
    singleTest(32768, 30)
    singleTest(32768, 40)
    singleTest(32768, 50)
    singleTest(32768, 60)
    singleTest(32768, 70)
    singleTest(32768, 80)
    singleTest(32768, 90)
