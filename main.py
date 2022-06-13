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
from tests import runTests

def main():
    data = None
    dataB8ZS = None

    menu = {}
    menu['1'] = "Generate signal and display"
    menu['2'] = "Don't use any scrambler and show BER"
    menu['3'] = "Use ADDScrambler.py and show BER"
    menu['4'] = "Use MULScrambler.py and show BER"
    menu['5'] = "Use XORScrambler.py and show BER"
    menu['6'] = "Use NOTScrambler.py and show BER"
    menu['7'] = "Use B8ZSScrambler.py and show BER"
    menu['8'] = "Run tests and save to file"
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
            print('Generated bitarray signal:',data);
            dataB8ZS = [0] * int(size)
            dataB8ZS = B8ZSDataGenerator(dataB8ZS, int(ones))
            print('Generated signal for B8ZS:', dataB8ZS);
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
                addScrambleSignal = data.copy()
                ADDScrambler(addScrambleSignal)
                trasmisionErrorGenerator(addScrambleSignal)
                ADDScrambler(addScrambleSignal)
                print('ADDScrambler BER:', bitErrorRatio(data, addScrambleSignal), '%')
        elif selection == '4':
            if not data:
                print('No signal generated! Cannot continue!')
                os.system('pause')
            else:
                mulScrambleSignal = data.copy()
                MULScrambler(mulScrambleSignal)
                trasmisionErrorGenerator(mulScrambleSignal)
                MULDescrambler(mulScrambleSignal)
                print('MULScrambler BER:',bitErrorRatio(data,mulScrambleSignal),'%')
        elif selection == '5':
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
        elif selection == '6':
            if not data:
                print('No signal generated! Cannot continue!')
                os.system('pause')
            else:
                notScrambleSignal = data.copy()
                NOTScrambler(notScrambleSignal)
                trasmisionErrorGenerator(notScrambleSignal)
                NOTScrambler(notScrambleSignal)
                print('NOTScrambler BER:',bitErrorRatio(data,notScrambleSignal),'%')
        elif selection == '7':
            if not dataB8ZS:
                print('No signal generated! Cannot continue!')
                os.system('pause')
            else:
                b8zsScrambleSignal = dataB8ZS.copy()
                b8zsScrambleSignal = B8ZSScrambler(b8zsScrambleSignal, -1)
                b8zsScrambleSignal = trasmisionErrorGeneratorForB8(b8zsScrambleSignal)
                b8zsScrambleSignal = B8ZSDescrambler(b8zsScrambleSignal)
                print('B8ZSScrambler BER: ',bitErrorRatio(dataB8ZS,b8zsScrambleSignal),'%')
        elif selection == '8':
            runTests()
        elif selection == '0':
            break;
        else:
            print ("Unknown Option Selected!")

if __name__ == '__main__':
    main()