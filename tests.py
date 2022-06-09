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

def runTests():
    if os.path.exists('results.txt'):
        os.remove('results.txt')

    print('Creating new bitarray of size 8192!')
    test = bitarray(8192)
    print('Filling 10% of signal with ones')
    initArray(test, 10)
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
    print('Saving results')
    with open('results.txt', 'x') as file:
        file.write('Result for size 8192 and 10% of ones:\n')
        file.write("No Scrambler average BER: " + str(signalBER / 10) + "\n")
        file.write("MULScrambler average BER: " + str(mulScramblerBER / 10) + "\n")
        file.write("XORScrambler average BER: " + str(xorScramblerBER / 10) + "\n")
        file.write("NOTScrambler average BER: " + str(notScramblerBER / 10) + "\n")
        file.write("\n")
    test.clear()

    print('Creating new bitarray of size 8192!')
    test = bitarray(8192)
    print('Filling 30% of signal with ones')
    initArray(test, 30)
    print('Testing algoritms!')
    signalBER = 0
    mulScramblerBER = 0
    xorScramblerBER = 0
    notScramblerBER = 0
    for i in range(0, 10):
        signal = test.copy()
        trasmisionErrorGenerator(signal)
        signalBER += bitErrorRatio(test, signal)

        mulScramblerSignal = test.copy()
        MULScramble(mulScramblerSignal)
        trasmisionErrorGenerator(mulScramblerSignal)
        MULDescramble(mulScramblerSignal)
        mulScramblerBER += bitErrorRatio(test, mulScramblerSignal)

        xorScramblerSignal = test.copy()
        key = XORKeyGenerator(0x27)
        XORScrambler(xorScramblerSignal, key)
        trasmisionErrorGenerator(xorScramblerSignal)
        XORScrambler(xorScramblerSignal, key)
        xorScramblerBER += bitErrorRatio(test, xorScramblerSignal)

        notScrambleSignal = test.copy()
        NOTScrambler(notScrambleSignal)
        trasmisionErrorGenerator(notScrambleSignal)
        NOTScrambler(notScrambleSignal)
        notScramblerBER += bitErrorRatio(test, notScrambleSignal)
    print('Saving results')
    with open('results.txt', 'a') as file:
        file.write('Result for size 8192 and 30% of ones:\n')
        file.write("No Scrambler average BER: " + str(signalBER / 10) + "\n")
        file.write("MULScrambler average BER: " + str(mulScramblerBER / 10) + "\n")
        file.write("XORScrambler average BER: " + str(xorScramblerBER / 10) + "\n")
        file.write("NOTScrambler average BER: " + str(notScramblerBER / 10) + "\n")
        file.write("\n")
    test.clear()

    print('Creating new bitarray of size 8192!')
    test = bitarray(8192)
    print('Filling 50% of signal with ones')
    initArray(test, 50)
    print('Testing algoritms!')
    signalBER = 0
    mulScramblerBER = 0
    xorScramblerBER = 0
    notScramblerBER = 0
    for i in range(0, 10):
        signal = test.copy()
        trasmisionErrorGenerator(signal)
        signalBER += bitErrorRatio(test, signal)

        mulScramblerSignal = test.copy()
        MULScramble(mulScramblerSignal)
        trasmisionErrorGenerator(mulScramblerSignal)
        MULDescramble(mulScramblerSignal)
        mulScramblerBER += bitErrorRatio(test, mulScramblerSignal)

        xorScramblerSignal = test.copy()
        key = XORKeyGenerator(0x27)
        XORScrambler(xorScramblerSignal, key)
        trasmisionErrorGenerator(xorScramblerSignal)
        XORScrambler(xorScramblerSignal, key)
        xorScramblerBER += bitErrorRatio(test, xorScramblerSignal)

        notScrambleSignal = test.copy()
        NOTScrambler(notScrambleSignal)
        trasmisionErrorGenerator(notScrambleSignal)
        NOTScrambler(notScrambleSignal)
        notScramblerBER += bitErrorRatio(test, notScrambleSignal)
    print('Saving results')
    with open('results.txt', 'a') as file:
        file.write('Result for size 8192 and 50% of ones:\n')
        file.write("No Scrambler average BER: " + str(signalBER / 10) + "\n")
        file.write("MULScrambler average BER: " + str(mulScramblerBER / 10) + "\n")
        file.write("XORScrambler average BER: " + str(xorScramblerBER / 10) + "\n")
        file.write("NOTScrambler average BER: " + str(notScramblerBER / 10) + "\n")
        file.write("\n")
    test.clear()

    print('Creating new bitarray of size 8192!')
    test = bitarray(8192)
    print('Filling 75% of signal with ones')
    initArray(test, 75)
    print('Testing algoritms!')
    signalBER = 0
    mulScramblerBER = 0
    xorScramblerBER = 0
    notScramblerBER = 0
    for i in range(0, 10):
        signal = test.copy()
        trasmisionErrorGenerator(signal)
        signalBER += bitErrorRatio(test, signal)

        mulScramblerSignal = test.copy()
        MULScramble(mulScramblerSignal)
        trasmisionErrorGenerator(mulScramblerSignal)
        MULDescramble(mulScramblerSignal)
        mulScramblerBER += bitErrorRatio(test, mulScramblerSignal)

        xorScramblerSignal = test.copy()
        key = XORKeyGenerator(0x27)
        XORScrambler(xorScramblerSignal, key)
        trasmisionErrorGenerator(xorScramblerSignal)
        XORScrambler(xorScramblerSignal, key)
        xorScramblerBER += bitErrorRatio(test, xorScramblerSignal)

        notScrambleSignal = test.copy()
        NOTScrambler(notScrambleSignal)
        trasmisionErrorGenerator(notScrambleSignal)
        NOTScrambler(notScrambleSignal)
        notScramblerBER += bitErrorRatio(test, notScrambleSignal)
    print('Saving results')
    with open('results.txt', 'a') as file:
        file.write('Result for size 8192 and 75% of ones:\n')
        file.write("No Scrambler average BER: " + str(signalBER / 10) + "\n")
        file.write("MULScrambler average BER: " + str(mulScramblerBER / 10) + "\n")
        file.write("XORScrambler average BER: " + str(xorScramblerBER / 10) + "\n")
        file.write("NOTScrambler average BER: " + str(notScramblerBER / 10) + "\n")
        file.write("\n")
    test.clear()

    print('Creating new bitarray of size 16384!')
    test = bitarray(16384)
    print('Filling 10% of signal with ones')
    initArray(test, 10)
    print('Testing algoritms!')
    signalBER = 0
    mulScramblerBER = 0
    xorScramblerBER = 0
    notScramblerBER = 0
    for i in range(0, 10):
        signal = test.copy()
        trasmisionErrorGenerator(signal)
        signalBER += bitErrorRatio(test, signal)

        mulScramblerSignal = test.copy()
        MULScramble(mulScramblerSignal)
        trasmisionErrorGenerator(mulScramblerSignal)
        MULDescramble(mulScramblerSignal)
        mulScramblerBER += bitErrorRatio(test, mulScramblerSignal)

        xorScramblerSignal = test.copy()
        key = XORKeyGenerator(0x27)
        XORScrambler(xorScramblerSignal, key)
        trasmisionErrorGenerator(xorScramblerSignal)
        XORScrambler(xorScramblerSignal, key)
        xorScramblerBER += bitErrorRatio(test, xorScramblerSignal)

        notScrambleSignal = test.copy()
        NOTScrambler(notScrambleSignal)
        trasmisionErrorGenerator(notScrambleSignal)
        NOTScrambler(notScrambleSignal)
        notScramblerBER += bitErrorRatio(test, notScrambleSignal)
    print('Saving results')
    with open('results.txt', 'a') as file:
        file.write('Result for size 16384 and 10% of ones:\n')
        file.write("No Scrambler average BER: " + str(signalBER / 10) + "\n")
        file.write("MULScrambler average BER: " + str(mulScramblerBER / 10) + "\n")
        file.write("XORScrambler average BER: " + str(xorScramblerBER / 10) + "\n")
        file.write("NOTScrambler average BER: " + str(notScramblerBER / 10) + "\n")
        file.write("\n")
    test.clear()

    print('Creating new bitarray of size 16384!')
    test = bitarray(16384)
    print('Filling 30% of signal with ones')
    initArray(test, 30)
    print('Testing algoritms!')
    signalBER = 0
    mulScramblerBER = 0
    xorScramblerBER = 0
    notScramblerBER = 0
    for i in range(0, 10):
        signal = test.copy()
        trasmisionErrorGenerator(signal)
        signalBER += bitErrorRatio(test, signal)

        mulScramblerSignal = test.copy()
        MULScramble(mulScramblerSignal)
        trasmisionErrorGenerator(mulScramblerSignal)
        MULDescramble(mulScramblerSignal)
        mulScramblerBER += bitErrorRatio(test, mulScramblerSignal)

        xorScramblerSignal = test.copy()
        key = XORKeyGenerator(0x27)
        XORScrambler(xorScramblerSignal, key)
        trasmisionErrorGenerator(xorScramblerSignal)
        XORScrambler(xorScramblerSignal, key)
        xorScramblerBER += bitErrorRatio(test, xorScramblerSignal)

        notScrambleSignal = test.copy()
        NOTScrambler(notScrambleSignal)
        trasmisionErrorGenerator(notScrambleSignal)
        NOTScrambler(notScrambleSignal)
        notScramblerBER += bitErrorRatio(test, notScrambleSignal)
    print('Saving results')
    with open('results.txt', 'a') as file:
        file.write('Result for size 16384 and 30% of ones:\n')
        file.write("No Scrambler average BER: " + str(signalBER / 10) + "\n")
        file.write("MULScrambler average BER: " + str(mulScramblerBER / 10) + "\n")
        file.write("XORScrambler average BER: " + str(xorScramblerBER / 10) + "\n")
        file.write("NOTScrambler average BER: " + str(notScramblerBER / 10) + "\n")
        file.write("\n")
    test.clear()

    print('Creating new bitarray of size 16384!')
    test = bitarray(16384)
    print('Filling 50% of signal with ones')
    initArray(test, 50)
    print('Testing algoritms!')
    signalBER = 0
    mulScramblerBER = 0
    xorScramblerBER = 0
    notScramblerBER = 0
    for i in range(0, 10):
        signal = test.copy()
        trasmisionErrorGenerator(signal)
        signalBER += bitErrorRatio(test, signal)

        mulScramblerSignal = test.copy()
        MULScramble(mulScramblerSignal)
        trasmisionErrorGenerator(mulScramblerSignal)
        MULDescramble(mulScramblerSignal)
        mulScramblerBER += bitErrorRatio(test, mulScramblerSignal)

        xorScramblerSignal = test.copy()
        key = XORKeyGenerator(0x27)
        XORScrambler(xorScramblerSignal, key)
        trasmisionErrorGenerator(xorScramblerSignal)
        XORScrambler(xorScramblerSignal, key)
        xorScramblerBER += bitErrorRatio(test, xorScramblerSignal)

        notScrambleSignal = test.copy()
        NOTScrambler(notScrambleSignal)
        trasmisionErrorGenerator(notScrambleSignal)
        NOTScrambler(notScrambleSignal)
        notScramblerBER += bitErrorRatio(test, notScrambleSignal)
    print('Saving results')
    with open('results.txt', 'a') as file:
        file.write('Result for size 16384 and 50% of ones:\n')
        file.write("No Scrambler average BER: " + str(signalBER / 10) + "\n")
        file.write("MULScrambler average BER: " + str(mulScramblerBER / 10) + "\n")
        file.write("XORScrambler average BER: " + str(xorScramblerBER / 10) + "\n")
        file.write("NOTScrambler average BER: " + str(notScramblerBER / 10) + "\n")
        file.write("\n")
    test.clear()

    print('Creating new bitarray of size 16384!')
    test = bitarray(16384)
    print('Filling 75% of signal with ones')
    initArray(test, 75)
    print('Testing algoritms!')
    signalBER = 0
    mulScramblerBER = 0
    xorScramblerBER = 0
    notScramblerBER = 0
    for i in range(0, 10):
        signal = test.copy()
        trasmisionErrorGenerator(signal)
        signalBER += bitErrorRatio(test, signal)

        mulScramblerSignal = test.copy()
        MULScramble(mulScramblerSignal)
        trasmisionErrorGenerator(mulScramblerSignal)
        MULDescramble(mulScramblerSignal)
        mulScramblerBER += bitErrorRatio(test, mulScramblerSignal)

        xorScramblerSignal = test.copy()
        key = XORKeyGenerator(0x27)
        XORScrambler(xorScramblerSignal, key)
        trasmisionErrorGenerator(xorScramblerSignal)
        XORScrambler(xorScramblerSignal, key)
        xorScramblerBER += bitErrorRatio(test, xorScramblerSignal)

        notScrambleSignal = test.copy()
        NOTScrambler(notScrambleSignal)
        trasmisionErrorGenerator(notScrambleSignal)
        NOTScrambler(notScrambleSignal)
        notScramblerBER += bitErrorRatio(test, notScrambleSignal)
    print('Saving results')
    with open('results.txt', 'a') as file:
        file.write('Result for size 16384 and 75% of ones:\n')
        file.write("No Scrambler average BER: " + str(signalBER / 10) + "\n")
        file.write("MULScrambler average BER: " + str(mulScramblerBER / 10) + "\n")
        file.write("XORScrambler average BER: " + str(xorScramblerBER / 10) + "\n")
        file.write("NOTScrambler average BER: " + str(notScramblerBER / 10) + "\n")
        file.write("\n")
    test.clear()

    print('Creating new bitarray of size 32768!')
    test = bitarray(32768)
    print('Filling 10% of signal with ones')
    initArray(test, 10)
    print('Testing algoritms!')
    signalBER = 0
    mulScramblerBER = 0
    xorScramblerBER = 0
    notScramblerBER = 0
    for i in range(0, 10):
        signal = test.copy()
        trasmisionErrorGenerator(signal)
        signalBER += bitErrorRatio(test, signal)

        mulScramblerSignal = test.copy()
        MULScramble(mulScramblerSignal)
        trasmisionErrorGenerator(mulScramblerSignal)
        MULDescramble(mulScramblerSignal)
        mulScramblerBER += bitErrorRatio(test, mulScramblerSignal)

        xorScramblerSignal = test.copy()
        key = XORKeyGenerator(0x27)
        XORScrambler(xorScramblerSignal, key)
        trasmisionErrorGenerator(xorScramblerSignal)
        XORScrambler(xorScramblerSignal, key)
        xorScramblerBER += bitErrorRatio(test, xorScramblerSignal)

        notScrambleSignal = test.copy()
        NOTScrambler(notScrambleSignal)
        trasmisionErrorGenerator(notScrambleSignal)
        NOTScrambler(notScrambleSignal)
        notScramblerBER += bitErrorRatio(test, notScrambleSignal)
    print('Saving results')
    with open('results.txt', 'a') as file:
        file.write('Result for size 32768 and 10% of ones:\n')
        file.write("No Scrambler average BER: " + str(signalBER / 10) + "\n")
        file.write("MULScrambler average BER: " + str(mulScramblerBER / 10) + "\n")
        file.write("XORScrambler average BER: " + str(xorScramblerBER / 10) + "\n")
        file.write("NOTScrambler average BER: " + str(notScramblerBER / 10) + "\n")
        file.write("\n")
    test.clear()

    print('Creating new bitarray of size 32768!')
    test = bitarray(32768)
    print('Filling 30% of signal with ones')
    initArray(test, 30)
    print('Testing algoritms!')
    signalBER = 0
    mulScramblerBER = 0
    xorScramblerBER = 0
    notScramblerBER = 0
    for i in range(0, 10):
        signal = test.copy()
        trasmisionErrorGenerator(signal)
        signalBER += bitErrorRatio(test, signal)

        mulScramblerSignal = test.copy()
        MULScramble(mulScramblerSignal)
        trasmisionErrorGenerator(mulScramblerSignal)
        MULDescramble(mulScramblerSignal)
        mulScramblerBER += bitErrorRatio(test, mulScramblerSignal)

        xorScramblerSignal = test.copy()
        key = XORKeyGenerator(0x27)
        XORScrambler(xorScramblerSignal, key)
        trasmisionErrorGenerator(xorScramblerSignal)
        XORScrambler(xorScramblerSignal, key)
        xorScramblerBER += bitErrorRatio(test, xorScramblerSignal)

        notScrambleSignal = test.copy()
        NOTScrambler(notScrambleSignal)
        trasmisionErrorGenerator(notScrambleSignal)
        NOTScrambler(notScrambleSignal)
        notScramblerBER += bitErrorRatio(test, notScrambleSignal)
    print('Saving results')
    with open('results.txt', 'a') as file:
        file.write('Result for size 32768 and 30% of ones:\n')
        file.write("No Scrambler average BER: " + str(signalBER / 10) + "\n")
        file.write("MULScrambler average BER: " + str(mulScramblerBER / 10) + "\n")
        file.write("XORScrambler average BER: " + str(xorScramblerBER / 10) + "\n")
        file.write("NOTScrambler average BER: " + str(notScramblerBER / 10) + "\n")
        file.write("\n")
    test.clear()

    print('Creating new bitarray of size 32768!')
    test = bitarray(32768)
    print('Filling 50% of signal with ones')
    initArray(test, 50)
    print('Testing algoritms!')
    signalBER = 0
    mulScramblerBER = 0
    xorScramblerBER = 0
    notScramblerBER = 0
    for i in range(0, 10):
        signal = test.copy()
        trasmisionErrorGenerator(signal)
        signalBER += bitErrorRatio(test, signal)

        mulScramblerSignal = test.copy()
        MULScramble(mulScramblerSignal)
        trasmisionErrorGenerator(mulScramblerSignal)
        MULDescramble(mulScramblerSignal)
        mulScramblerBER += bitErrorRatio(test, mulScramblerSignal)

        xorScramblerSignal = test.copy()
        key = XORKeyGenerator(0x27)
        XORScrambler(xorScramblerSignal, key)
        trasmisionErrorGenerator(xorScramblerSignal)
        XORScrambler(xorScramblerSignal, key)
        xorScramblerBER += bitErrorRatio(test, xorScramblerSignal)

        notScrambleSignal = test.copy()
        NOTScrambler(notScrambleSignal)
        trasmisionErrorGenerator(notScrambleSignal)
        NOTScrambler(notScrambleSignal)
        notScramblerBER += bitErrorRatio(test, notScrambleSignal)
    print('Saving results')
    with open('results.txt', 'a') as file:
        file.write('Result for size 32768 and 50% of ones:\n')
        file.write("No Scrambler average BER: " + str(signalBER / 10) + "\n")
        file.write("MULScrambler average BER: " + str(mulScramblerBER / 10) + "\n")
        file.write("XORScrambler average BER: " + str(xorScramblerBER / 10) + "\n")
        file.write("NOTScrambler average BER: " + str(notScramblerBER / 10) + "\n")
        file.write("\n")
    test.clear()

    print('Creating new bitarray of size 32768!')
    test = bitarray(32768)
    print('Filling 75% of signal with ones')
    initArray(test, 75)
    print('Testing algoritms!')
    signalBER = 0
    mulScramblerBER = 0
    xorScramblerBER = 0
    notScramblerBER = 0
    for i in range(0, 10):
        signal = test.copy()
        trasmisionErrorGenerator(signal)
        signalBER += bitErrorRatio(test, signal)

        mulScramblerSignal = test.copy()
        MULScramble(mulScramblerSignal)
        trasmisionErrorGenerator(mulScramblerSignal)
        MULDescramble(mulScramblerSignal)
        mulScramblerBER += bitErrorRatio(test, mulScramblerSignal)

        xorScramblerSignal = test.copy()
        key = XORKeyGenerator(0x27)
        XORScrambler(xorScramblerSignal, key)
        trasmisionErrorGenerator(xorScramblerSignal)
        XORScrambler(xorScramblerSignal, key)
        xorScramblerBER += bitErrorRatio(test, xorScramblerSignal)

        notScrambleSignal = test.copy()
        NOTScrambler(notScrambleSignal)
        trasmisionErrorGenerator(notScrambleSignal)
        NOTScrambler(notScrambleSignal)
        notScramblerBER += bitErrorRatio(test, notScrambleSignal)
    print('Saving results')
    with open('results.txt', 'a') as file:
        file.write('Result for size 32768 and 75% of ones:\n')
        file.write("No Scrambler average BER: " + str(signalBER / 10) + "\n")
        file.write("MULScrambler average BER: " + str(mulScramblerBER / 10) + "\n")
        file.write("XORScrambler average BER: " + str(xorScramblerBER / 10) + "\n")
        file.write("NOTScrambler average BER: " + str(notScramblerBER / 10) + "\n")
        file.write("\n")
    file.close()
    test.clear()