# Instruction Documentation

Writing programs in pseudo-arm is pretty simple, they all take the form:

```text
address_num: instruction args...
```

- Prefix all register addresses with an `X`
- Constants are pefixed with a `#`
- Tokens are separared by commas **AND SPACES**.
  - Suffix the address with a semicolon as well
  - Exclude the comma separating the instruction keyword and the first argument.
  - `LDUR` and `STUR` require that you enclose `s2` and `#C` in square brackets.

> :information_source: It is just a convention to place instructions 4 registers apart, you can not do this if you want.

## Instruction Reference

| Instruction | Syntax              | Effect                        |
|-------------|---------------------|-------------------------------|
| `ADD`       | `ADD s1, s2, s3`    | `s1 = s2 + s3`                |
| `ADDI`      | `ADDI s1, s2, #C`   | `s1 = s2 + C`                 |
| `AND`       | `AND s1, s2, s3`    | `s1 = s2 & s3`                |
| `LSL`       | `LSL s1, s2, s3`    | `s1 = s2 << s3`               |
| `ORR`       | `ORR s1, s2, s3`    | `s1 = s2 \| s3`               |
| `RSL`       | `RSL s1, s2, s3`    | `s1 = s2 >> s3`               |
| `SUB`       | `SUB s1, s2, s3`    | `s1 = s2 - s3`                |
| `SUBI`      | `SUBI s1, s2, #C`   | `s1 = s2 - C`                 |
| `XOR`       | `XOR s1, s2, s3`    | `s1 = s2 ^ s3`                |
| `LDUR`      | `LDUR s1, [s2, #C]` | `s1 = Memory[s2+100]`         |
| `STUR`      | `STUR s1, [s2, #C]` | `Memory[s2+100] = s1`         |
| `B`         | `B #C`              | `PC += 4 * C`                 |
| `CBZ`       | `CBZ s1, #C`        | `if s1 == 0 goto Pc += 4 * C` |
| `CBZ`       | `CBNZ s1, #C`       | `if s1 != 0 goto Pc += 4 * C` |

## Example

```text
X0: ADD X1, X31, X31
X4: ADD X2, X31, X31
X8: LDUR X3, [X1, #80]
X12: ADD X2, X2, X3
X16: ADDI X1, X1, #8
X20: SUBI X4, X1, #96
X24: CBNZ X4, #-4
X48: NOP
```

### Line-By-Line Explanation

1. Sets `X1` to 0.
2. Sets `X2` to 0.
3. Loads value of `MEM[80]` into `X3`.
4. Increments `X2` by `X3`.
5. Increments `X1` by 8.
6. Sets `X4` to be the difference between `X1` and 96.
7. Checks if `X4` is 0, if so it sets the program counter to 8, going back to step 3 only this time X1 has a different value.

### Python Translation

```py
X1, X2 = 0, 0
while X4 != 0:
    X3 = MEM[X1+80]
    X2 += X3
    X1 += 8
    X4 = X1 - 96
```
