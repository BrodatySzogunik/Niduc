import os

from bitarray import bitarray

from initArray import initArray
from bitErrorRatio import bitErrorRatio
from transmisionErrorGenerator import trasmisionErrorGenerator
from MULScrambler import MULScramble
from MULScrambler import MULDescramble
from XORScrambler import XORScrambler
from XORScrambler import XORKeyGenerator
from NOTScrambler import NOTScrambler

def singleTest(size, percentage):
    print('Creating new bitarray of size ' + str(size) + '!')
    test = bitarray(size)
    print('Filling ' + str(percentage) + '% of signal with ones!')
    initArray(test, percentage)
    print('Testing algoritms!')
    signalBER = 0
    mulScramblerBER = 0
    xorScramblerBER = 0
    notScramblerBER = 0
    for i in range (0,10):
        signal = test.copy()
        trasmisionErrorGenerator(signal)
        signalBER += bitErrorRatio(test,signal)

        mulScramblerSignal = test.copy()
        MULScramble(mulScramblerSignal)
        trasmisionErrorGenerator(mulScramblerSignal)
        MULDescramble(mulScramblerSignal)
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
    print('Saving results\n')
    with open('results.txt', 'a') as file:
        file.write('Result for size ' + str(size) + ' and ' + str(percentage) + '% of ones:\n')
        file.write("No Scrambler average BER: " + str(signalBER / 10) + "\n")
        file.write("MULScrambler average BER: " + str(mulScramblerBER / 10) + "\n")
        file.write("XORScrambler average BER: " + str(xorScramblerBER / 10) + "\n")
        file.write("NOTScrambler average BER: " + str(notScramblerBER / 10) + "\n")
        file.write("\n")
    test.clear()

def runTests():
    if os.path.exists('results.txt'):
        os.remove('results.txt')
    singleTest(8192, 10)
    singleTest(8192, 30)
    singleTest(8192, 50)
    singleTest(8192, 75)
    singleTest(16384, 10)
    singleTest(16384, 30)
    singleTest(16384, 50)
    singleTest(16384, 75)
    singleTest(32768, 10)
    singleTest(32768, 30)
    singleTest(32768, 50)
    singleTest(32768, 75)