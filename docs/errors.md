# Errors

Every failure the interpreter intends to report is a `BetaError`. The text begins `Beta behavior detected`, and includes the line when one is known. If the failure happens inside a hustle, the following lines name that hustle and the call site, from innermost to outer.

The interpreter does not try to recover and continue. A program either finishes or stops at the first beta behavior.

## Syntax

| Situation | What is reported |
| --- | --- |
| Character that begins no token | the Matrix does not recognize it |
| String with no closing quote | unclosed string |
| Block reaches end of file | the block was never closed, with the opening line |
| Token after `BACK TO THE MATRIX` | unexpected token after the program |
| Repeated parameter | the hustle repeats a parameter |
| Call or expression where a value was required | expected a value |

## Names and calls

| Situation | What is reported |
| --- | --- |
| Unbound name | not in the garage |
| Calling a non-hustle | not a hustle |
| Wrong argument count | expected and actual counts |
| `CASH OUT` at the top level | nothing to cash |
| `ESCAPE THE GRIND` outside a grind | no grind to escape |

## Values

| Situation | What is reported |
| --- | --- |
| Arithmetic on text, except `PLUS` and a repeating `TIMES` | expected a number |
| Division or remainder by zero | division, split, or modulo by zero |
| Negative string repeat | cannot be repeated a negative number of times |
| Index outside text or a garage | index is outside a value of that length |
| `PUT` applied to a non-garage, or to an index outside it | expected a garage, or the index is outside that length |
| `NUMBER` applied to text that is not numeric | cannot read a number |

## Limits

A grind past 1,000,000 turns reports the limit and the line of the `GRIND WHILE`. A hustle nested past 1,000 calls reports the limit and the call. These replace an unbounded hang and a raw recursion traceback.

A program error exits with status 1. A wrong command line exits with status 2. A missing file is reported on the standard error stream. The forms are `cobratate.py FILE`, `cobratate.py -c CODE`, and `cobratate.py` for the read-eval-print loop.

## Input and files

A missing program file is reported on the standard error stream and the process exits with status 1. A beta behavior in a program also exits with status 1. Status 2 is reserved for a wrong command line. End of input is not an error: `ASK THE MATRIX` yields the empty string.
