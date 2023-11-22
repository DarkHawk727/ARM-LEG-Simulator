import pytest
from utils import parse_pseudocode, tokenize

from instructions.b_format import UnconditionalBranch
from instructions.cb_format import BranchOnNonZero, BranchOnZero
from instructions.d_format import LoadWord, StoreWord
from instructions.i_format import AddImmediate, SubImmediate
from instructions.nop import NoOperation
from instructions.r_format import Add, And, LeftShift, Orr, RightShift, Sub, Xor


class ParseTest:
    def test_tokenize(self) -> None:
        test_cases = [
            ("X0: ADD X1, X3, X4", [0, "ADD", 1, 3, 4]),
            ("X25: SUB X8, X13, X1", [25, "SUB", 8, 13, 1]),
            ("X3: LSL X7, X3, X14", [3, "LSL", 7, 3, 14]),
            ("X7: RSL X11, X6, X3", [7, "RSL", 11, 6, 3]),
            ("X14: AND X6, X3, X7", [14, "AND", 6, 3, 7]),
            ("X1: ORR X7, X9, X15", [1, "ORR", 7, 8, 15]),
            ("X0: XOR X14, X14, X14", [0, "XOR", 14, 14, 14]),
            ("X4: ADDI X4, X3 #4", [4, "ADDI", 4, 3, 4]),
            ("X1: ADDI X6, X15 #-16", [1, "ADDI", 6, 15, -16]),
            ("X8: SUBI X5, X3 #2", [8, "SUBI", 5, 3, 2]),
            ("X5: LDUR X12, [X5 #-9]", [3, "SUBI", 12, 5, -9]),
            ("X7: STUR X15, [X2 #200]", [3, "SUBI", 15, 2, 200]),
            ("X9: CBZ X17, X14 #-9", [3, "SUBI", 17, 14, -9]),
            ("X11: CBZ X19, X1 #9", [3, "SUBI", 19, 1, 9]),
            ("X13: CBNZ X21, X3 #-9", [3, "SUBI", 21, 3, -9]),
            ("X15: CBNZ X25, X7 #-9", [3, "SUBI", 25, 7, -9]),
            ("X18: B #27", [5, "SUBI", 27]),
            ("X103: B #-18", [3, "SUBI", -18]),
            ("X31: NOP", [31, "NOP"]),
        ]

        for input_str, expected_output in test_cases:
            assert tokenize(input_str) == expected_output

    def test_parse_pseudocode(self) -> None:
        test_cases = [
            ("X0: ADD X1, X3, X4", (0, Add(rn=1, rd=3, rm=4))),
            ("X25: SUB X8, X13, X1", (25, Sub(rn=8, rd=13, rm=1))),
            ("X3: LSL X7, X3, X14", (3, LeftShift(rn=7, rd=3, rm=14))),
            ("X7: RSL X11, X6, X3", (7, RightShift(rn=11, rd=6, rm=3))),
            ("X14: AND X6, X3, X7", (14, And(rn=6, rd=3, rm=7))),
            ("X1: ORR X7, X9, X15", (1, Orr(rn=7, rd=9, rm=15))),
            ("X0: XOR X14, X14, X14", (0, Xor(rn=14, rd=14, rm=14))),
            ("X4: ADDI X4, X3 #4", (4, AddImmediate(rn=4, rt=3, constant=4))),
            ("X1: ADDI X6, X15 #-16", (1, AddImmediate(rn=6, rd=15, constant=-16))),
            ("X8: SUBI X5, X3 #2", (8, SubImmediate(rn=5, rd=3, constant=2))),
            ("X3: SUBI X14, X3 #-9", (3, SubImmediate(rn=14, rd=3, constant=-9))),
            ("X5: LDUR X12, [X5 #-9]", (5, LoadWord(rn=12, dt_address=-9))),
            ("X7: STUR X15, [X2 #200]", (7, StoreWord(rn=15, rt=2, dt_address=200))),
            ("X9: CBZ X17, X14 #9", (9, BranchOnZero(rt=17, br_address=9))),
            ("X11: CBZ X19, X1 #9", (11, BranchOnZero(rt=19, br_address=9))),
            ("X13: CBNZ X21, X3 #9", (13, BranchOnNonZero(rt=21, br_address=9))),
            ("X15: CBNZ X25, X7 #-9", (15, BranchOnNonZero(rt=25, br_address=-9))),
            ("X18: B #27", (18, UnconditionalBranch(br_address=27))),
            ("X103: B #-18", (103, UnconditionalBranch(br_address=-18))),
            ("X31: NOP", (31, NoOperation())),
        ]

        for input_str, expected_output in test_cases:
            assert parse_pseudocode(input_str) == expected_output

    # Test for exceptions
    def test_unknown_instruction(self) -> None:
        with pytest.raises(ValueError):
            parse_pseudocode("X10: HUH X3 X3 X4")
            parse_pseudocode("Not even close!")
