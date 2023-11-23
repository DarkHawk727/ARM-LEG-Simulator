import pytest

from arm_leg.components.central_processing_unit import CPU
from arm_leg.instructions.b_format import UnconditionalBranch
from arm_leg.instructions.cb_format import BranchOnNonZero, BranchOnZero


def test_unconditional_branch() -> None:
    cpu = CPU()
    cpu.registers[0] = UnconditionalBranch(br_address=4)

    assert cpu.program_counter == 16


def test_branch_on_zero_taken() -> None:
    cpu = CPU()
    cpu.registers[0] = BranchOnZero(rt=1, br_address=4)
    cpu.execute_instruction()

    assert cpu.program_counter == 16


def test_branch_on_zero_not_taken() -> None:
    cpu = CPU()
    cpu.registers[0] = BranchOnZero(rt=1, br_address=4)
    cpu.registers[1] = 14
    cpu.execute_instruction()

    assert cpu.program_counter == 4


def test_branch_on_not_zero_taken() -> None:
    cpu = CPU()
    cpu.registers[0] = BranchOnNonZero(rt=1, br_address=4)
    cpu.execute_instruction()

    assert cpu.program_counter == 4


def test_branch_on_not_zero_not_taken() -> None:
    cpu = CPU()
    cpu.registers[0] = BranchOnNonZero(rt=1, br_address=4)
    cpu.registers[1] = 14
    cpu.execute_instruction()

    assert cpu.program_counter == 16
