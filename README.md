# Cobratate

Cobratate is an esoteric imperative language. Version 1.2 is released under the [MIT License](LICENSE). The vocabulary is borrowed from the public persona of Andrew Tate. The evaluation rules are ordinary: names, arithmetic, conditionals, loops, functions, and lists. It is a teaching language, not a production platform, and it is not affiliated with, endorsed by, or authorised by Andrew Tate.

**Public site:** [https://rishabh-bgp.github.io/cobratate/](https://rishabh-bgp.github.io/cobratate/)

The site is part of this repository. [`site/index.html`](site/index.html) is the source. [`index.html`](index.html) is the copy GitHub Pages serves from the repository root, together with [`site/mark.jpg`](site/mark.jpg). The page has a dark and a light mode, the install steps, the statement forms, all twenty checked programs, the manual links, and the syllabus invitation.

Created by [Er. Rishabh Aryan](https://github.com/Rishabh-bgp), M.Tech student in Artificial Intelligence and Data Science at the Indian Institute of Information Technology, Bhagalpur. The language was written during a hackathon at the Indian Institute of Technology Jammu, in the course of an internship there. The account of that session is [ORIGIN.md](ORIGIN.md). ORCID: [0009-0004-7595-9440](https://orcid.org/0009-0004-7595-9440).

```
ESCAPE THE MATRIX
WHAT COLOR IS YOUR BUGATTI "What color is your Bugatti?"
BACK TO THE MATRIX
```

`WHAT COLOR IS YOUR BUGATTI` prints. `GRIND WHILE` is a while-loop. `HUSTLE` is a function. `CASH OUT` returns. A reader who does not know the persona can still use the [language reference](docs/reference.md), because each phrase has one meaning. The [inspiration note](docs/inspiration.md) separates the borrowed phrases from the public allegations, which are stated as allegations.

## Contents

- [Public site](#public-site)
- [How to use Cobratate on your computer](#how-to-use-cobratate-on-your-computer)
- [What a program contains](#what-a-program-contains)
- [Programs](#programs)
- [Manual](#manual)
- [For universities, colleges, and schools](#for-universities-colleges-and-schools)
- [Repository layout](#repository-layout)
- [License](#license)

## Public site

The published page is [rishabh-bgp.github.io/cobratate](https://rishabh-bgp.github.io/cobratate/).

| Path in this repository | Role |
| --- | --- |
| [site/index.html](site/index.html) | Source of the page. Edit this file. |
| [site/mark.jpg](site/mark.jpg) | Emblem used by the page. |
| [index.html](index.html) | Copy served by GitHub Pages, which publishes the repository root. After an edit, copy `site/index.html` here and point the emblem at `site/mark.jpg`. |
| [.github/workflows/pages.yml](.github/workflows/pages.yml) | Optional Actions deploy of the `site/` folder. The live site is currently the root copy. |

The page is responsive. Below 720 pixels the navigation collapses to a Menu control. Tables scroll sideways rather than widening the page. The colour mode follows the system on a first visit and is then stored in the browser.

## How to use Cobratate on your computer

Python 3.10 or newer is required. There is no package to install and no network call at runtime. The interpreter is the single file `cobratate.py`.

1. Check Python.

```bash
python --version
```

If that command is not found, try `python3 --version` or, on Windows, `py --version`. If the reported version is older than 3.10, install a current Python from [python.org](https://www.python.org/downloads/). On Windows, enable "Add python.exe to PATH" during installation.

2. Obtain the repository.

```bash
git clone https://github.com/Rishabh-bgp/cobratate.git
cd cobratate
```

If Git is not installed, download the ZIP from the Code button on GitHub, extract it, and open a terminal in that folder. The commands below are the same.

3. Confirm the interpreter, then run a greeting, a sort, and a small learning model.

```bash
python cobratate.py --version
python cobratate.py examples/intro/hello.cbt
python cobratate.py examples/dsa/bubble.cbt
python cobratate.py examples/ml/perceptron.cbt
```

On macOS or Linux, use `python3` if that is the command that answered the version check. On Windows, use `py` if `python` is not recognised.

4. Run one statement without saving a file.

```bash
python cobratate.py -c "WHAT COLOR IS YOUR BUGATTI 21 PLUS 21"
```

5. Start the read-eval-print loop. The prompt is `topg>`. A complete line runs immediately. A line that opens `IF`, `GRIND WHILE`, or `HUSTLE` waits until you close it with `PERIOD`, `STOP GRINDING`, or `DONE HUSTLING`. `:help` prints the forms. `:quit` leaves the loop.

```bash
python cobratate.py
```

6. Write a program of your own. Save it as a text file, conventionally `name.cbt`, then pass that path.

```bash
python cobratate.py myprogram.cbt
```

`python cobratate.py --help` prints the three forms: a file, `-c CODE`, or no argument for the loop. A program that fails exits with status 1 and a line beginning `Beta behavior detected`. A wrong command line exits with status 2. A missing file is reported on the standard error stream rather than as a Python traceback.

The first reading after installation is the [tutorial](docs/tutorial.md). The rules are in the [language reference](docs/reference.md). Diagnostics are listed in [errors](docs/errors.md).

## What a program contains

A program is enclosed by `ESCAPE THE MATRIX` and `BACK TO THE MATRIX`. `MATRIX:` starts a comment, as do `#` and `//`. When this page and `cobratate.py` disagree, the interpreter is the specification.

| Form | Meaning |
| --- | --- |
| `WHAT COLOR IS YOUR BUGATTI expr` | Print `expr` and a newline. |
| `BUGATTI name EQUALS expr` | Bind a name in the current environment. |
| `IF expr THEN … OTHERWISE YOU ARE A BETA … PERIOD` | Conditional. The otherwise-branch may be omitted. |
| `GRIND WHILE expr … STOP GRINDING` | Loop while `expr` is sigma. `ESCAPE THE GRIND` leaves it. |
| `HUSTLE name WITH a AND b … DONE HUSTLING` | Define a function. |
| `CASH OUT expr` | Return from the current function. |
| `CALL name (expr, expr)` | Call. The parenthesis ends the argument list. |
| `ASK THE MATRIX` | Read one line. `ASK THE MATRIX FOR A NUMBER` reads a number. |
| `[expr, expr]` | A list, called a garage. |
| `CALL put (garage, index, value)` | A new garage with one index replaced. The original is not modified. |

Values are numbers, text, the booleans `SIGMA` and `BETA`, and garages. `DIVIDED BY` is real division, and an exact whole result stays an integer. `SPLIT BY` is floor division. Assignment inside a function is local. A grind stops after one million turns. A function stops after one thousand nested calls. An error names the line and, inside a call, the hustle stack.

Built-in names: `length`, `absolute`, `floor`, `at`, `piece`, `put`, `kind`, `text`, `number`, `min`, `max`. There are no classes, modules, files, or a network library. Those absences are deliberate.

## Programs

Every example, with the result it was checked against, is in [docs/programs.md](docs/programs.md). Each file runs with no input. The directory index is [examples/README.md](examples/README.md).

Introduction, in [examples/intro](examples/intro):

- [hello.cbt](examples/intro/hello.cbt) prints.
- [grind.cbt](examples/intro/grind.cbt) assigns and loops.
- [fizz.cbt](examples/intro/fizz.cbt) is FizzBuzz as COBRA, TATE, and COBRATATE.
- [hustle.cbt](examples/intro/hustle.cbt) uses functions, booleans, and string repeat.
- [garage.cbt](examples/intro/garage.cbt) uses lists, indexing, kind, and number conversion.

Numerical work, in [examples/numbers](examples/numbers):

- [primes.cbt](examples/numbers/primes.cbt) lists primes below 50 by trial division.
- [euclid.cbt](examples/numbers/euclid.cbt) computes a greatest common divisor of 42 and a least common multiple of 252.
- [collatz.cbt](examples/numbers/collatz.cbt) records hailstone steps and a peak.
- [fib.cbt](examples/numbers/fib.cbt) computes Fibonacci by recursion.
- [binomial.cbt](examples/numbers/binomial.cbt) prints Pascal's triangle.
- [bases.cbt](examples/numbers/bases.cbt) writes 42 in base 2 as 101010.

Data structures and algorithms, in [examples/dsa](examples/dsa). A stack is a garage whose last element is the top. A queue is a garage whose first element is the front. A graph is a garage of neighbour garages.

- [bubble.cbt](examples/dsa/bubble.cbt) sorts `[5, 1, 4, 2, 8, 0]` to `[0, 1, 2, 4, 5, 8]`.
- [search.cbt](examples/dsa/search.cbt) finds 9 at index 4 and reports 8 absent.
- [stack.cbt](examples/dsa/stack.cbt) leaves `[10, 20]` after three pushes and one pop.
- [twosum.cbt](examples/dsa/twosum.cbt) returns indices `[0, 1]` for `[2, 7, 11, 15]` and target 9.
- [bfs.cbt](examples/dsa/bfs.cbt) visits `[0, 1, 2, 3]` on `[[1, 2], [3], [3], []]`.

Machine learning, in [examples/ml](examples/ml). These are teaching implementations. They use ordinary arithmetic. There is no training-file format and no automatic differentiation.

- [regression.cbt](examples/ml/regression.cbt) fits `y = 2x` by gradient descent. After 200 steps the weight is about 1.99, and `x = 5` predicts about 9.98.
- [perceptron.cbt](examples/ml/perceptron.cbt) learns AND. The four inputs classify as 0 0 0 1.
- [knn.cbt](examples/ml/knn.cbt) classifies `[2, 2]` as 0 and `[5, 6]` as 1 by one nearest neighbour.
- [normalize.cbt](examples/ml/normalize.cbt) scales `[10, 20, 30]` to `[0, 0.5, 1]`. A constant column becomes zeros.

## Manual

| Document | Use it for |
| --- | --- |
| [Documentation index](docs/index.md) | The map of the manual |
| [Tutorial](docs/tutorial.md) | A first program through lists |
| [Language reference](docs/reference.md) | Tokens, values, statements, scope, limits |
| [Built-in hustles](docs/library.md) | Argument counts and the errors for a wrong call |
| [Programs](docs/programs.md) | Every example and its checked result |
| [Errors](docs/errors.md) | The diagnostics and the two exit statuses |
| [Inspiration](docs/inspiration.md) | The persona, the phrases, and the allegations as allegations |
| [Glossary](docs/glossary.md) | Terms |
| [Origin](ORIGIN.md) | The internship hackathon at the Indian Institute of Technology Jammu |
| [Contributing](CONTRIBUTING.md) | Tests, patches, and the site copy |
| [Public site](https://rishabh-bgp.github.io/cobratate/) | The same material, as a page |

## For universities, colleges, and schools

Universities, colleges, and schools are welcome to add Cobratate to a syllabus, a laboratory manual, a programming-club session, or a short module. The MIT License already permits that use: an institution may copy the interpreter, the manual, and the site, distribute them to a class, and modify them for a course, provided the copyright notice and license terms are kept with the copy. No separate permission is required. Attribution to this repository is appreciated.

The language is a supplement, not a replacement for a production language. The recommended place is an early laboratory, a one-week interlude in an introductory programming course, or a seminar on language design. A department that adopts it should also say that the persona behind the vocabulary is controversial, and that the inspiration page records the allegations as allegations. The exercises do not require students to endorse that persona.

| Laboratory | Material | Course idea |
| --- | --- | --- |
| 1 | [Tutorial](docs/tutorial.md), [hello](examples/intro/hello.cbt) | Output, comments, a complete program |
| 2 | [grind](examples/intro/grind.cbt), [hustle](examples/intro/hustle.cbt) | Assignment, conditionals, loops, functions |
| 3 | [garage](examples/intro/garage.cbt), [primes](examples/numbers/primes.cbt) | Lists and a numerical algorithm |
| 4 | [bubble](examples/dsa/bubble.cbt), [search](examples/dsa/search.cbt), [stack](examples/dsa/stack.cbt) | Sorting, search, and a stack |
| 5 | [bfs](examples/dsa/bfs.cbt), [twosum](examples/dsa/twosum.cbt) | A graph and a pair search |
| 6 | [regression](examples/ml/regression.cbt), [perceptron](examples/ml/perceptron.cbt), [knn](examples/ml/knn.cbt) | A line, a threshold model, a nearest neighbour |

The public site is a suitable first link for a laboratory sheet: [rishabh-bgp.github.io/cobratate](https://rishabh-bgp.github.io/cobratate/).

## Repository layout

| Path | Role |
| --- | --- |
| `cobratate.py` | Interpreter and normative specification |
| `docs/` | Tutorial, reference, library, catalogue, errors, glossary |
| `examples/intro/` | First programs |
| `examples/numbers/` | Numerical algorithms |
| `examples/dsa/` | Sort, search, stack, graph traversal |
| `examples/ml/` | Regression, perceptron, nearest neighbour, scaling |
| `site/index.html` | Source of the GitHub Pages site |
| `site/mark.jpg` | Emblem |
| `index.html` | Page served at the public site |
| `test_cobratate.py` | Regression tests for the interpreter |
| `LICENSE` | MIT |

From the repository directory:

```bash
python -m unittest test_cobratate.py -v
```

A change to evaluation rules should add or adjust a test. The sample programs must keep running. Details are in [CONTRIBUTING.md](CONTRIBUTING.md).

## License

Copyright (c) 2026 Er. Rishabh Aryan. Released under the [MIT License](LICENSE).
