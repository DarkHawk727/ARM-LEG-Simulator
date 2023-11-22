from typing import Literal

from tabulate import tabulate

from arm_leg.components.data_memory import DataMemory
from arm_leg.components.register_file import RegisterFile
from arm_leg.instructions.b_format import BFormatInstruction
from arm_leg.instructions.cb_format import CBFormatInstruction
from arm_leg.instructions.d_format import DFormatInstruction


class CPU:
    program_counter: int
    registers: RegisterFile
    memory: DataMemory

    def __init__(self) -> None:
        self.program_counter = 0
        self.registers = RegisterFile()
        self.memory = DataMemory()

    def execute_instruction(self) -> None:
        current = self.registers[self.program_counter]
        if isinstance(current, int):
            raise ValueError("Program counter jumped to integer!")
        else:
            if isinstance(current, BFormatInstruction):
                current.execute(self.program_counter)
            elif isinstance(current, CBFormatInstruction):
                current.execute(self.registers, self.program_counter)
            elif isinstance(current, DFormatInstruction):
                current.execute(self.registers, self.memory)
                self.program_counter += 4
            else:  # I and R format take the same args
                current.execute(self.registers)
                self.program_counter += 4

    def print_cpu_state(self, print_option: Literal["REG", "MEM", "BOTH"]) -> None:
        allowable_options = {"REG", "MEM", "BOTH"}

        # Reshape registers into 2x16 format
        print_reg = [
            self.registers[i : i + 16] for i in range(0, len(self.registers), 16)
        ]

        # Reshape memory into 16x16 format
        print_mem = [self.memory[i : i + 16] for i in range(0, len(self.memory), 16)]

        print("\n\033[92m" + "PROGRAM COUNTER: " + "\033[0m", self.program_counter)
        print(
            "\033[92m" + "CURRENT INSTRUCTION: " + "\033[0m",
            self.registers[self.program_counter],
        )

        if print_option not in allowable_options:
            raise ValueError(
                'Invalid print option, can only be one of: "REG", "MEM", "BOTH"'
            )
        if print_option in ["REG", "BOTH"]:
            print("\033[1m" + "REGISTERS" + "\033[0m")
            print(tabulate(print_reg, tablefmt="fancy_grid"))
        if print_option in ["MEM", "BOTH"]:
            print("\033[1mMEMORY\033[0m")
            print(tabulate(print_mem, tablefmt="fancy_grid"))
