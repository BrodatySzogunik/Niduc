from bitarray import bitarray

from MULScramble import MULScramble
from MULScramble import MULDescramble
from InitArray import initArray
from bitErrorRatio import bitErrorRatio
from transmisionErrorGenerator import trasmisionErrorGenerator



mainData = bitarray(100)


mainData2 = bitarray(100)



initArray(mainData, 1)
initArray(mainData2,20)

print(mainData)
trasmisionErrorGenerator(mainData)
print(mainData)

print(mainData)
MULScramble(mainData)
trasmisionErrorGenerator(mainData)
print(mainData)




