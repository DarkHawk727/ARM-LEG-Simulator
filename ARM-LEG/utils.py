from instructions.instruction import Instruction
from instructions.b_format import UnconditionalBranch
from instructions.cb_format import BranchOnZero, BranchOnNonZero
from instructions.d_format import LoadWord, StoreWord
from instructions.i_format import AddImmediate, SubImmediate
from instructions.r_format import Add, Sub, LeftShift, RightShift, Orr, And, Xor


def parse_pseudocode(inp: str) -> Instruction:
    tokenized = inp.split(" ")
    match tokenized:
        case [_, "B", arg1]:
            return UnconditionalBranch(br_address=int(arg1[1:])) # Get rid of the # prefix
        case [_, "CBZ", arg1, arg2]:
            return BranchOnZero(rt=int()) # Get rid of the # prefix
        case [_, "CBNZ", arg1, arg2]:
            return UnconditionalBranch(br_address=int(arg1[1:])) # Get rid of the # prefix
        case [_, "SUB", arg1, arg2, arg3]:
            return Sub(rn=int(arg1), rd=int(arg2), rm=int(arg3))
        case [_, "ADD", arg1, arg2, arg3]:
            return Add(rn=int(arg1), rd=int(arg2), rm=int(arg3))
        case [_, "ORR", arg1, arg2, arg3]:
            return Orr(rn=int(arg1), rd=int(arg2), rm=int(arg3))
        case [_, "AND", arg1, arg2, arg3]:
            return And(rn=int(arg1), rd=int(arg2), rm=int(arg3))
        case [_, "LSL", arg1, arg2, arg3]:
            return LeftShift(rn=int(arg1), rd=int(arg2), rm=int(arg3))
        case [_, "RSL", arg1, arg2, arg3]:
            return RightShift(rn=int(arg1), rd=int(arg2), rm=int(arg3))
        case [_, "XOR", arg1, arg2, arg3]:
            return Xor(rn=int(arg1), rd=int(arg2), rm=int(arg3))