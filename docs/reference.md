# Language reference

This reference describes Cobratate 1.2 as implemented by `cobratate.py`. A construct not listed here is a syntax error. When this page and the interpreter disagree, the interpreter is the specification and this page should be corrected. The [tutorial](tutorial.md) is the first reading. The [program catalogue](programs.md) lists every checked example.

## Lexical structure

A program is a sequence of lines. Tokens are recognised by longest match, case-insensitively for keywords and case-sensitively for names. Whitespace separates tokens and is otherwise ignored.

Comments begin with `MATRIX:`, `matrix:`, `#`, or `//` and continue to the end of the line. They produce no tokens.

String literals use double quotes. The escapes are `\n`, `\t`, `\"`, and `\\`. An unclosed string is an error.

Number literals are integers, or reals with one decimal point. A leading minus is the unary operator, not part of the literal.

Names begin with a letter or `_` and continue with letters, digits, or `_`. A name that is also a keyword is the keyword.

The punctuation tokens are `(`, `)`, `[`, `]`, and `,`.

The phrase tokens, longest first, are:

| Phrase | Role |
| --- | --- |
| `ESCAPE THE MATRIX` | Optional program opener |
| `BACK TO THE MATRIX` | Optional program closer |
| `WHAT COLOR IS YOUR BUGATTI` | Print |
| `OTHERWISE YOU ARE A BETA` | Else |
| `IS NOT THE SAME AS` | Inequality |
| `IS THE SAME AS` | Equality |
| `IS GREATER THAN` | Greater |
| `IS LESS THAN` | Less |
| `ASK THE MATRIX` | Input expression |
| `ESCAPE THE GRIND` | Break |
| `STOP GRINDING` | End of loop |
| `DONE HUSTLING` | End of function |
| `GRIND WHILE` | Loop |
| `DIVIDED BY` | Real division |
| `SPLIT BY` | Floor division |
| `CASH OUT` | Return |
| `BUGATTI` | Assignment |
| `EQUALS` | Assignment operator |
| `HUSTLE` | Function |
| `PERIOD` | End of conditional |
| `SIGMA` | True |
| `BETA` | False |
| `CALL` | Call |
| `WITH` | Introduces arguments or parameters |
| `THEN` | Introduces a then-branch |
| `PLUS` `MINUS` `TIMES` `MODULO` | Arithmetic |
| `AND` `OR` `NOT` | Logic |
| `IF` | Conditional |

## Program structure

A file is a program. `ESCAPE THE MATRIX` may open it. `BACK TO THE MATRIX` may close it. Both may be absent. Tokens after the closer are an error.

## Data model

Cobratate has five kinds of value.

| Kind | Written | Notes |
| --- | --- | --- |
| number | `42`, `3.14` | Integers and floats. An exact whole float produced by arithmetic is stored as an integer when it is inside the safe integer range of IEEE-754. |
| text | `"cobra"` | Immutable string |
| sigma | `SIGMA`, `BETA` | Boolean. Printed as `SIGMA` or `BETA` |
| garage | `[1, 2, 3]` | Ordered list. May contain any value, including garages |
| hustle | defined by `HUSTLE` | Callable. Not constructed by a literal |

Sigma-ness, used by `IF`, `GRIND WHILE`, `AND`, `OR`, and `NOT`:

- `SIGMA` is sigma. `BETA` is not.
- A number is sigma when it is not zero.
- Text is sigma when it is not empty.
- A garage is sigma when it is not empty.
- A hustle is sigma.

`CALL kind WITH value` returns `"number"`, `"text"`, `"sigma"`, `"garage"`, or `"hustle"`.

## Statements

### Print

```
WHAT COLOR IS YOUR BUGATTI expression
```

Evaluates the expression and writes its text form followed by a newline.

### Assignment

```
BUGATTI name EQUALS expression
```

Binds `name` in the current environment. It does not walk outward. A hustle that assigns a name already bound outside creates a local binding and leaves the outer binding unchanged.

### Conditional

```
IF expression THEN
  statements
OTHERWISE YOU ARE A BETA
  statements
PERIOD
```

The otherwise-branch is optional. `PERIOD` is required. The condition is tested for sigma-ness, not for identity with `SIGMA`. An unclosed conditional is an error naming the opening line.

### Loop

```
GRIND WHILE expression
  statements
STOP GRINDING
```

The condition is tested before each turn. `ESCAPE THE GRIND` leaves the innermost grind only. Outside a grind it is an error. A grind stops with an error after 1,000,000 turns. The counter is per loop, not global.

### Function

```
HUSTLE name WITH param AND param
  statements
DONE HUSTLING
```

`WITH` and the parameter list are optional. Parameters may also be separated by commas. A repeated parameter is an error. The hustle closes over the environment in which it was defined, for reading. A call pushes a frame. `CASH OUT expression` leaves that frame with the value. `CASH OUT` outside a hustle is an error. A hustle that ends without `CASH OUT` yields `0`.

Nesting is limited to 1,000 hustle frames. The diagnostic names the limit. A Python recursion failure, should one still occur, is also reported as beta behavior rather than a traceback.

### Expression statement

A call used as a statement is evaluated and its value discarded.

## Expressions

Precedence, tightest first:

1. unary `NOT`, unary `MINUS`
2. `TIMES`, `DIVIDED BY`, `SPLIT BY`, `MODULO`
3. `PLUS`, `MINUS`
4. `IS GREATER THAN`, `IS LESS THAN`, `IS THE SAME AS`, `IS NOT THE SAME AS`
5. `AND`
6. `OR`

Grouping is `( expression )`.

### Arithmetic

`PLUS` on two numbers adds. On two garages it concatenates. On a garage and another value it appends or prepends that value. If either side is text and neither rule above applies, it concatenates the text forms.

`MINUS` subtracts numbers. `TIMES` multiplies numbers. A text value times a non-negative integer repeats the text. A negative repeat is an error.

`DIVIDED BY` divides in real arithmetic and then keeps an exact whole result as an integer. `SPLIT BY` is floor division and always yields an integer. `MODULO` is the remainder. Division or remainder with a zero denominator is an error.

Comparisons of text compare lexicographically. Comparisons of numbers compare numerically. `IS THE SAME AS` and `IS NOT THE SAME AS` use equality, so `1` and `1.0` compare equal after tidying, and a number is not equal to its text form.

`AND` and `OR` return a boolean and do not evaluate the right side when the left side decides the result.

### Calls

```
CALL name (expression, expression)
CALL name WITH expression AND expression
CALL name
```

The parenthesized form accepts full expressions, including `AND` and `OR`, and ends at `)`. The `WITH` form separates arguments with `AND` or a comma. Each argument in that form is parsed only through comparison precedence, so an operator after the last argument can be swallowed. Prefer the parenthesized form when an operator follows the call.

The argument count must match the parameter count. Calling a non-hustle is an error.

### Garages

```
[expression, expression]
[]
```

A trailing comma is permitted. `CALL at WITH garage AND index` returns the element. A negative index counts from the end. An index outside the garage is an error. `CALL piece WITH garage AND start AND end` returns a garage, using Python's slice bounds: a start past the end is empty, and a negative bound counts from the end. `CALL put (garage, index, value)` returns a new garage with that index replaced. It does not modify the garage that was passed in.

### Input

`ASK THE MATRIX` reads one line, without the trailing newline. An integer literal becomes an integer. A real literal becomes a float. Any other line stays text. End of input yields `""`.

## Scope

There is a global environment, and a fresh environment for each hustle call, parented on the environment in which the hustle was defined. Lookup walks outward. Assignment does not. Built-in hustles live in the global environment and may be shadowed by a user hustle of the same name.

## Text form

Numbers that are whole print without a decimal point. Other floats print with up to ten significant digits. Sigma values print as `SIGMA` and `BETA`. Garages print as `[1, 2, 3]`. Nested garages print recursively.

## Limits

| Limit | Value | Diagnostic |
| --- | --- | --- |
| Turns of one grind | 1,000,000 | grind ran past the limit |
| Nested hustle calls | 1,000 | hustle nested past the limit |
| Python stack, as a backstop | raised to cover the hustle limit | the hustle recursed until the stack quit |

These limits are properties of the interpreter, not of the language abstractly. Another implementation may choose different bounds, but a program that depends on unbounded recursion or an unbounded loop is not portable to this one.
