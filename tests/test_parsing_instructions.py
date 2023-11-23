import pytest

from arm_leg.instructions.b_format import UnconditionalBranch
from arm_leg.instructions.cb_format import BranchOnNonZero, BranchOnZero
from arm_leg.instructions.d_format import LoadWord, StoreWord
from arm_leg.instructions.i_format import AddImmediate, SubImmediate
from arm_leg.instructions.nop import NoOperation
from arm_leg.instructions.r_format import Add, And, Eor, LeftShift, Orr, RightShift, Sub
from arm_leg.utils import parse_pseudocode, tokenize


@pytest.mark.parametrize(
    "input_str, expected_output",
    [
        ("X0: ADD X1, X3, X4", [0, "ADD", 1, 3, 4]),
        ("X25: SUB X8, X13, X1", [25, "SUB", 8, 13, 1]),
        ("X3: LSL X7, X3, X14", [3, "LSL", 7, 3, 14]),
        ("X7: RSL X11, X6, X3", [7, "RSL", 11, 6, 3]),
        ("X14: AND X6, X3, X7", [14, "AND", 6, 3, 7]),
        ("X1: ORR X7, X9, X15", [1, "ORR", 7, 9, 15]),
        ("X0: EOR X14, X14, X14", [0, "EOR", 14, 14, 14]),
        ("X4: ADDI X4, X3 #4", [4, "ADDI", 4, 3, 4]),
        ("X1: ADDI X6, X15 #-16", [1, "ADDI", 6, 15, -16]),
        ("X8: SUBI X5, X3 #2", [8, "SUBI", 5, 3, 2]),
        ("X5: LDUR X12, [X5 #-9]", [5, "LDUR", 12, 5, -9]),
        ("X7: STUR X15, [X2 #200]", [7, "STUR", 15, 2, 200]),
        ("X9: CBZ X17, X14 #-9", [9, "CBZ", 17, 14, -9]),
        ("X11: CBZ X19, X1 #9", [11, "CBZ", 19, 1, 9]),
        ("X13: CBNZ X21, X3 #-9", [13, "CBNZ", 21, 3, -9]),
        ("X15: CBNZ X25, X7 #-9", [15, "CBNZ", 25, 7, -9]),
        ("X18: B #27", [18, "B", 27]),
        ("X103: B #-18", [103, "B", -18]),
        ("X31: NOP", [31, "NOP"]),
    ],
)
def test_tokenize(input_str, expected_output):
    assert tokenize(input_str) == expected_output


@pytest.mark.parametrize(
    "input_str, expected_output",
    [
        ("X0: ADD X1, X3, X4", (0, Add(rn=1, rd=3, rm=4))),
        ("X25: SUB X8, X13, X1", (25, Sub(rn=8, rd=13, rm=1))),
        ("X3: LSL X7, X3, X14", (3, LeftShift(rn=7, rd=3, rm=14))),
        ("X7: RSL X11, X6, X3", (7, RightShift(rn=11, rd=6, rm=3))),
        ("X14: AND X6, X3, X7", (14, And(rn=6, rd=3, rm=7))),
        ("X1: ORR X7, X9, X15", (1, Orr(rn=7, rd=9, rm=15))),
        ("X0: EOR X14, X14, X14", (0, Eor(rn=14, rd=14, rm=14))),
        ("X4: ADDI X4, X3 #4", (4, AddImmediate(rn=4, rd=3, constant=4))),
        ("X1: ADDI X6, X15 #-16", (1, AddImmediate(rn=6, rd=15, constant=-16))),
        ("X8: SUBI X5, X3 #2", (8, SubImmediate(rn=5, rd=3, constant=2))),
        ("X5: LDUR X12, [X5 #-9]", (5, LoadWord(rn=12, rt=5, dt_address=-9))),
        ("X7: STUR X15, [X2 #200]", (7, StoreWord(rn=15, rt=2, dt_address=200))),
        ("X9: CBZ X17, #9", (9, BranchOnZero(rt=17, br_address=9))),
        ("X11: CBZ X19, #9", (11, BranchOnZero(rt=19, br_address=9))),
        ("X13: CBNZ X21, #9", (13, BranchOnNonZero(rt=21, br_address=9))),
        ("X15: CBNZ X25, #-9", (15, BranchOnNonZero(rt=25, br_address=-9))),
        ("X18: B #27", (18, UnconditionalBranch(br_address=27))),
        ("X103: B #-18", (103, UnconditionalBranch(br_address=-18))),
        ("X31: NOP", (31, NoOperation())),
    ],
)
def test_parse_pseudocode(input_str, expected_output):
    assert parse_pseudocode(input_str) == expected_output


# Test for exceptions
def test_unknown_instruction() -> None:
    with pytest.raises(ValueError):
        parse_pseudocode("X10: HUH X3 X3 X4")
        parse_pseudocode("Not even close!")
