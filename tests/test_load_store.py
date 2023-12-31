from arm_leg.components.central_processing_unit import CPU
from arm_leg.instructions.d_format import LoadWord, StoreWord


def test_stores() -> None:
    cpu = CPU()
    cpu.registers[0] = StoreWord(rn=1, rt=2, dt_address=0)
    cpu.registers[2] = 42
    cpu.execute_instruction()

    assert cpu.memory[1] == 42


def test_loads() -> None:
    cpu = CPU()
    cpu.registers[0] = LoadWord(rn=1, rt=2, dt_address=0)
    cpu.memory[1] = 24
    cpu.execute_instruction()

    assert cpu.registers[2] == 24


def test_load_overwrite() -> None:
    cpu = CPU()
    cpu.registers[0] = LoadWord(rn=1, rt=2, dt_address=0)
    cpu.registers[2] = 72
    cpu.memory[1] = 24
    cpu.execute_instruction()

    assert cpu.registers[2] == 24


def test_store_overwrite() -> None:
    cpu = CPU()
    cpu.registers[0] = StoreWord(rn=1, rt=2, dt_address=0)
    cpu.registers[2] = 24
    cpu.memory[1] = 42
    cpu.execute_instruction()

    assert cpu.memory[1] == 24
