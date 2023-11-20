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
├── ARM-LEG/
│   ├── __init__.py
│   ├── main.py
│   └── utils.py
├── components/
│   ├── cpu.py
│   ├── register_file.py
│   └── data_memory.py
├── instructions/
│   ├── b_format.py
│   ├── cb_format.py
│   ├── d_format.py
│   ├── i_format.py
│   ├── instruction.py
│   ├── opcodes.py
│   └── r_format.py
├── tests/
│   ├── instruction_tests/
│   │   ├── load.py
│   │   ├── store.py
│   │   ├── arithmetic.py
│   │   └── branches.py
│   └── parse_tests/
│       ├── test0.txt
│       ├── test1.txt
│       └── test2.txt
├── .gitignore
├── instruction_documentation.md
└── readme.md
```

## Installation
> :warning: This program requires `python <3.10`.

Clone the repository

```sh
git clone https://github.com/DarkHawk727/ARM-LEG-Simulator/
```
then install the dependencies

```sh
pip install -r requirements.txt
```

## Usage

> :information_source: For information about how to write your pseudo-ARM programs, see the [Instruction Documentation](https://www.example.com).


### Using `ARM-LEG` in the Command Line
```sh
ARM-LEG -f "some/folder/example.txt" -p ["BOTH" | "MEM" | "REG"] -m 1000
```
(you can use `--help` to display this in the command line)

The print option will either display the contents of the memory, the registers, or both __for each iteration of the pseudo-ARM program__; this means that the outputs can get quite long.
The `-m` option will set a max-iterations count so that in the case of an infinite loop, the program does terminate.

(you can redirect the outputs to a textfile using standard output redirection)

## Current Limitations

 - Doesn't support X31 immutability.
 - Doesn't support X31 aliasing with XZR.
 - Doesn't support comments?
 - Need to test: `STUR`, `LDUR`, `CBZ`, and `B`

## Contributing
1. Fork [it](https://github.com/zahash/DarkHawk727/ARM-LEG-simulator)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request