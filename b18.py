import sys

class Wire:
    def __init__(self, signal, index):
        self.__signal = signal
        self.__index = index

    def setSignal(self, signal):
        self.__signal = int(signal)

    def getSignal(self):
        return self.__signal

class Nand:
    def __init__(self, in1, in2, in_index, out_index):
        self.__in1 = in1
        self.__in2 = in2
        self.__in_index = in_index
        self.__out_index = out_index

    def getin1index(self):
        return self.__in1

    def getin2index(self):
        return self.__in2

    def setin1index(self, in1):
        self.__in1 = int(in1)

    def setin2index(self, in2):
        self.__in2 = int(in2)

    def updateOutput(self, outputs):
        num_outputs = len(outputs) - 1
        if self.__in1> num_outputs or self.__in2 > num_outputs or self.__out_index > num_outputs:
            return
        outputs[self.__out_index].setSignal(1 - 
        (outputs[self.__in1].getSignal() * outputs[self.__in2].getSignal()))

def printHeader(j, k, m, n):
    print("------" * (j + k))
    for i in range(j):
        print('{:>3}  |'.format(i), end="")
    for i in range(m * n * 2, (m * n * 2) + k):
        print('{:>3}  |'.format(i), end="")
    print()
    print("------" * (j + k))

def b18_simulation(fileName, Circuit, inputs, outputs, j, k):
    fin = open(fileName)
    for i, line in enumerate(fin.readlines()):
        line = line.split()
        in_wire = int(line[1])
        out_wire = int(line[0])

        if in_wire >= len(Circuit)*2:
            inputs[in_wire].setSignal(outputs[out_wire].getSignal())

        elif in_wire % 2 == 0:
            Circuit[int(in_wire/2)].setin1index(out_wire)
            Circuit[int(in_wire/2)].updateOutput(outputs)
        else:
            Circuit[int(in_wire/2)].setin2index(out_wire)
            Circuit[int(in_wire / 2)].updateOutput(outputs)

    for i in range(j):
        print("  " + str(outputs[i].getSignal()) + "  |", end="")
    for out in range(k, 0, -1):
        print("  " + str(inputs[-out].getSignal()) + "  |", end="")
    print()

fileName = sys.argv[1]

j = 8
k = 4
m = 10
n = 10

inputs = []
for i in range((m*n*2) + k):
    inputs.append(Wire(None, i))

outputs = []
for i in range((m * n) + j):
    outputs.append(Wire(1, i))

input_wire_index = 0
Circuit = []
for i in range(m * n):
    Circuit.append(Nand(input_wire_index, input_wire_index + 1, i, i + j))
    input_wire_index += 2

printHeader(j, k, m, n)
counter = 0
num_inputs = pow(2, j)
while counter < num_inputs:
    binary_comb = str(bin(counter))[2:].zfill(j)
    for i in range(j):
        outputs[i].setSignal(binary_comb[i])

    b18_simulation(fileName, Circuit, inputs, outputs, j, k)
    counter = counter + 1
