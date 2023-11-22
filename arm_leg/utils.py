from typing import List, Tuple

from arm_leg.components.central_processing_unit import CPU
from arm_leg.instructions.b_format import UnconditionalBranch
from arm_leg.instructions.cb_format import BranchOnNonZero, BranchOnZero
from arm_leg.instructions.d_format import LoadWord, StoreWord
from arm_leg.instructions.i_format import AddImmediate, SubImmediate
from arm_leg.instructions.instruction import Instruction
from arm_leg.instructions.r_format import Add, And, LeftShift, Orr, RightShift, Sub, Xor


def tokenize(inp: str) -> List[str | int]:
    stripped = inp.translate({ord(i): None for i in "#,:X[]"}).split(" ")
    return [int(part) if i != 1 else part for i, part in enumerate(stripped)]


def parse_pseudocode(inp: str) -> Tuple[int, Instruction]:
    tokenized = tokenize(inp)

    # Define a mapping from instruction names to constructors
    instruction_map = {
        "B": lambda args: UnconditionalBranch(br_address=args[0]),
        "CBZ": lambda args: BranchOnZero(rt=args[0], br_address=args[1]),
        "CBNZ": lambda args: BranchOnNonZero(rt=args[0], br_address=args[1]),
        "SUB": lambda args: Sub(rn=args[0], rd=args[1], rm=args[2]),
        "ADD": lambda args: Add(rn=args[0], rd=args[1], rm=args[2]),
        "LSL": lambda args: LeftShift(rn=args[0], rd=args[1], rm=args[2]),
        "RSL": lambda args: RightShift(rn=args[0], rd=args[1], rm=args[2]),
        "ORR": lambda args: Orr(rn=args[0], rd=args[1], rm=args[2]),
        "AND": lambda args: And(rn=args[0], rd=args[1], rm=args[2]),
        "XOR": lambda args: Xor(rn=args[0], rd=args[1], rm=args[2]),
        "LDUR": lambda args: LoadWord(rn=args[0], rt=args[1], dt_address=args[2]),
        "STUR": lambda args: StoreWord(rn=args[0], rt=args[1], dt_address=args[2]),
        "ADDI": lambda args: AddImmediate(rn=args[0], rt=args[1], dt_address=args[2]),
        "SUBI": lambda args: SubImmediate(rn=args[0], rt=args[1], dt_address=args[2]),
    }

    address, instruction, *args = tokenized

    if instruction in instruction_map:
        return (address, instruction_map[instruction](args))
    else:
        raise ValueError(f"Unknown instruction: {instruction}")


def read_program_from_file(fp: str, cpu: CPU) -> None:
    with open(fp, "r") as f:
        for line in f.readlines():
            address, instruction = parse_pseudocode(line)
            cpu.registers[address] = instruction
