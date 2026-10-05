# Contributing

Cobratate is released under the MIT License. See [LICENSE](LICENSE). Issues and pull requests are welcome on the public repository.

## What belongs here

- A failing program that should be accepted, or an accepted program that should fail, with the source in a test.
- A correction to the language reference when it disagrees with `cobratate.py`. The interpreter is the specification when the two disagree. Either the reference is updated, or the interpreter is changed and the change is noted.
- Documentation in the same register as `docs/`: descriptive, with an example, and without treating allegations about any real person as settled facts.
- An example under `examples/intro`, `examples/numbers`, `examples/dsa`, or `examples/ml`, with a row in [docs/programs.md](docs/programs.md).

## Local check

Python 3.10 or newer is required. From the repository root:

```bash
python -m unittest test_cobratate.py -v
python cobratate.py examples/intro/hello.cbt
python cobratate.py examples/dsa/bubble.cbt
python cobratate.py examples/ml/perceptron.cbt
python cobratate.py --version
```

On macOS or Linux, `python3` may be the installed command. A change to evaluation rules should add or adjust a test in `test_cobratate.py`. The sample programs must keep running.

## Site

GitHub Pages publishes the repository root. `index.html` is the page that is served. `site/index.html` is the source copy, and `site/mark.jpg` is the emblem. After editing `site/index.html`, copy it to `index.html` and point the emblem at `site/mark.jpg`. The public address is [rishabh-bgp.github.io/cobratate](https://rishabh-bgp.github.io/cobratate/).

## Style

The interpreter is one module so that a reader can follow a program from token to value without a package layout. Keywords are phrases. Failures are `BetaError`. Comments in the implementation may use the language's register. The reference manual should not.
