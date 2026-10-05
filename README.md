# Cobratate

Cobratate is a small imperative programming language with the vocabulary of a motivational monologue and the semantics of a normal teaching language. The name joins *cobra* and *Tate*. It is an esolang: the jokes are in the syntax, not in the evaluation rules.

A program announces that it has left, does some work, and then goes back.

```
ESCAPE THE MATRIX
WHAT COLOR IS YOUR BUGATTI "What color is your Bugatti?"
BACK TO THE MATRIX
```

The banners are optional. A file of bare statements is also a program.

## Origin

Cobratate was written during a hackathon at the Indian Institute of Technology Jammu, in the course of an internship there. The constraint was a working language before the hall closed. The phrases came first; the evaluator was fitted behind them the same night. A fuller account is in [ORIGIN.md](ORIGIN.md).

## Run it

```
python cobratate.py examples/hello.cbt
python cobratate.py          # REPL, prompt is topg>
```

Requires Python 3.10 or newer. No dependencies.

## Statements

| Form | Meaning |
| --- | --- |
| `WHAT COLOR IS YOUR BUGATTI expr` | Print `expr` and a newline |
| `BUGATTI name EQUALS expr` | Bind or rebind `name` |
| `IF expr THEN ... PERIOD` | Conditional |
| `IF expr THEN ... OTHERWISE YOU ARE A BETA ... PERIOD` | Conditional with alternative |
| `GRIND WHILE expr ... STOP GRINDING` | Loop while `expr` is sigma |
| `ESCAPE THE GRIND` | Leave the innermost grind |
| `HUSTLE name WITH a AND b ... DONE HUSTLING` | Define a function; `WITH` and parameters are optional |
| `CASH OUT expr` | Return from the current hustle |
| `CALL name WITH expr AND expr` | Call a hustle. `AND` or a comma separates arguments. A boolean `AND` inside an argument must be parenthesized |
| `CALL name (expr, expr)` | Call that ends at `)`. Use this when an operator follows the call |

`ASK THE MATRIX` reads one line. A line that parses as an integer or a float becomes that number; anything else stays a string.

## Values and operators

- Numbers: `42`, `3.14`
- Strings: `"double quotes"`, with `\\n`, `\\t`, `\\"`, `\\\\`
- Booleans: `SIGMA` (true), `BETA` (false). Printed as `SIGMA` and `BETA`
- Zero, the empty string, and `BETA` are not sigma. Everything else is

| Operator | Token |
| --- | --- |
| Add, or concatenate if either side is a string | `PLUS` |
| Subtract | `MINUS` |
| Multiply; a string times an integer repeats the string | `TIMES` |
| Divide; an exact whole result stays an integer | `DIVIDED BY` |
| Floor division | `SPLIT BY` |
| Remainder | `MODULO` |
| Comparisons | `IS GREATER THAN`, `IS LESS THAN`, `IS THE SAME AS`, `IS NOT THE SAME AS` |
| Logic, short-circuit | `AND`, `OR`, `NOT` |
| Grouping | `( ... )` |

Precedence, tightest first: unary `NOT` / `MINUS`, then `TIMES` / `DIVIDED BY` / `SPLIT BY` / `MODULO`, then `PLUS` / `MINUS`, then comparisons, then `AND`, then `OR`.

## Built-in hustles

- `CALL length WITH value` — length of the value rendered as text
- `CALL absolute WITH n` — absolute value
- `CALL floor WITH n` — greatest integer not above `n`
- `CALL at WITH text AND index` — one character; a negative index counts from the end
- `CALL piece WITH text AND start AND end` — slice, Python rules

## Comments and errors

A comment runs from `MATRIX:`, `#`, or `//` to the end of the line.

Runtime and syntax failures raise `Beta behavior detected`, including an unclosed block, a missing hustle, division by zero, an index outside a string, `CASH OUT` outside a hustle, and `ESCAPE THE GRIND` outside a grind. A grind stops after one million turns. A hustle stops after one thousand nested calls. An unknown name is "not in the garage."

Assignment binds in the current block. A hustle can read an outer name, and assigning that name inside the hustle creates a local binding rather than changing the outer one. Parameters are local. `CASH OUT` leaves only the current hustle. A missing `CASH OUT` yields `0`.

## Examples

- `examples/hello.cbt` — output
- `examples/grind.cbt` — assignment and a loop
- `examples/fizz.cbt` — FizzBuzz, as COBRA / TATE / COBRATATE
- `examples/fib.cbt` — recursive Fibonacci
- `examples/hustle.cbt` — functions, booleans, string repeat
- `examples/primes.cbt` — trial division up to a limit
- `examples/euclid.cbt` — greatest common divisor, least common multiple, reduced fraction
- `examples/collatz.cbt` — hailstone steps and peak, with the longest chain
- `examples/binomial.cbt` — Pascal's triangle by combinations
- `examples/bases.cbt` — binary, hexadecimal, and an arbitrary integer base

## Scope

A hustle closes over the environment in which it was defined, for reading. Assignment does not write through to an outer environment. `CASH OUT` leaves only the current hustle. A missing `CASH OUT` yields `0`.
