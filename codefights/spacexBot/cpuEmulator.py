def cpuEmulator(subroutine):
    pc = [0]
    step = 0
    MAX = [pow(2, 32)]
    PCMAX = 1024
    STEPMAX = 5 * pow(10, 4)

    operations = {}
    opcode = lambda f: operations.setdefault(f.__name__, f)

    @opcode
    def MOV(xx, yy):
        '''
        When xx is a register, copies the value from register
        Rxx to Ryy.

        When xx is a constant, copies the constant d to Ryy.
        '''
        if xx.isnumeric():
            registers[yy] = int(xx)
        else:
            registers[yy] = registers[xx]

    @opcode
    def ADD(xx, yy):
        '''
        Calculates (Rxx + Ryy) MOD 2^32 and stores to Rxx
        '''
        registers[xx] = (int(registers[xx]) + int(registers[yy])) % MAX[0]

    @opcode
    def DEC(xx):
        '''
        Decrements Rxx by one and stores to Rxx. Decrementing 0
        will cause and underflow and results in 2^32 - 1
        '''
        if int(registers[xx]) == 0:
            registers[xx] = MAX[0] - 1
        else:
            registers[xx] = int(registers[xx]) - 1

    @opcode
    def INC(xx):
        '''
        Increments Rxx by one and stores to Rxx. Incrementing
        2^32 - 1 will cause and overflow and results in 0
        '''
        if int(registers[xx]) == MAX[0] - 1:
            registers[xx] = 0
        else:
            registers[xx] = int(registers[xx]) + 1

    @opcode
    def INV(xx):
        '''
        bitwise inversion of Rxx
        '''
        registers[xx] = ~int(registers[xx])

    @opcode
    def JMP(d):
        '''
        d is the 1-indexed location of the instruction to
        unconditionally jump to. We decrement pc by one to account
        for the 1-based index and once more because we increment pc
        after calling each operation.
        '''
        pc[0] = int(d) - 2


    @opcode
    def JZ(d):
        '''
        d is the 1-indexed location of the instruction to
        conditionally jump to. We decrement pc by one to account
        for the 1-based index and once more because we increment pc
        after calling each operation. The condition is based on the
        value of R00, if it is equal to zero, then we jump to d.

        '''
        if registers["R00"] == 0:
            pc[0] = int(d) - 2

    # import array
    # registers = memoryview(array.array('I', [0 for i in range(43)]))
    #
    # from collections import namedtuple
    # registers = namedtuple('registers', ''.join(['R' + str(i).zfill(2) + ' ' for i in range(43)]))
    # IMMUTABLE NEVERMIND
    registers = {"R" + str(i).zfill(2): 0 for i in range(43)}

    while pc[0] < PCMAX:
        step +=1
        # extract funtion call
        instructionAndVariables = subroutine[pc[0]].split(" ")
        instruction = instructionAndVariables[0]
        # print("instruction: \t", instructionAndVariables)

        # extract variables
        if instruction != 'NOP':
            variables = instructionAndVariables[1].split(",")
            if len(variables) == 0:
                operations[instruction]()
            elif len(variables) == 1:
                operations[instruction](variables[0])
            else:
                operations[instruction](variables[0],variables[1])
        # Debug Print statements
        # print("Step: \t", step)
        # print("PC: \t", pc[0])
        # print("Registers: \n", registers)
        if pc[0] < len(subroutine) - 1:
            # print("\nadd one to program counter\n")
            pc[0] += 1
        else:
            # print("\nSuccessful exit of subroutine\n")
            break

        if step > STEPMAX:
            # print("\nexit subroutine - infinite loop\n")
            break

    return str(registers["R42"])

subroutine = [
    "MOV 5,R00",
    "MOV 10,R01",
    "JZ 7",
    "ADD R02,R01",
    "DEC R00",
    "JMP 3",
    "MOV R02,R42"
]

print("R42: \t", cpuEmulator(subroutine))
assert cpuEmulator(subroutine) == '50'
