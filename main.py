from typing import List, Union, TypeVar

REGISTERS = [0] * 32
MEMORY = [0] * 256
PC = 0


def read_program_from_file(registers: List[Union[int, str]]) -> None:
    """
    Reads program from file and loads it into registers and memory.
    """
    with open(file="example.txt", mode="r") as f:
        for line in f.readlines():
            address, instruction = (
                int(line.split(": ")[0][1:]),
                line.split(": ")[1].strip(),
            )
            registers[address] = instruction


def print_cpu_state(
    registers: List[Union[int, str]], memory: List[Union[int, str]], mode: str = "BOTH"
) -> None:
    """
    Function to print the contents of either registers or memory or both.
    """
    print("ARM CPU")
    print("NOTE: READ LEFT TO RIGHT!")
    print("=" * 15, "CPU STATE", "=" * 15, sep=" ")

    if mode in ("REG", "BOTH"):
        print("=" * 15, "REGISTERS", "=" * 15, sep=" ")
        for i in range(0, 32, 2):
            register1 = f"X{i:02} {registers[i]:<24}"
            register2 = f"X{i+1:02} {registers[i+1]:<24}"
            print(f"{register1}{register2}")

    if mode in ("MEM", "BOTH"):
        print("=" * 15, "MEMORY", "=" * 15, sep=" ")
        for i in range(0, 256, 2):
            memory1 = f"M{i:03} {memory[i]:<24}"
            memory2 = f"M{i+1:03} {memory[i+1]:<24}"
            print(f"{memory1}{memory2}")


def execute(
    register: List[Union[int, str]],
    memory: List[Union[int, str]],
    program_counter: int,
) -> None:
    """
    Executes a single instruction and modifies the memory/registers,
    also increments the program counter.

    address: ADDI target, addend, #constant
    address: SUBI target, addend, #constant
    address: ADD target, addend_1, addend_2
    address: SUB target, subend_1, subend_2
    address: CBZ check, #constant
    address: CBNZ check, #constant
    address: LDUR target, [addend, #offset]
    addres: STUR target, [addend, #offset]
    address: B #constant
    """

    match instruction:
        case ["ADD", _, target, addend_1, addend_2]:
            register[target] = register[addend_1] + register[addend_2]
            program_counter += 4

        case ["ADD", _, target, addend_1, addend_2]:
            register[target] = register[addend_1] - register[addend_2]
            program_counter += 4

        case ["ADDI", _, target, addend, constant]:
            register[target] = register[addend] + constant
            program_counter += 4

        case ["ADDI", _, target, addend, constant]:
            register[target] = register[addend] + constant
            program_counter += 4
    
        case ["CBZ", _, check, constant]:
            if register[check] == 0:
                program_counter = 4 * constant # Note the simple assignement
        
        case ["CBNZ", _, check, constant]:
            if register[check] != 0:
                program_counter = 4 * constant # Note the simple assignment

        case ["LDUR", _, target, addend, offset]:
            register[target] = memory[addend + offset]
            program_counter += 4

        case ["STUR", target, addend, offset]:
            memory[addend + offset] = register[target]
            program_counter += 4
            
        case ["B", offset]:
            program_counter += 4 * offset


def parse_instruction(instruction: str) -> List[Union[str, int]]:
    """
    Takes in the string represntation of an instruction and strips all extraneous symbols.
    """
    instruction = (
        instruction.replace("X", "")
        .replace(":", "")
        .replace(",", "")
        .replace("#", "")
        .replace("[", "")
        .replace("]", "")
        .split()
    )
    instruction[0], instruction[1] = (
        instruction[1],
        instruction[0],
    )  # Move the operator to the front.

    instruction = [instruction[0]] + list(
        map(int, instruction[1:])
    )  # Convert the numbers to integers.

    return instruction
