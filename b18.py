import sys

'''
    Reads the filename from the command line
'''
filename = sys.argv[1]

'''
    Number of input pins
'''
j = 8 

'''
    number of output pins
'''
k = 4

'''
    Number of Nand gates per row
'''
m = 10

'''
    Number of rows of Nand gates
'''
n = 10

'''
    Class: Wire
    Description: 
        Replicates working of a wire in a Gate Array Architecture
    Variables:
        signal - Whether the signal is asserted or disserted
        id - index of the wire in the circuit
    Functions:
        setSignal(<value of the signal>) - Sets the signal of the wire
        getSignal() - Returns the signal of the wire
'''
class Wire:
    def __init__(self, signal, index):
        self.__signal = signal
        self.__index = index

    def setSignal(self, signal):
        self.__signal = int(signal)

    def getSignal(self):
        return self.__signal

'''
    Class: Nand
    Description: 
        Replicates the working of a Nand gate in a gate array architecture
    Variables:
        input1 - index of the first input wire
        input2 - index of the second input wire
        gate_index - index of the Nand gate
        out_wire_index - index of the output wire from the respective nand gate
'''
class Nand:
    def __init__(self, input1, input2, gate_index, out_wire_index):
        self.__input1 = input1
        self.__input2 = input2
        self.__gate_index = gate_index
        self.__out_wire_index = out_wire_index

    '''
        Returns the index of the first input wire
    '''
    def getin1index(self):
        return self.__input1

    '''
        Returns the index of the second input wire
    '''
    def getin2index(self):
        return self.__input2

    '''
        Sets the index of the first input wire to the provided index
    '''
    def setin1index(self, in1):
        self.__input1 = int(in1)

    '''
        Sets the index of the second input wire to the provided index
    '''
    def setin2index(self, in2):
        self.__input2 = int(in2)

    '''
        Performs Nand Operation if the Gate has valid indexes for the wires
        Operation: 1 - (input1 * input2) 
    '''
    def nandOperation(self, outputs):
        num_outputs = len(outputs) - 1
        if self.__input1> num_outputs or self.__input2 > num_outputs or self.__out_wire_index > num_outputs:
            return
        else:
            outputs[self.__out_wire_index].setSignal(1 - (outputs[self.__input1].getSignal() * outputs[self.__input2].getSignal()))

'''
    Function: printHeader
    Parameters:
        j - Number of input pins
        k - Number of output pins
        m - Number of nand gates in each row
        n - Number of rows of nand gates
    Description: 
        Prints the header of the output table
'''
def printHeader(j, k, m, n):
    print("------" * (j + k))
    for i in range(j):
        print('{:>3}  |'.format(i), end="")
    for i in range(m * n * 2, (m * n * 2) + k):
        print('{:>3}  |'.format(i), end="")
    print()
    print("------" * (j + k))

'''
    Function: printResults
    Parameters:
        j - Number of input pins
        inputs - list of input wires
        outputs - list of output wires
    Description:
        Prints the calculated output for each of the inputs after 
        the nand operations
'''
def printResults(j, inputs, outputs):
    for i in range(j):
        print("  " + str(outputs[i].getSignal()) + "  |", end="")
    for i in range(k, 0, -1):
        print("  " + str(inputs[-i].getSignal()) + "  |", end="")
    print()

'''
    Function: readInput
    Parameters:
        filename - name of the file to be opened for reading
    Description:
        Opens the input file and stores the contents line-by-line in a list
        and returns the list
'''
def readInput(filename):
    with open(filename) as fin:
        wirelist = fin.readlines()
        return wirelist

'''
    Function: b18_simulation
    Parameters:
        wirelist - list of pairs of input and output wire indexes in the form
                    of string
        circuit - List of Nand Gates
        inputs - list of input wires
        outputs - list of output wires]
        j - Number of input pins
        k - Number of output pins
    Description:
        Performs b18 simulation. A pair of input and output pins is selected 
        from the wirelist and checked for the following cases:
        Case 1: If the id of the input wire is greater than the number of gates
                times 2. Determines that the wire is an output wire, and the
                signal is set of the output wire  
        Case 2: if the id of the input wire is even, then the first index of 
                the wire is set
        Case 3: if the id of the wire is odd, then the second index of the wire
                is set
        Then, the signal for each of the input and output wires is printed in
        the form of a table.

'''
def b18_simulation(wirelist, circuit, inputs, outputs, j, k):
    for wire_pair in wirelist:
        wire_pair = wire_pair.split()
        in_wire = int(wire_pair[1])
        out_wire = int(wire_pair[0])

        if in_wire >= len(circuit)*2:
            inputs[in_wire].setSignal(outputs[out_wire].getSignal())
        elif in_wire % 2 == 0:
            circuit[int(in_wire/2)].setin1index(out_wire)
            circuit[int(in_wire/2)].nandOperation(outputs)
        else:
            circuit[int(in_wire/2)].setin2index(out_wire)
            circuit[int(in_wire/2)].nandOperation(outputs)
    
    printResults(j, inputs, outputs)

'''
    Function: setup
    Parameters:
        binary_comb - a string that represents the number in binary
        outputs - list of output wires
    Description:
        Sets the signal for each of the input values
'''
def setup(binary_comb, outputs):
    for i in range(j):
        outputs[i].setSignal(binary_comb[i])

'''
    Function: main
    Parameters: None
    Description:
        Start of the program. 
        Fills in the input wires list and the output wires list with wires with
        default values. Fills the circuit list with Nand Gates with default
        values. It then prints the header for the output.
        For every input in 2^j possible inputs, a binary string is generated 
        and the signals are asserted for the corresponding nand gates.
        The wirelist is then read from the inputfile provided by the user on
        the command line. It then performs the b18 simulation and the results
        are printed. The counter is then incremented by 1 inorder to produce the
        next binary permutation and the whole process repeats again. 
'''
def main():
    # Fill the inputs list with Dummy Input Wires
    inputs = []
    for i in range((m*n*2) + k):
        inputs.append(Wire(None, i))

    # Fill the outputs list with Dummy Output Wires
    outputs = []
    for i in range((m * n) + j):
        outputs.append(Wire(1, i))

    # Fill in the circuit list with Dummy Nand gates 
    input_wire_index = 0
    circuit = []
    for i in range(m * n):
        circuit.append(Nand(input_wire_index, input_wire_index + 1, i, i + j))
        input_wire_index += 2

    printHeader(j, k, m, n)

    # Setup the 
    counter = 0
    num_inputs = pow(2, j)
    while counter < num_inputs:
        setup(str(bin(counter))[2:].zfill(j), outputs)
        wirelist = readInput(filename)
        b18_simulation(wirelist, circuit, inputs, outputs, j, k)
        counter += 1

if __name__ == "__main__":
    main()