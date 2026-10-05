# Cobratate

Cobratate is an esoteric imperative language. The vocabulary comes from the public persona of Andrew Tate. The evaluation rules are ordinary: names, arithmetic, conditionals, loops, functions, and lists. Version 1.1 is released under the [MIT License](LICENSE). It is not affiliated with, endorsed by, or authorised by Andrew Tate.

```
ESCAPE THE MATRIX
WHAT COLOR IS YOUR BUGATTI "What color is your Bugatti?"
BACK TO THE MATRIX
```

The manual is organised like the Python documentation.

| | |
| --- | --- |
| [Documentation index](docs/index.md) | Where to start |
| [Tutorial](docs/tutorial.md) | A first program through garages |
| [Language reference](docs/reference.md) | The rules |
| [Built-in hustles](docs/library.md) | The standard names |
| [Errors](docs/errors.md) | Diagnostics and limits |
| [Inspiration](docs/inspiration.md) | Andrew Tate, the phrases, and the allegations as allegations |
| [Glossary](docs/glossary.md) | Terms |
| [Origin](ORIGIN.md) | The IIT Jammu internship hackathon |
| [Contributing](CONTRIBUTING.md) | Tests and patches |

## Run

Python 3.10 or newer. No dependencies.

```
python cobratate.py examples/hello.cbt
python cobratate.py -c 'WHAT COLOR IS YOUR BUGATTI 21 PLUS 21'
python cobratate.py --version
python cobratate.py
python -m unittest test_cobratate.py -v
```

The read-eval-print prompt is `topg>`.

## Statements

| Form | Meaning |
| --- | --- |
| `WHAT COLOR IS YOUR BUGATTI expr` | Print `expr` and a newline |
| `BUGATTI name EQUALS expr` | Bind in the current environment |
| `IF expr THEN ... PERIOD` | Conditional |
| `IF expr THEN ... OTHERWISE YOU ARE A BETA ... PERIOD` | Conditional with alternative |
| `GRIND WHILE expr ... STOP GRINDING` | Loop while `expr` is sigma |
| `ESCAPE THE GRIND` | Leave the innermost grind |
| `HUSTLE name WITH a AND b ... DONE HUSTLING` | Define a function |
| `CASH OUT expr` | Return |
| `CALL name (expr, expr)` | Call. The parenthesis ends the call |
| `[expr, expr]` | A garage, which is a list |

`SIGMA` is true and `BETA` is false. `ASK THE MATRIX` reads one line. Comments run from `MATRIX:`, `#`, or `//` to the end of the line. Failures are `Beta behavior detected`, with the hustle stack when the failure is inside a call.

## Examples

- `examples/hello.cbt` — output
- `examples/grind.cbt` — assignment and a loop
- `examples/fizz.cbt` — FizzBuzz, as COBRA / TATE / COBRATATE
- `examples/fib.cbt` — recursive Fibonacci
- `examples/hustle.cbt` — functions, booleans, string repeat
- `examples/primes.cbt` — trial division
- `examples/euclid.cbt` — greatest common divisor and least common multiple
- `examples/collatz.cbt` — hailstone steps and peak
- `examples/binomial.cbt` — Pascal's triangle
- `examples/bases.cbt` — integer bases
- `examples/garage.cbt` — lists, indexing, and kind
