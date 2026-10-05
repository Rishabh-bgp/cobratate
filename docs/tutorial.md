# Tutorial

This tutorial assumes no prior Cobratate. It assumes an ordinary programming vocabulary. Each example is a complete program. The banners are optional; they are included because a Cobratate program traditionally announces that it has left.

Save a program as `hello.cbt` and run it:

```
python cobratate.py hello.cbt
```

With no file, the same interpreter starts a read-eval-print loop. The prompt is `topg>`. `:quit` leaves it. A snippet can also be run without a file:

```
python cobratate.py -c 'WHAT COLOR IS YOUR BUGATTI 21 PLUS 21'
```

## A first program

```
ESCAPE THE MATRIX
WHAT COLOR IS YOUR BUGATTI "What color is your Bugatti?"
BACK TO THE MATRIX
```

`WHAT COLOR IS YOUR BUGATTI` prints one value and a newline. The text is a string literal. A comment begins with `MATRIX:`, `#`, or `//` and runs to the end of the line.

## Names

```
BUGATTI wealth EQUALS 1000
BUGATTI day EQUALS 1
WHAT COLOR IS YOUR BUGATTI wealth
```

`BUGATTI` binds a name in the current environment. A later `BUGATTI` for the same name in the same environment replaces the value. Names are case-sensitive. `wealth` and `Wealth` are different.

An unbound name is an error: the name is "not in the garage."

## Arithmetic

```
WHAT COLOR IS YOUR BUGATTI 84 DIVIDED BY 2
WHAT COLOR IS YOUR BUGATTI 7 SPLIT BY 2
WHAT COLOR IS YOUR BUGATTI 7 MODULO 2
```

`DIVIDED BY` is real division, except that an exact whole result is kept as an integer, so the first line prints `42`. `SPLIT BY` is floor division and prints `3`. `MODULO` is the remainder.

`PLUS` adds numbers. If either side is text, it concatenates, after rendering the other side. `TIMES` multiplies. A string times a non-negative integer repeats the string. `"Cobra" TIMES 3` is `CobraCobraCobra`.

## Truth

`SIGMA` is true. `BETA` is false. They print as those words. A condition is sigma when it is `SIGMA`, a non-zero number, a non-empty string, or a non-empty garage. Zero, `BETA`, the empty string, and the empty garage are not sigma.

```
IF wealth IS GREATER THAN 0 THEN
  WHAT COLOR IS YOUR BUGATTI "Still in the game."
OTHERWISE YOU ARE A BETA
  WHAT COLOR IS YOUR BUGATTI "Broke behavior."
PERIOD
```

`OTHERWISE YOU ARE A BETA` may be omitted. `PERIOD` closes the conditional. A comparison is `IS GREATER THAN`, `IS LESS THAN`, `IS THE SAME AS`, or `IS NOT THE SAME AS`. `AND` and `OR` are short-circuit. `NOT` negates sigma-ness.

## Grinding

```
BUGATTI n EQUALS 1
GRIND WHILE n IS LESS THAN 4
  WHAT COLOR IS YOUR BUGATTI n
  BUGATTI n EQUALS n PLUS 1
STOP GRINDING
```

The body runs while the condition is sigma. `ESCAPE THE GRIND` leaves the innermost grind. A grind that runs past one million turns stops with an error, so a forgotten increment does not hang the interpreter forever.

## Hustles

A hustle is a function.

```
HUSTLE net WITH revenue AND cost
  CASH OUT revenue MINUS cost
DONE HUSTLING

WHAT COLOR IS YOUR BUGATTI CALL net (9000, 1200)
```

`CALL net (9000, 1200)` is the robust call form: the parenthesis ends the call, so a following operator is outside it. `CALL net WITH 9000 AND 1200` is the same call. `AND` in that form separates arguments, and a boolean `AND` inside an argument must be parenthesized.

`CASH OUT` leaves the current hustle with a value. Without it, the hustle yields `0`. A hustle may call itself. Nesting stops after one thousand calls.

Assignment inside a hustle is local. The hustle can read an outer name. Assigning that name does not change the outer binding.

## Garages

A garage is a list.

```
BUGATTI primes EQUALS [2, 3, 5, 7]
WHAT COLOR IS YOUR BUGATTI CALL at (primes, 0)
WHAT COLOR IS YOUR BUGATTI CALL piece (primes, 1, 3)
WHAT COLOR IS YOUR BUGATTI primes PLUS [11]
```

`CALL at` indexes. A negative index counts from the end. `CALL piece` slices with the same start and end rules as Python. `PLUS` concatenates two garages. An index outside the garage is an error.

## Asking

`ASK THE MATRIX` reads one line. A line that is an integer or a float becomes that number. Anything else stays text. End of input yields the empty string.

```
BUGATTI answer EQUALS ASK THE MATRIX
WHAT COLOR IS YOUR BUGATTI "heard " PLUS answer
```

The next page is the [language reference](reference.md).
