# Cobratate

Cobratate is an esoteric imperative language. The vocabulary comes from the public persona of Andrew Tate. The evaluation rules are ordinary: names, arithmetic, conditionals, loops, functions, and lists. Version 1.2 is released under the [MIT License](LICENSE). It is not affiliated with, endorsed by, or authorised by Andrew Tate.

```
ESCAPE THE MATRIX
WHAT COLOR IS YOUR BUGATTI "What color is your Bugatti?"
BACK TO THE MATRIX
```

The full program catalogue, with checked results, is [docs/programs.md](docs/programs.md). The data-structure programs are in [examples/dsa](examples/dsa), and the machine-learning programs are in [examples/ml](examples/ml).

## How to use Cobratate on your computer

Python 3.10 or newer is required. There are no packages to install.

1. Install Python from [python.org](https://www.python.org/downloads/) if `python --version` or `python3 --version` is older than 3.10.
2. Clone the repository and enter it:

```bash
git clone https://github.com/Rishabh-bgp/cobratate.git
cd cobratate
```

3. Run a program. On Windows, if `python` is not recognised, use `py` instead. On macOS or Linux, `python3` is the usual command.

```bash
python cobratate.py --version
python cobratate.py examples/intro/hello.cbt
python cobratate.py examples/dsa/bubble.cbt
python cobratate.py examples/ml/perceptron.cbt
```

4. Run one statement without a file:

```bash
python cobratate.py -c "WHAT COLOR IS YOUR BUGATTI 21 PLUS 21"
```

5. Start the read-eval-print loop. The prompt is `topg>`. Type `:quit` to leave.

```bash
python cobratate.py
```

6. Run a program of your own. Save it as a text file, conventionally `name.cbt`, then pass that path:

```bash
python cobratate.py myprogram.cbt
```

`python cobratate.py --help` prints the same three forms: a file, `-c CODE`, or no argument for the loop. A program error exits with status 1. A wrong command line exits with status 2.

## Programs

Every example is listed, with the result it was checked against, in [docs/programs.md](docs/programs.md).

Data structures and algorithms, in [examples/dsa](examples/dsa):

- [Bubble sort](examples/dsa/bubble.cbt)
- [Linear scan and binary search](examples/dsa/search.cbt)
- [Stack](examples/dsa/stack.cbt)
- [Two-sum](examples/dsa/twosum.cbt)
- [Breadth-first search](examples/dsa/bfs.cbt)

Machine learning, in [examples/ml](examples/ml):

- [Linear regression](examples/ml/regression.cbt)
- [Perceptron on AND](examples/ml/perceptron.cbt)
- [One-nearest neighbour](examples/ml/knn.cbt)
- [Min-max scaling](examples/ml/normalize.cbt)

## Manual

| | |
| --- | --- |
| [Documentation index](docs/index.md) | Where to start |
| [Tutorial](docs/tutorial.md) | A first program through garages |
| [Language reference](docs/reference.md) | The rules |
| [Built-in hustles](docs/library.md) | The standard names |
| [Programs](docs/programs.md) | Every example, including data structures and learning |
| [Errors](docs/errors.md) | Diagnostics and limits |
| [Inspiration](docs/inspiration.md) | Andrew Tate, the phrases, and the allegations as allegations |
| [Glossary](docs/glossary.md) | Terms |
| [Origin](ORIGIN.md) | The IIT Jammu internship hackathon |
| [Contributing](CONTRIBUTING.md) | Tests and patches |

## Layout

| Path | Role |
| --- | --- |
| `cobratate.py` | Interpreter, normative specification |
| `docs/programs.md` | Catalogue of every example |
| `examples/intro/` | First programs |
| `examples/numbers/` | Numerical algorithms |
| `examples/dsa/` | Sort, search, stack, graph traversal |
| `examples/ml/` | Regression, perceptron, nearest neighbour, scaling |
| `test_cobratate.py` | Regression tests |

`CALL put (garage, index, value)` returns a new garage with one index replaced. Algorithms rebind the name; they do not mutate the old garage.
