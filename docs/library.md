# Built-in hustles

These names are bound in the global environment of every program. Each is called like a user hustle. A wrong argument count is an error. A user hustle of the same name shadows the built-in in that environment.

## length

`CALL length WITH value`

The length of text or of a garage. Any other value is rendered as text first, and that text's length is returned.

## absolute

`CALL absolute WITH number`

The absolute value. A non-number is an error. `SIGMA` is accepted as `1` and `BETA` as `0`, because conditions are numeric in arithmetic.

## floor

`CALL floor WITH number`

The greatest integer not above the number. Floor division by `SPLIT BY` is usually clearer.

## at

`CALL at WITH target AND index`

One element of a garage, or one character of text. A negative index counts from the end. An index outside the value is an error and names the length.

## piece

`CALL piece WITH target AND start AND end`

A slice of text or of a garage. Bounds follow Python: they are clamped, and a negative bound counts from the end. The result has the same kind as `target`.

## kind

`CALL kind WITH value`

Returns `"number"`, `"text"`, `"sigma"`, `"garage"`, or `"hustle"`.

## text

`CALL text WITH value`

The same rendering that print uses, without the newline.

## number

`CALL number WITH value`

A number is returned unchanged. `SIGMA` becomes `1` and `BETA` becomes `0`. Text is parsed as an integer, or as a float if it contains a point. Text that is not a number is an error.

## min and max

`CALL min (a, b, c)` and `CALL max (a, b, c)`

The least or greatest argument, compared with ordinary ordering. At least one argument is required. Mixing text and numbers raises the usual comparison error if the values cannot be ordered.

## Absence

There is no file hustle, no network hustle, and no clock. A program that needs them should be generated from outside, or the interpreter should be extended. The [contributing notes](../CONTRIBUTING.md) describe where that extension belongs.
