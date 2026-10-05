# Contributing

Cobratate is released under the MIT License. See [LICENSE](LICENSE). Issues and pull requests are welcome on the public repository.

## What belongs here

- A failing program that should be accepted, or an accepted program that should fail, with the source in a test.
- A correction to the language reference when it disagrees with `cobratate.py`. The interpreter is the specification when the two disagree; the reference should then be updated, or the interpreter should be changed and the change noted.
- Documentation in the same register as `docs/`: descriptive, with an example, and without treating allegations about any real person as settled facts.

## Local check

Python 3.10 or newer is required. From the repository root:

```
python3 -m unittest test_cobratate.py -v
python3 cobratate.py examples/hello.cbt
python3 cobratate.py --version
```

A change to evaluation rules should add or adjust a test in `test_cobratate.py`. Sample programs in `examples/` must keep running.

## Style

The interpreter is one module so that a new reader can follow a program from token to value without a package layout. Match the existing names: keywords are phrases, failures are `BetaError`, and comments in the implementation may use the language's register. The reference manual should not.
