# Programs

This is the catalogue. The source files are not in the repository root.

- Data structures and algorithms: [examples/dsa](../examples/dsa)
- Machine learning: [examples/ml](../examples/ml)
- Introduction: [examples/intro](../examples/intro)
- Numerical: [examples/numbers](../examples/numbers)

Each file runs with no input, from the repository directory:

```bash
python cobratate.py examples/dsa/bubble.cbt
python cobratate.py examples/ml/perceptron.cbt
```

How to install Python and clone the repository is in the [README](../README.md#how-to-use-cobratate-on-your-computer).

## Introduction

| Program | What it shows |
| --- | --- |
| [examples/intro/hello.cbt](../examples/intro/hello.cbt) | Print |
| [examples/intro/grind.cbt](../examples/intro/grind.cbt) | Assignment and a loop |
| [examples/intro/fizz.cbt](../examples/intro/fizz.cbt) | FizzBuzz as COBRA / TATE / COBRATATE |
| [examples/intro/hustle.cbt](../examples/intro/hustle.cbt) | Functions, booleans, string repeat |
| [examples/intro/garage.cbt](../examples/intro/garage.cbt) | Lists, indexing, kind, and number conversion |

## Numerical

| Program | What it shows |
| --- | --- |
| [examples/numbers/primes.cbt](../examples/numbers/primes.cbt) | Trial division |
| [examples/numbers/euclid.cbt](../examples/numbers/euclid.cbt) | Greatest common divisor and least common multiple |
| [examples/numbers/collatz.cbt](../examples/numbers/collatz.cbt) | Hailstone steps and peak |
| [examples/numbers/fib.cbt](../examples/numbers/fib.cbt) | Recursive Fibonacci |
| [examples/numbers/binomial.cbt](../examples/numbers/binomial.cbt) | Pascal's triangle |
| [examples/numbers/bases.cbt](../examples/numbers/bases.cbt) | Integer bases |

## Data structures and algorithms

Garages are the only aggregate. A stack is a garage whose last element is the top. A queue is a garage whose first element is the front. A graph is a garage of neighbour garages. `CALL put` returns a new garage; it does not modify the old one, so an algorithm rebinds the name.

| Program | Algorithm | Checked result |
| --- | --- | --- |
| [examples/dsa/bubble.cbt](../examples/dsa/bubble.cbt) | Bubble sort | `[5, 1, 4, 2, 8, 0]` becomes `[0, 1, 2, 4, 5, 8]` |
| [examples/dsa/search.cbt](../examples/dsa/search.cbt) | Linear scan and binary search | `9` is at index `4`; `8` is absent |
| [examples/dsa/stack.cbt](../examples/dsa/stack.cbt) | Push, top, and pop | After three pushes and one pop, `[10, 20]` |
| [examples/dsa/twosum.cbt](../examples/dsa/twosum.cbt) | Pair of indices adding to a target | `[2, 7, 11, 15]` and `9` give `[0, 1]` |
| [examples/dsa/bfs.cbt](../examples/dsa/bfs.cbt) | Breadth-first search | The graph `[[1, 2], [3], [3], []]` from `0` visits `[0, 1, 2, 3]` |

Binary search assumes a sorted garage and returns `MINUS 1` when the target is absent. Breadth-first search marks visited nodes in a garage of zeros and ones. It does not handle a missing node; the graph must be a dense index from zero.

## Machine learning

These are teaching implementations. They use ordinary arithmetic, not a numerical library. There is no training file format and no automatic differentiation.

| Program | Model | Checked result |
| --- | --- | --- |
| [examples/ml/regression.cbt](../examples/ml/regression.cbt) | Univariate linear regression, gradient descent, 200 steps | On \(y = 2x\), the weight is about \(1.99\) and \(x = 5\) predicts about \(9.98\) |
| [examples/ml/perceptron.cbt](../examples/ml/perceptron.cbt) | Perceptron on the AND gate | The four inputs classify as `0 0 0 1` |
| [examples/ml/knn.cbt](../examples/ml/knn.cbt) | One-nearest neighbour, squared Euclidean distance | `[2, 2]` is class `0`; `[5, 6]` is class `1` |
| [examples/ml/normalize.cbt](../examples/ml/normalize.cbt) | Min-max scaling | `[10, 20, 30]` becomes `[0, 0.5, 1]`; a constant column becomes zeros |

The regression loss is mean squared error, applied as the gradient of \(\frac{1}{n}\sum_i (w x_i + b - y_i)^2\). The perceptron updates \(w \leftarrow w + \eta (y - \hat{y}) x\) with a threshold at zero. Nearest neighbour does not take a square root, because the ordering of squared distances is the same.
