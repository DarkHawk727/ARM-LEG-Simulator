import pytest

from arm_leg.components.central_processing_unit import CPU
from arm_leg.instructions.i_format import AddImmediate, SubImmediate
from arm_leg.instructions.r_format import Add, And, LeftShift, Orr, RightShift, Sub, Eor


def test_add() -> None:
    cpu = CPU()
    cpu.registers[0] = Add(rn=2, rd=3, rm=1)
    cpu.registers[1] = 15
    cpu.registers[2] = 14
    cpu.execute_instruction()

    assert cpu.registers[3] == 29


def test_sub() -> None:
    cpu = CPU()
    cpu.registers[0] = Sub(rn=2, rd=3, rm=1)
    cpu.registers[1] = 28
    cpu.registers[2] = 1
    cpu.execute_instruction()

    assert cpu.registers[3] == -27


def test_left_shift() -> None:
    cpu = CPU()
    cpu.registers[0] = LeftShift(rn=2, rd=3, rm=1)
    cpu.registers[1] = 2
    cpu.registers[2] = 3
    cpu.execute_instruction()

    assert cpu.registers[3] == 12


def test_right_shift() -> None:
    cpu = CPU()
    cpu.registers[0] = RightShift(rn=2, rd=3, rm=1)
    cpu.registers[1] = 2
    cpu.registers[2] = 4
    cpu.execute_instruction()

    assert cpu.registers[3] == 1


def test_and() -> None:
    cpu = CPU()
    cpu.registers[0] = And(rn=2, rd=3, rm=1)
    cpu.registers[1] = 8
    cpu.registers[2] = 9
    cpu.execute_instruction()

    assert cpu.registers[3] == 8


def test_orr() -> None:
    cpu = CPU()
    cpu.registers[0] = Orr(rn=2, rd=3, rm=1)
    cpu.registers[1] = 15
    cpu.registers[2] = 14
    cpu.execute_instruction()

    assert cpu.registers[3] == 15


def test_eor() -> None:
    cpu = CPU()
    cpu.registers[0] = Eor(rn=2, rd=3, rm=1)
    cpu.registers[1] = 2
    cpu.registers[2] = 8
    cpu.execute_instruction()

    assert cpu.registers[3] == 10


def add_immediate() -> None:
    cpu = CPU()
    cpu.registers[0] = AddImmediate(rn=1, rd=2, constant=8)
    cpu.registers[1] = 13
    cpu.execute_instruction()

    assert cpu.registers[2] == 21


def sub_immediate() -> None:
    cpu = CPU()
    cpu.registers[0] = SubImmediate(rn=1, rd=2, constant=4)
    cpu.registers[1] = 13
    cpu.execute_instruction()

    assert cpu.registers[2] == 9
