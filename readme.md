<div align="center">
<pre>

 █████╗ ██████╗ ███╗   ███╗      ██╗     ███████╗ ██████╗ 
██╔══██╗██╔══██╗████╗ ████║      ██║     ██╔════╝██╔════╝ 
███████║██████╔╝██╔████╔██║█████╗██║     █████╗  ██║  ███╗
██╔══██║██╔══██╗██║╚██╔╝██║╚════╝██║     ██╔══╝  ██║   ██║
██║  ██║██║  ██║██║ ╚═╝ ██║      ███████╗███████╗╚██████╔╝
╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝      ╚══════╝╚══════╝ ╚═════╝ 
----------------------------------------------------------
python pseudo-ARM program simulator
</pre>
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
</div>
This is a Python program to "simulate" the subset of the subset of ARM we use in <em>CS 251: Computer Organization and Design</em>. The word simulate is used loosely as this program doesn't execute the instructions how a real CPU would, its behaviorally? equivalent to it.

## Program Structure
```
.
├── arm_leg/
│   ├── components/
│   │   ├── cpu.py
│   │   ├── data_memory.py
│   │   └── register_file.py
│   ├── instructions/
│   │   ├── b_format.py
│   │   ├── cb_format.py
│   │   ├── d_format.py
│   │   ├── i_format.py
│   │   ├── instruction.py
│   │   ├── nop.py
│   │   ├── opcodes.py
│   │   └── r_format.py
│   ├── __init__.py
│   ├── main.py
│   └── utils.py
├── tests/
│   ├── test_arithmetic_operations.py
│   ├── test_branching.py
│   ├── test_load_store.py
│   └── test_parsing_instructions.py
├── .gitignore
├── conftest.py
├── instruction_documentation.md
├── LICENSE
├── readme.md
└── requirements.txt
```

## Installation

> :warning: This program requires `python >=3.10`.

Clone the repository

```sh
git clone https://github.com/DarkHawk727/ARM-LEG-Simulator/
```
then install the dependencies

```sh
pip install -r requirements.txt
```

## Usage

> :information_source: For information about how to write your pseudo-ARM programs, see the [Instruction Documentation](https://www.github.com/DarkHawk727/ARM-LEG-Simulator/blob/main/instruction_documentation.md).


### Using `ARM-LEG` in the Command Line

```sh
ARM-LEG -f "some/folder/example.txt" -p ["BOTH" | "MEM" | "REG"] -m 1000
```

(you can use `--help` to display this in the command line)

The print option will either display the contents of the memory, the registers, or both __for each iteration of the pseudo-ARM program__; this means that the outputs can get quite long.
The `-m` option will set a max-iterations count so that in the case of an infinite loop, the program does terminate.

(you can redirect the outputs to a textfile using standard output redirection)

## Current Limitations

- ~~Doesn't support X31 immutability.~~
- Doesn't support X31 aliasing with XZR.
- Doesn't support comments?
- Need to test: `STUR`, `LDUR`, `CBZ`, and `B`
- Programs must be at most 31 instructions long (Just 31 stores or smth) since they are stored in the registers (ig take CS450 to solve this)

## Contributing

1. Fork [it](https://github.com/zahash/DarkHawk727/ARM-LEG-simulator)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request.
