import argparse
from components.cpu import CPU
from instructions.instruction import Instruction
from instructions.nop import NoOperation
from utils import read_program_from_file


def run_arm_program(file_path, print_option, max_iterations):
    cpu = CPU()
    read_program_from_file(fp=file_path, cpu=cpu)

    current_instruction: Instruction = cpu.registers[cpu.program_counter]
    num_iterations = 0
    while (
        not isinstance(current_instruction, NoOperation)
        or num_iterations <= max_iterations
    ):
        cpu.print_cpu_state(print_option=print_option)
        current_instruction.execute()
        current_instruction = cpu.registers[cpu.program_counter]
        num_iterations += 1

    if num_iterations == max_iterations:
        print("Maximum iterations reached! The program might not have completed.")


def main():
    parser = argparse.ArgumentParser(description="ARM-LEG Program Runner")

    parser.add_argument(
        "-f", type=str, required=True, help="Path to the ARM program file"
    )
    parser.add_argument(
        "-p",
        type=str,
        choices=["BOTH", "MEM", "REG"],
        required=True,
        help="Print option: BOTH, MEM, or REG",
    )
    parser.add_argument(
        "-m",
        type=int,
        default=1000,
        help="Maximum number of iterations (default: 1000)",
    )

    args = parser.parse_args()

    run_arm_program(args.f, args.p, args.m)


if __name__ == "__main__":
    main()
