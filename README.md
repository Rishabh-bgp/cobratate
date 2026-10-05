# Cobratate

Cobratate is an esoteric imperative language for people who are learning to program, and for instructors who want a short language whose jokes are in the words and whose rules are ordinary. Version 1.2 is released under the [MIT License](LICENSE). Universities, colleges, and schools are welcome to add it to a syllabus.

The vocabulary comes from the public persona of Andrew Tate. The evaluator does not. `WHAT COLOR IS YOUR BUGATTI` prints. `GRIND WHILE` is a while-loop. `HUSTLE` is a function. `CASH OUT` returns. A reader who knows the persona can hear the monologue. A reader who does not can still use the [language reference](docs/reference.md), because each phrase has one meaning.

This project is not affiliated with, endorsed by, or authorised by Andrew Tate. The [inspiration note](docs/inspiration.md) separates the borrowed phrases from the public allegations, which are stated as allegations.

```
ESCAPE THE MATRIX
WHAT COLOR IS YOUR BUGATTI "What color is your Bugatti?"
BACK TO THE MATRIX
```

The checked catalogue of every example is [docs/programs.md](docs/programs.md). Data-structure programs live in [examples/dsa](examples/dsa). Machine-learning programs live in [examples/ml](examples/ml). The public site is [rishabh-bgp.github.io/cobratate](https://rishabh-bgp.github.io/cobratate/).

## How to use Cobratate on your computer

Python 3.10 or newer is required. There is no package to install and no network call at runtime. The interpreter is the single file `cobratate.py`.

1. Check Python.

```bash
python --version
```

If that command is not found, try `python3 --version` or, on Windows, `py --version`. If the reported version is older than 3.10, install a current Python from [python.org](https://www.python.org/downloads/). On Windows, enable "Add python.exe to PATH" during installation.

2. Clone the repository and enter it.

```bash
git clone https://github.com/Rishabh-bgp/cobratate.git
cd cobratate
```

If Git is not installed, download the repository as a ZIP from the green Code button on GitHub, extract it, and open a terminal in that folder. The commands below are the same.

3. Confirm the interpreter, then run the greeting, a sort, and a small learning model.

```bash
python cobratate.py --version
python cobratate.py examples/intro/hello.cbt
python cobratate.py examples/dsa/bubble.cbt
python cobratate.py examples/ml/perceptron.cbt
```

On macOS or Linux, replace `python` with `python3` if that is the command that answered the version check. On Windows, replace it with `py` if `python` is not recognised.

4. Run one statement without saving a file.

```bash
python cobratate.py -c "WHAT COLOR IS YOUR BUGATTI 21 PLUS 21"
```

5. Start the read-eval-print loop. The prompt is `topg>`. A complete line runs immediately. A line that opens `IF`, `GRIND WHILE`, or `HUSTLE` waits until you close it with `PERIOD`, `STOP GRINDING`, or `DONE HUSTLING`. `:help` prints the forms. `:quit` leaves the loop.

```bash
python cobratate.py
```

6. Write a program of your own. Save it as a text file, conventionally with the extension `.cbt`, in any directory. From the repository directory, pass its path.

```bash
python cobratate.py myprogram.cbt
```

`python cobratate.py --help` prints the three forms: a file, `-c CODE`, or no argument for the loop. A program that fails exits with status 1 and a line beginning `Beta behavior detected`. A wrong command line exits with status 2. A missing file is reported on the standard error stream rather than as a Python traceback.

The first reading after installation is the [tutorial](docs/tutorial.md). The rules are in the [language reference](docs/reference.md). Diagnostics are listed in [errors](docs/errors.md).

## For universities, colleges, and schools

Universities, colleges, and schools are welcome to add Cobratate to a syllabus, a laboratory manual, a programming-club session, or a short module whose aim is to make the first encounter with programming less solemn. The MIT License already permits that use: an institution may copy the interpreter and the manual, distribute them to a class, and modify them for a course, provided the copyright notice and license terms are kept with the copy. No separate permission is required. Attribution to this repository is appreciated.

The language is suitable as a supplement, not as a replacement for a production language. The recommended place is an early laboratory, a one-week interlude in an introductory programming course, or a seminar on language design. Students meet names, arithmetic, truth, loops, functions, and lists, then see those same ideas carry a sort, a search, a graph traversal, and a small learning model. The unfamiliar words slow the student down just enough to read the rule rather than the keyword.

A department that adopts it should also say, in the course note, that the persona behind the vocabulary is controversial and that the [inspiration page](docs/inspiration.md) records the allegations as allegations. The exercises do not require students to endorse that persona. An instructor who wants the rules without the register can still teach from the reference manual, which is written in ordinary technical English.

Suggested mapping onto a first programming course:

| Week or laboratory | Cobratate material | Course idea |
| --- | --- | --- |
| 1 | [Tutorial](docs/tutorial.md), [hello](examples/intro/hello.cbt) | Output, comments, a complete program |
| 2 | [grind](examples/intro/grind.cbt), [hustle](examples/intro/hustle.cbt) | Assignment, conditionals, loops, functions |
| 3 | [garage](examples/intro/garage.cbt), [primes](examples/numbers/primes.cbt) | Lists and a numerical algorithm |
| 4 | [bubble](examples/dsa/bubble.cbt), [search](examples/dsa/search.cbt), [stack](examples/dsa/stack.cbt) | Sorting, search, and a stack |
| 5 | [bfs](examples/dsa/bfs.cbt), [twosum](examples/dsa/twosum.cbt) | A graph and a pair search |
| 6 | [regression](examples/ml/regression.cbt), [perceptron](examples/ml/perceptron.cbt), [knn](examples/ml/knn.cbt) | A line, a threshold model, a nearest neighbour |

Assessment can be a short program with a stated input and a stated printed result, compared with the checked results in [docs/programs.md](docs/programs.md). The interpreter accepts no hidden standard library, so a submission is the file the student wrote.

Instructors who adapt an example, translate the manual, or add a laboratory sheet are welcome to send the change as a pull request. The [contributing notes](CONTRIBUTING.md) describe the local check.

## What the language contains

Cobratate 1.2 has numbers, text, the booleans `SIGMA` and `BETA`, lists written as garages, and functions written as hustles. It has assignment, a conditional, a while-loop, input, and calls. It does not have classes, modules, files, or a network library. Those absences are deliberate: a teaching language that fits in one file should not pretend to be a platform.

| Form | Meaning |
| --- | --- |
| `WHAT COLOR IS YOUR BUGATTI expr` | Print `expr` and a newline |
| `BUGATTI name EQUALS expr` | Bind a name in the current environment |
| `IF expr THEN ... OTHERWISE YOU ARE A BETA ... PERIOD` | Conditional; the otherwise-branch may be omitted |
| `GRIND WHILE expr ... STOP GRINDING` | Loop while `expr` is sigma |
| `ESCAPE THE GRIND` | Leave the innermost loop |
| `HUSTLE name WITH a AND b ... DONE HUSTLING` | Define a function |
| `CASH OUT expr` | Return from the current function |
| `CALL name (expr, expr)` | Call; the parenthesis ends the call |
| `ASK THE MATRIX` | Read one line |
| `[expr, expr]` | A list |
| `CALL put (garage, index, value)` | A new list with one index replaced |

`DIVIDED BY` is real division, and an exact whole result stays an integer. `SPLIT BY` is floor division. A grind stops after one million turns. A function stops after one thousand nested calls. An error names the line and, inside a call, the hustle stack. Assignment inside a function is local: it can read an outer name and does not write through to it.

## Programs

Every example, with the result it was checked against, is in [docs/programs.md](docs/programs.md).

Introduction, in [examples/intro](examples/intro): [hello](examples/intro/hello.cbt), [grind](examples/intro/grind.cbt), [FizzBuzz](examples/intro/fizz.cbt), [functions](examples/intro/hustle.cbt), [lists](examples/intro/garage.cbt).

Numerical, in [examples/numbers](examples/numbers): [primes](examples/numbers/primes.cbt), [Euclid](examples/numbers/euclid.cbt), [Collatz](examples/numbers/collatz.cbt), [Fibonacci](examples/numbers/fib.cbt), [binomial coefficients](examples/numbers/binomial.cbt), [bases](examples/numbers/bases.cbt).

Data structures and algorithms, in [examples/dsa](examples/dsa):

- [Bubble sort](examples/dsa/bubble.cbt)
- [Linear scan and binary search](examples/dsa/search.cbt)
- [Stack](examples/dsa/stack.cbt)
- [Two-sum](examples/dsa/twosum.cbt)
- [Breadth-first search](examples/dsa/bfs.cbt)

Machine learning, in [examples/ml](examples/ml). These are teaching implementations, not a numerical library:

- [Linear regression](examples/ml/regression.cbt) by gradient descent
- [Perceptron](examples/ml/perceptron.cbt) on the AND gate
- [One-nearest neighbour](examples/ml/knn.cbt)
- [Min-max scaling](examples/ml/normalize.cbt)

## Manual

| Document | Use it for |
| --- | --- |
| [Documentation index](docs/index.md) | The map of the manual |
| [Tutorial](docs/tutorial.md) | A first program through lists |
| [Language reference](docs/reference.md) | Tokens, values, statements, scope, limits |
| [Built-in hustles](docs/library.md) | `length`, `at`, `put`, `kind`, `min`, `max`, and the rest |
| [Programs](docs/programs.md) | Every example and its checked result |
| [Errors](docs/errors.md) | The diagnostics |
| [Inspiration](docs/inspiration.md) | The persona, the phrases, and the allegations as allegations |
| [Glossary](docs/glossary.md) | Terms |
| [Origin](ORIGIN.md) | The internship hackathon at the Indian Institute of Technology Jammu |
| [Contributing](CONTRIBUTING.md) | Tests and patches |
| [Examples index](examples/README.md) | The four example directories |

When the manual and `cobratate.py` disagree, the interpreter is the specification and the manual should be corrected.

## Layout and checks

| Path | Role |
| --- | --- |
| `cobratate.py` | Interpreter and normative specification |
| `docs/` | Tutorial, reference, library, catalogue, errors |
| `examples/intro/` | First programs |
| `examples/numbers/` | Numerical algorithms |
| `examples/dsa/` | Sort, search, stack, graph traversal |
| `examples/ml/` | Regression, perceptron, nearest neighbour, scaling |
| `test_cobratate.py` | Regression tests for the interpreter |
| `LICENSE` | MIT |

From the repository directory:

```bash
python -m unittest test_cobratate.py -v
```

A change to evaluation rules should add or adjust a test. The sample programs must keep running. Details are in [CONTRIBUTING.md](CONTRIBUTING.md).
