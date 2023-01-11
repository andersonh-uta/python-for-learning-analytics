"""
https://adventofcode.com/2019/day/2

Opcodes:
    1: add
    2: multiple
    99: halt/exit the program

Syntax:
    opcode, arg_ptr1, arg_ptr2, dst_ptr

Logic:
    global_register = [...]
    opcodes = {...}
    global_register[dst_ptr] = opcodes[opcode](
        global_register[arg_ptr1],
        global_register[arg_ptr2],
    )

"""
from copy import deepcopy

instructions = list(map(int, open("inputs/2019_day_2").read().split(",")))
instructions[1] = 12
instructions[2] = 2

def compute_intcode(instructions):
    instructions = deepcopy(instructions)
    for idx in range(0, len(instructions), 4):
        opcode, operand_1, operand_2, destination = instructions[idx:idx+4]
        operand_1 = instructions[operand_1]
        operand_2 = instructions[operand_2]
        if opcode == 1:
            instructions[destination] = operand_1 + operand_2
        elif opcode == 2:
            instructions[destination] = operand_1 * operand_2
        elif opcode == 99:
            break
        else:
            raise ValueError(f"Bad opcode: {opcode}")
    return instructions[0]


# desired output: 19690720
for noun in range(100):
    for verb in range(100):
        # print(noun, verb)
        instructions[1] = noun
        instructions[2] = verb
        result = compute_intcode(instructions)
        if result == 19690720:
            print(100*noun + verb)
            exit()