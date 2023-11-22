import pytest

from components.cpu import CPU
from instructions.i_format import AddImmediate, SubImmediate
from instructions.r_format import Add, And, LeftShift, Orr, RightShift, Sub, Xor


class ArithmeticTest:
    def test_add(self) -> None:
        cpu = CPU()
        cpu.registers[0] = Add(rn=2, rd=3, rm=1)
        cpu.registers[1] = 15
        cpu.registers[2] = 14
        cpu.execute_instruction()

        assert cpu.registers[3] == 29

    def test_sub(self) -> None:
        cpu = CPU()
        cpu.registers[0] = Sub(rn=2, rd=3, rm=1)
        cpu.registers[1] = 28
        cpu.registers[2] = 1
        cpu.execute_instruction()

        assert cpu.registers[3] == -27

    def test_left_shift(self) -> None:
        cpu = CPU()
        cpu.registers[0] = LeftShift(rn=2, rd=3, rm=1)
        cpu.registers[1] = 2
        cpu.registers[2] = 3
        cpu.execute_instruction()

        assert cpu.registers[3] == 12

    def test_right_shift(self) -> None:
        cpu = CPU()
        cpu.registers[0] = RightShift(rn=2, rd=3, rm=1)
        cpu.registers[1] = 2
        cpu.registers[2] = 4
        cpu.execute_instruction()

        assert cpu.registers[3] == 1

    def test_and(self) -> None:
        cpu = CPU()
        cpu.registers[0] = And(rn=2, rd=3, rm=1)
        cpu.registers[1] = 8
        cpu.registers[2] = 9
        cpu.execute_instruction()

        assert cpu.registers[3] == 8

    def test_orr(self) -> None:
        cpu = CPU()
        cpu.registers[0] = Orr(rn=2, rd=3, rm=1)
        cpu.registers[1] = 15
        cpu.registers[2] = 14
        cpu.execute_instruction()

        assert cpu.registers[3] == 15

    def test_xor(self) -> None:
        cpu = CPU()
        cpu.registers[0] = Xor(rn=2, rd=3, rm=1)
        cpu.registers[1] = 2
        cpu.registers[2] = 8
        cpu.execute_instruction()

        assert cpu.registers[3] == 10

    def add_immediate(self) -> None:
        cpu = CPU()
        cpu.registers[0] = AddImmediate(rn=1, rd=2, constant=8)
        cpu.registers[1] = 13
        cpu.execute_instruction()

        assert cpu.registers[2] == 21

    def sub_immediate(self) -> None:
        cpu = CPU()
        cpu.registers[0] = SubImmediate(rn=1, rd=2, constant=4)
        cpu.registers[1] = 13
        cpu.execute_instruction()

        assert cpu.registers[2] == 9
