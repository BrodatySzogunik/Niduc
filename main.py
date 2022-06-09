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
from tests import runTests

def main():
    #mainData = bitarray(8192)

    #initArray(mainData, 50)

    #signal = mainData.copy()
    #trasmisionErrorGenerator(signal)
    #print('No scrambler BER:',bitErrorRatio(mainData,signal),'%')

    #mulScrambleSignal = mainData.copy()
    #MULScramble(mulScrambleSignal)
    #trasmisionErrorGenerator(mulScrambleSignal)
    #MULDescramble(mulScrambleSignal)
    #print('MULScrambler BER:',bitErrorRatio(mainData,mulScrambleSignal),'%')

    #xorScrambleSignal = mainData.copy()
    #key = XORKeyGenerator(0x27)
    #XORScrambler(xorScrambleSignal, key)
    #trasmisionErrorGenerator(xorScrambleSignal)
    #XORScrambler(xorScrambleSignal, key)
    #print('XORScrambler BER:',bitErrorRatio(mainData,xorScrambleSignal),'%')

    #notScrambleSignal = mainData.copy()
    #NOTScrambler(notScrambleSignal)
    #trasmisionErrorGenerator(notScrambleSignal)
    #NOTScrambler(notScrambleSignal)
    #print('NOTScrambler BER:',bitErrorRatio(mainData,notScrambleSignal),'%')

    data = None

    menu = {}
    menu['1'] = "Generate signal and display"
    menu['2'] = "Don't use any scrambler and show BER"
    menu['3'] = "Use MULScrambler.py and show BER"
    menu['4'] = "Use XORScrambler.py and show BER"
    menu['5'] = "Use NOTScrambler.py and show BER"
    menu['6'] = "Run tests and save to file"
    menu['0'] = "Exit"
    while True:
        options = menu.keys()
        for entry in options:
            print (entry, menu[entry])
        selection = input("Please Select:")
        if selection == '1':
            size = input("Insert size:")
            ones = input("Insert percentage of one [1-100]:")
            data = bitarray(int(size))
            initArray(data,int(ones))
            print('Generated signal:',data);
            os.system('pause')
        elif selection == '2':
            if not data:
                print('No signal generated! Cannot continue!')
                os.system('pause')
            else:
                signal = data.copy()
                trasmisionErrorGenerator(signal)
                print('No scrambler BER:',bitErrorRatio(data,signal),'%')
        elif selection == '3':
            if not data:
                print('No signal generated! Cannot continue!')
                os.system('pause')
            else:
                mulScrambleSignal = data.copy()
                MULScramble(mulScrambleSignal)
                trasmisionErrorGenerator(mulScrambleSignal)
                MULDescramble(mulScrambleSignal)
                print('MULScrambler BER:',bitErrorRatio(data,mulScrambleSignal),'%')
        elif selection == '4':
            if not data:
                print('No signal generated! Cannot continue!')
                os.system('pause')
            else:
                xorScrambleSignal = data.copy()
                key = XORKeyGenerator(0x27)
                XORScrambler(xorScrambleSignal, key)
                trasmisionErrorGenerator(xorScrambleSignal)
                XORScrambler(xorScrambleSignal, key)
                print('XORScrambler BER:',bitErrorRatio(data,xorScrambleSignal),'%')
        elif selection == '5':
            if not data:
                print('No signal generated! Cannot continue!')
                os.system('pause')
            else:
                notScrambleSignal = data.copy()
                NOTScrambler(notScrambleSignal)
                trasmisionErrorGenerator(notScrambleSignal)
                NOTScrambler(notScrambleSignal)
                print('NOTScrambler BER:',bitErrorRatio(data,notScrambleSignal),'%')
        elif selection == '6':
            runTests()
        elif selection == '0':
            break;
        else:
            print ("Unknown Option Selected!")

if __name__ == '__main__':
    main()