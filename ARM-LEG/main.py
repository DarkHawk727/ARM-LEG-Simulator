from typing import List, Union

import numpy as np
from tabulate import tabulate


class CPU:
    def __init__(self):
        self.program_counter = 0
        self.memory = [0] * 256
        self.registers = [0] * 32

    def read_program_from_file(self, program_path: str) -> None:
        """
        Reads program from file and loads it into registers.
        """
        with open(file=program_path, mode="r") as f:
            for line in f.readlines():
                address, instruction = (
                    int(line.split(": ")[0][1:]),
                    line.split(": ")[1].strip(),
                )
                self.registers[address] = instruction

    def print_cpu_state(self, instruction: List[int | str], mode: str = "BOTH") -> None:
        """
        Function to print the contents of registers, memory, or both.
        """
        print_reg = np.reshape(a=self.registers, newshape=(2, 16))
        print_mem = np.reshape(a=self.memory, newshape=(16, 16))

        print("\n\033[92m" + "PROGRAM COUNTER: " + "\033[0m", self.program_counter)
        print("\033[92m" + "CURRENT INSTRUCTION: " + "\033[0m", instruction)
        if mode in ["REG", "BOTH"]:
            # print("\033[1m" + "REGISTERS" + "\033[0m")
            print(tabulate(print_reg, tablefmt="fancy_grid"))
        if mode in ["MEM", "BOTH"]:
            print("\033[1mMEMORY\033[0m")
            print(tabulate(print_mem, tablefmt="fancy_grid"))

    def execute_instruction(self, instruction: List[int | str]) -> None:
        """
        Executes a single instruction.

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
            case ["ADD", target, addend_1, addend_2]:
                self.registers[target] = (
                    self.registers[addend_1] + self.registers[addend_2]
                )
                self.program_counter += 4

            case ["SUB", target, subend_1, subend_2]:
                self.registers[target] = (
                    self.registers[subend_1] - self.registers[subend_2]
                )
                self.program_counter += 4

            case ["ADDI", target, addend, constant]:
                self.registers[target] = self.registers[addend] + constant
                self.program_counter += 4

            case ["SUBI", target, addend, constant]:
                self.registers[target] = self.registers[addend] + constant
                self.program_counter += 4

            case ["CBZ", check, constant]:
                if self.registers[check] == 0:
                    self.program_counter += 4 * constant

            case ["CBNZ", check, constant]:
                if self.registers[check] != 0:
                    self.program_counter += 4 * constant

            case ["LDUR", target, addend, offset]:
                self.registers[target] = self.memory[addend + offset]
                self.program_counter += 4

            case ["STUR", target, addend, offset]:
                self.memory[addend + offset] = self.registers[target]
                self.program_counter += 4

            case ["B", offset]:
                self.program_counter += 4 * offset


def parse_instruction(instruction: str | int) -> List[str | int]:
    """
    Takes in the string representation of an instruction and strips all extraneous symbols.
    """
    if instruction == ["EXIT"]:
        return ["EXIT"]
    else:
        instruction = (
            instruction.replace("X", "")
            .replace(":", "")
            .replace(",", "")
            .replace("#", "")
            .replace("[", "")
            .replace("]", "")
            .split()
        )

        instruction = [instruction[0]] + list(
            map(int, instruction[1:])
        )  # Convert the numbers to integers.

        return instruction


def main() -> None:
    ARM = CPU()
    ARM.read_program_from_file("ARM-LEG/examples/example1.txt")
    
    while ARM.program_counter != 32:
        inst = parse_instruction(ARM.registers[ARM.program_counter])
        ARM.execute_instruction(inst)
        ARM.print_cpu_state(inst)


if __name__ == "__main__":
    main()
