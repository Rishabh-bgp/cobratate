# Cobratate

Cobratate is an esoteric imperative language. The vocabulary comes from the public persona of Andrew Tate. The evaluation rules are ordinary: names, arithmetic, conditionals, loops, functions, and lists. Version 1.2 is released under the [MIT License](LICENSE). It is not affiliated with, endorsed by, or authorised by Andrew Tate.

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
| [Programs](docs/programs.md) | Introduction, numerical, data-structure, and learning examples |
| [Errors](docs/errors.md) | Diagnostics and limits |
| [Inspiration](docs/inspiration.md) | Andrew Tate, the phrases, and the allegations as allegations |
| [Glossary](docs/glossary.md) | Terms |
| [Origin](ORIGIN.md) | The IIT Jammu internship hackathon |
| [Contributing](CONTRIBUTING.md) | Tests and patches |

## Run

Python 3.10 or newer. No dependencies.

```
python cobratate.py examples/intro/hello.cbt
python cobratate.py examples/dsa/bubble.cbt
python cobratate.py examples/ml/perceptron.cbt
python cobratate.py -c 'WHAT COLOR IS YOUR BUGATTI 21 PLUS 21'
python cobratate.py --version
python -m unittest test_cobratate.py -v
```

The read-eval-print prompt is `topg>`.

## Layout

| Path | Role |
| --- | --- |
| `cobratate.py` | Interpreter, normative specification |
| `docs/` | Tutorial, reference, library, programs, errors |
| `examples/intro/` | First programs |
| `examples/numbers/` | Numerical algorithms |
| `examples/dsa/` | Sort, search, stack, graph traversal |
| `examples/ml/` | Regression, perceptron, nearest neighbour, scaling |
| `test_cobratate.py` | Regression tests |

`CALL put (garage, index, value)` returns a new garage with one index replaced. Algorithms rebind the name; they do not mutate the old garage.
