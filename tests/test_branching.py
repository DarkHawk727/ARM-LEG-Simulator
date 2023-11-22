import pytest

from components.cpu import cpu
from instructions.b_format import UnconditionalBranch
from instructions.cb_format import BranchOnNonZero, BranchOnZero


class BranchTest:
    def unconditional_branch(self) -> None:
        cpu = CPU()
        cpu.registers[0] = UnconditionalBranch(br_address=4)
        
        assert cpu.program_counter == 16

    def branch_on_zero_taken(self) -> None:
        cpu = CPU()
        cpu.registers[0] = BranchOnZero(rt=1, br_address=4)
        cpu.execute_instruction()

        assert cpu.program_counter == 16

    def branch_on_zero_not_taken(self) -> None:
        cpu = CPU()
        cpu.registers[0] = BranchOnZero(rt=1, br_address=4)
        cpu.registers[1] = 14
        cpu.execute_instruction()

        assert cpu.program_counter == 4

    def branch_on_not_zero_taken(self) -> None:
        cpu = CPU()
        cpu.registers[0] = BranchOnNonZero(rt=1, br_address=4)
        cpu.execute_instruction()

        assert cpu.program_counter == 4

    def branch_on_not_zero_not_taken(self) -> None:
        cpu = CPU()
        cpu.registers[0] = BranchOnNonZero(rt=1, br_address=4)
        cpu.registers[1] = 14
        cpu.execute_instruction()

        assert cpu.program_counter == 16
