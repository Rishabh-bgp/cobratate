#!/usr/bin/env python3
"""Cobratate — an esoteric programming language for those who have escaped the Matrix.

Run a program:  python cobratate.py program.cbt
Run a snippet:  python cobratate.py -c 'WHAT COLOR IS YOUR BUGATTI 21'
Start the REPL: python cobratate.py
"""

from __future__ import annotations

import sys
from dataclasses import dataclass
from typing import Any, Callable

VERSION = "1.2.0"


# ---------------------------------------------------------------------------
# Errors
# ---------------------------------------------------------------------------

class BetaError(Exception):
    """Raised when a program exhibits beta behavior."""

    def __init__(self, message: str, line: int | None = None, stack: list | None = None):
        self.line = line
        self.stack = list(stack or [])
        where = f" on line {line}" if line else ""
        text = f"Beta behavior detected{where}: {message}"
        if self.stack:
            frames = "\n".join(f"  in hustle {name} on line {lineno}" for name, lineno in self.stack)
            text = text + "\n" + frames
        super().__init__(text)


class CashOut(Exception):
    """Internal signal for CASH OUT (return)."""

    def __init__(self, value: Any):
        self.value = value


class EscapeGrind(Exception):
    """Internal signal for ESCAPE THE GRIND (break)."""


# ---------------------------------------------------------------------------
# Lexer
# ---------------------------------------------------------------------------

# Longest-match phrases first.
PHRASES: list[tuple[str, str]] = [
    ("ESCAPE THE MATRIX", "ESCAPE_THE_MATRIX"),
    ("BACK TO THE MATRIX", "BACK_TO_THE_MATRIX"),
    ("WHAT COLOR IS YOUR BUGATTI", "PRINT"),
    ("OTHERWISE YOU ARE A BETA", "ELSE"),
    ("IS NOT THE SAME AS", "NEQ"),
    ("IS THE SAME AS", "EQ"),
    ("IS GREATER THAN", "GT"),
    ("IS LESS THAN", "LT"),
    ("ASK THE MATRIX", "INPUT"),
    ("ESCAPE THE GRIND", "BREAK"),
    ("STOP GRINDING", "END_WHILE"),
    ("DONE HUSTLING", "END_FUNC"),
    ("GRIND WHILE", "WHILE"),
    ("DIVIDED BY", "DIV"),
    ("SPLIT BY", "IDIV"),
    ("CASH OUT", "RETURN"),
    ("BUGATTI", "LET"),
    ("EQUALS", "ASSIGN"),
    ("HUSTLE", "FUNC"),
    ("PERIOD", "END_IF"),
    ("SIGMA", "TRUE"),
    ("BETA", "FALSE"),
    ("CALL", "CALL"),
    ("WITH", "WITH"),
    ("THEN", "THEN"),
    ("PLUS", "PLUS"),
    ("MINUS", "MINUS"),
    ("TIMES", "TIMES"),
    ("MODULO", "MOD"),
    ("AND", "AND"),
    ("NOT", "NOT"),
    ("OR", "OR"),
    ("IF", "IF"),
]


@dataclass
class Token:
    kind: str
    value: Any
    line: int


class Lexer:
    def __init__(self, source: str):
        self.source = source
        self.lines = source.splitlines()
        self.tokens: list[Token] = []

    def tokenize(self) -> list[Token]:
        for lineno, raw in enumerate(self.lines, start=1):
            self._tokenize_line(raw, lineno)
        self.tokens.append(Token("EOF", None, len(self.lines) + 1))
        return self.tokens

    def _tokenize_line(self, raw: str, lineno: int) -> None:
        i = 0
        n = len(raw)
        while i < n:
            if raw[i].isspace():
                i += 1
                continue
            # Comments: MATRIX: ...   or  # ...   or  // ...
            if raw[i] == "#" or raw.startswith("//", i):
                return
            if raw.startswith("MATRIX:", i) or raw.startswith("matrix:", i):
                return
            if raw[i] == '"':
                i += 1
                buf = []
                while i < n and raw[i] != '"':
                    if raw[i] == "\\" and i + 1 < n:
                        mapping = {"n": "\n", "t": "\t", '"': '"', "\\": "\\"}
                        buf.append(mapping.get(raw[i + 1], raw[i + 1]))
                        i += 2
                        continue
                    buf.append(raw[i])
                    i += 1
                if i >= n or raw[i] != '"':
                    raise BetaError("unclosed string. A king finishes what he starts", lineno)
                i += 1
                self.tokens.append(Token("STRING", "".join(buf), lineno))
                continue
            if raw[i].isdigit() or (raw[i] == "." and i + 1 < n and raw[i + 1].isdigit()):
                start = i
                has_dot = False
                while i < n and (raw[i].isdigit() or (raw[i] == "." and not has_dot)):
                    if raw[i] == ".":
                        has_dot = True
                    i += 1
                text = raw[start:i]
                value: int | float = float(text) if has_dot else int(text)
                self.tokens.append(Token("NUMBER", value, lineno))
                continue
            if raw[i].isalpha() or raw[i] == "_":
                upper_rest = raw[i:].upper()
                matched = False
                for phrase, kind in PHRASES:
                    plen = len(phrase)
                    if upper_rest.startswith(phrase):
                        end = i + plen
                        if end == n or not (raw[end].isalnum() or raw[end] == "_"):
                            self.tokens.append(Token(kind, phrase, lineno))
                            i = end
                            matched = True
                            break
                if matched:
                    continue
                start = i
                while i < n and (raw[i].isalnum() or raw[i] == "_"):
                    i += 1
                word = raw[start:i]
                self.tokens.append(Token("IDENT", word, lineno))
                continue
            if raw[i] in "(),[]":
                kind = {"(": "LPAREN", ")": "RPAREN", ",": "COMMA", "[": "LBRACK", "]": "RBRACK"}[raw[i]]
                self.tokens.append(Token(kind, raw[i], lineno))
                i += 1
                continue
            raise BetaError(f"the Matrix does not recognize '{raw[i]}'", lineno)


# ---------------------------------------------------------------------------
# AST
# ---------------------------------------------------------------------------

@dataclass
class Num:
    value: int | float
    line: int


@dataclass
class Str:
    value: str
    line: int


@dataclass
class Bool:
    value: bool
    line: int


@dataclass
class Var:
    name: str
    line: int


@dataclass
class Unary:
    op: str
    expr: Any
    line: int


@dataclass
class Binary:
    op: str
    left: Any
    right: Any
    line: int


@dataclass
class Call:
    name: str
    args: list
    line: int


@dataclass
class Seq:
    items: list
    line: int


@dataclass
class Input:
    line: int


@dataclass
class Print:
    expr: Any
    line: int


@dataclass
class Assign:
    name: str
    expr: Any
    line: int


@dataclass
class If:
    cond: Any
    then_body: list
    else_body: list
    line: int


@dataclass
class While:
    cond: Any
    body: list
    line: int


@dataclass
class Func:
    name: str
    params: list[str]
    body: list
    line: int


@dataclass
class Return:
    expr: Any
    line: int


@dataclass
class Break:
    line: int


@dataclass
class ExprStmt:
    expr: Any
    line: int


@dataclass
class Program:
    body: list


# ---------------------------------------------------------------------------
# Parser
# ---------------------------------------------------------------------------

class Parser:
    def __init__(self, tokens: list[Token]):
        self.tokens = tokens
        self.pos = 0

    def current(self) -> Token:
        return self.tokens[self.pos]

    def check(self, *kinds: str) -> bool:
        return self.current().kind in kinds

    def advance(self) -> Token:
        tok = self.current()
        if tok.kind != "EOF":
            self.pos += 1
        return tok

    def expect(self, kind: str, hint: str) -> Token:
        if not self.check(kind):
            tok = self.current()
            raise BetaError(f"expected {hint}, got {tok.kind}", tok.line)
        return self.advance()

    def parse(self) -> Program:
        # Optional banner. A true program announces the escape.
        if self.check("ESCAPE_THE_MATRIX"):
            self.advance()
        body = self.parse_block(stop={"BACK_TO_THE_MATRIX", "EOF"})
        if self.check("BACK_TO_THE_MATRIX"):
            self.advance()
        if not self.check("EOF"):
            tok = self.current()
            raise BetaError(f"unexpected {tok.kind} after the program", tok.line)
        return Program(body)

    def parse_block(self, stop: set[str], opener: str = "block", line: int | None = None) -> list:
        stmts = []
        while not self.check(*stop, "EOF"):
            stmts.append(self.parse_statement())
        if "EOF" not in stop and self.check("EOF"):
            raise BetaError(f"{opener} was never closed. A king finishes the block", line)
        return stmts

    def parse_statement(self):
        tok = self.current()
        if self.check("PRINT"):
            self.advance()
            expr = self.parse_expression()
            return Print(expr, tok.line)
        if self.check("LET"):
            self.advance()
            name = self.expect("IDENT", "a Bugatti name").value
            self.expect("ASSIGN", "EQUALS")
            expr = self.parse_expression()
            return Assign(name, expr, tok.line)
        if self.check("IF"):
            self.advance()
            cond = self.parse_expression()
            self.expect("THEN", "THEN")
            then_body = self.parse_block({"ELSE", "END_IF"}, "IF", tok.line)
            else_body: list = []
            if self.check("ELSE"):
                self.advance()
                else_body = self.parse_block({"END_IF"}, "IF", tok.line)
            self.expect("END_IF", "PERIOD")
            return If(cond, then_body, else_body, tok.line)
        if self.check("WHILE"):
            self.advance()
            cond = self.parse_expression()
            body = self.parse_block({"END_WHILE"}, "GRIND WHILE", tok.line)
            self.expect("END_WHILE", "STOP GRINDING")
            return While(cond, body, tok.line)
        if self.check("FUNC"):
            self.advance()
            name = self.expect("IDENT", "a hustle name").value
            params: list[str] = []
            if self.check("WITH"):
                self.advance()
                params.append(self.expect("IDENT", "a parameter name").value)
                while self.check("AND", "COMMA"):
                    if self.tokens[self.pos + 1].kind != "IDENT":
                        break
                    self.advance()
                    params.append(self.expect("IDENT", "a parameter name").value)
            if len(params) != len(set(params)):
                raise BetaError(f"hustle '{name}' repeats a parameter. Names are not rented twice", tok.line)
            body = self.parse_block({"END_FUNC"}, "HUSTLE", tok.line)
            self.expect("END_FUNC", "DONE HUSTLING")
            return Func(name, params, body, tok.line)
        if self.check("RETURN"):
            self.advance()
            expr = self.parse_expression() if not self._next_is_statement_start() else Num(0, tok.line)
            return Return(expr, tok.line)
        if self.check("BREAK"):
            self.advance()
            return Break(tok.line)
        expr = self.parse_expression()
        return ExprStmt(expr, tok.line)

    def _next_is_statement_start(self) -> bool:
        return self.check(
            "PRINT", "LET", "IF", "WHILE", "FUNC", "RETURN", "BREAK",
            "ELSE", "END_IF", "END_WHILE", "END_FUNC", "BACK_TO_THE_MATRIX", "EOF",
        )

    def parse_expression(self):
        return self.parse_or()

    def parse_or(self):
        expr = self.parse_and()
        while self.check("OR"):
            op = self.advance()
            right = self.parse_and()
            expr = Binary(op.kind, expr, right, op.line)
        return expr

    def parse_and(self):
        expr = self.parse_cmp()
        while self.check("AND"):
            # Do not consume AND that belongs to a parameter list; that only
            # happens inside HUSTLE, which is parsed before expressions.
            op = self.advance()
            right = self.parse_cmp()
            expr = Binary(op.kind, expr, right, op.line)
        return expr

    def parse_cmp(self):
        expr = self.parse_add()
        while self.check("GT", "LT", "EQ", "NEQ"):
            op = self.advance()
            right = self.parse_add()
            expr = Binary(op.kind, expr, right, op.line)
        return expr

    def parse_add(self):
        expr = self.parse_mul()
        while self.check("PLUS", "MINUS"):
            op = self.advance()
            right = self.parse_mul()
            expr = Binary(op.kind, expr, right, op.line)
        return expr

    def parse_mul(self):
        expr = self.parse_unary()
        while self.check("TIMES", "DIV", "IDIV", "MOD"):
            op = self.advance()
            right = self.parse_unary()
            expr = Binary(op.kind, expr, right, op.line)
        return expr

    def parse_unary(self):
        if self.check("NOT", "MINUS"):
            op = self.advance()
            expr = self.parse_unary()
            return Unary(op.kind, expr, op.line)
        return self.parse_primary()

    def parse_primary(self):
        tok = self.current()
        if self.check("NUMBER"):
            self.advance()
            return Num(tok.value, tok.line)
        if self.check("STRING"):
            self.advance()
            return Str(tok.value, tok.line)
        if self.check("TRUE"):
            self.advance()
            return Bool(True, tok.line)
        if self.check("FALSE"):
            self.advance()
            return Bool(False, tok.line)
        if self.check("INPUT"):
            self.advance()
            return Input(tok.line)
        if self.check("LPAREN"):
            self.advance()
            expr = self.parse_expression()
            self.expect("RPAREN", ")")
            return expr
        if self.check("LBRACK"):
            self.advance()
            items = []
            if not self.check("RBRACK"):
                items.append(self.parse_expression())
                while self.check("COMMA"):
                    self.advance()
                    if self.check("RBRACK"):
                        break
                    items.append(self.parse_expression())
            self.expect("RBRACK", "]")
            return Seq(items, tok.line)
        if self.check("CALL"):
            self.advance()
            name = self.expect("IDENT", "a hustle name").value
            if self.check("LPAREN"):
                args = self._parse_paren_args()
            else:
                args = self._parse_call_args(tok.line)
            return Call(name, args, tok.line)
        if self.check("IDENT"):
            self.advance()
            return Var(tok.value, tok.line)
        raise BetaError(
            f"expected a value, got {tok.kind}. What color is your syntax?",
            tok.line,
        )

    def _parse_call_args(self, line: int) -> list:
        # AND or a comma separates arguments. Prefer CALL name (arg, arg) when an operator follows the call.
        args: list = []
        if self.check("WITH"):
            self.advance()
            args.append(self.parse_cmp())
            while self.check("AND", "COMMA"):
                self.advance()
                args.append(self.parse_cmp())
        return args

    def _parse_paren_args(self) -> list:
        self.expect("LPAREN", "(")
        args: list = []
        if not self.check("RPAREN"):
            args.append(self.parse_expression())
            while self.check("COMMA", "AND"):
                self.advance()
                args.append(self.parse_expression())
        self.expect("RPAREN", ")")
        return args


# ---------------------------------------------------------------------------
# Interpreter
# ---------------------------------------------------------------------------

class Environment:
    def __init__(self, parent: Environment | None = None):
        self.values: dict[str, Any] = {}
        self.parent = parent

    def declare(self, name: str, value: Any) -> None:
        self.values[name] = value

    def get(self, name: str, line: int) -> Any:
        if name in self.values:
            return self.values[name]
        if self.parent:
            return self.parent.get(name, line)
        raise BetaError(f"'{name}' is not in the garage. Declare it with BUGATTI", line)

    def set(self, name: str, value: Any) -> None:
        if name in self.values:
            self.values[name] = value
            return
        if self.parent and self.parent.has(name):
            self.parent.set(name, value)
            return
        self.values[name] = value

    def has(self, name: str) -> bool:
        return name in self.values or (self.parent is not None and self.parent.has(name))


def is_sigma(value: Any) -> bool:
    if isinstance(value, bool):
        return value
    if value is None:
        return False
    if isinstance(value, (int, float)):
        return value != 0
    if isinstance(value, str):
        return value != ""
    if isinstance(value, list):
        return len(value) != 0
    return True


def as_number(value: Any, line: int) -> int | float:
    if isinstance(value, bool):
        return 1 if value else 0
    if isinstance(value, (int, float)):
        return value
    raise BetaError(f"expected a number, got {value!r}. Numbers only, king", line)


def tidy(value: int | float) -> int | float:
    """Keep an exact whole result as an int so later MODULO and recursion stay exact."""
    if isinstance(value, float) and value.is_integer() and abs(value) < 2**53:
        return int(value)
    return value


class Interpreter:
    LOOP_LIMIT = 1_000_000
    CALL_LIMIT = 1_000

    def __init__(self, output: Callable[[str], None] | None = None, input_fn: Callable[[], str] | None = None):
        self.output = output or (lambda s: print(s, end=""))
        self.input_fn = input_fn or input
        self.globals = Environment()
        self.loop_depth = 0
        self.func_depth = 0
        self.stack: list[tuple[str, int]] = []
        sys.setrecursionlimit(max(sys.getrecursionlimit(), self.CALL_LIMIT * 12))
        self._install_builtins()

    def _install_builtins(self) -> None:
        def length(args, line):
            if len(args) != 1:
                raise BetaError("LENGTH expects one argument", line)
            value = args[0]
            if isinstance(value, (str, list)):
                return len(value)
            return len(str(value))

        def absolute(args, line):
            if len(args) != 1:
                raise BetaError("ABSOLUTE GRIND expects one argument", line)
            return abs(as_number(args[0], line))

        def floor_of(args, line):
            if len(args) != 1:
                raise BetaError("FLOOR expects one argument", line)
            return int(as_number(args[0], line) // 1)

        def at(args, line):
            if len(args) != 2:
                raise BetaError("AT expects a garage or text value and an index", line)
            target = args[0]
            if not isinstance(target, (str, list)):
                target = str(target)
            index = int(as_number(args[1], line))
            if index < 0:
                index += len(target)
            if index < 0 or index >= len(target):
                raise BetaError(f"index {args[1]!r} is outside a value of length {len(target)}", line)
            return target[index]

        def piece(args, line):
            if len(args) != 3:
                raise BetaError("PIECE expects text or a garage, a start, and an end", line)
            target = args[0]
            if not isinstance(target, (str, list)):
                target = str(target)
            start = int(as_number(args[1], line))
            end = int(as_number(args[2], line))
            return target[start:end]

        def put(args, line):
            if len(args) != 3:
                raise BetaError("PUT expects a garage, an index, and a value", line)
            if not isinstance(args[0], list):
                raise BetaError("PUT expects a garage", line)
            target = list(args[0])
            index = int(as_number(args[1], line))
            if index < 0:
                index += len(target)
            if index < 0 or index >= len(target):
                raise BetaError(f"index {args[1]!r} is outside a garage of length {len(target)}", line)
            target[index] = args[2]
            return target

        def kind(args, line):
            if len(args) != 1:
                raise BetaError("KIND expects one argument", line)
            value = args[0]
            if isinstance(value, bool):
                return "sigma"
            if isinstance(value, (int, float)):
                return "number"
            if isinstance(value, str):
                return "text"
            if isinstance(value, list):
                return "garage"
            if isinstance(value, tuple):
                return "hustle"
            return "unknown"

        def as_text(args, line):
            if len(args) != 1:
                raise BetaError("TEXT expects one argument", line)
            return Interpreter._stringify(args[0])

        def as_num(args, line):
            if len(args) != 1:
                raise BetaError("NUMBER expects one argument", line)
            value = args[0]
            if isinstance(value, bool):
                return 1 if value else 0
            if isinstance(value, (int, float)):
                return value
            if isinstance(value, str):
                try:
                    return float(value) if "." in value else int(value)
                except ValueError:
                    raise BetaError(f"cannot read a number from {value!r}", line) from None
            raise BetaError(f"cannot read a number from {value!r}", line)

        def extreme(which):
            def run(args, line, which=which):
                if not args:
                    raise BetaError(f"{which} expects at least one argument", line)
                best = args[0]
                for item in args[1:]:
                    if (item > best) if which == "MAX" else (item < best):
                        best = item
                return best
            return run

        self.globals.declare("length", ("builtin", length))
        self.globals.declare("absolute", ("builtin", absolute))
        self.globals.declare("floor", ("builtin", floor_of))
        self.globals.declare("at", ("builtin", at))
        self.globals.declare("piece", ("builtin", piece))
        self.globals.declare("put", ("builtin", put))
        self.globals.declare("kind", ("builtin", kind))
        self.globals.declare("text", ("builtin", as_text))
        self.globals.declare("number", ("builtin", as_num))
        self.globals.declare("min", ("builtin", extreme("MIN")))
        self.globals.declare("max", ("builtin", extreme("MAX")))

    def run(self, program: Program) -> None:
        self.execute_block(program.body, self.globals)

    def execute_block(self, statements: list, env: Environment) -> None:
        for stmt in statements:
            self.execute(stmt, env)

    def execute(self, stmt, env: Environment) -> None:
        try:
            self._execute(stmt, env)
        except BetaError as err:
            if self.stack and not err.stack:
                err.stack = list(self.stack)
                err.args = (str(err).split("\n")[0] + "\n" + "\n".join(
                    f"  in hustle {name} on line {lineno}" for name, lineno in err.stack
                ),)
            raise

    def _execute(self, stmt, env: Environment) -> None:
        if isinstance(stmt, Print):
            value = self.eval(stmt.expr, env)
            self.output(self._stringify(value) + "\n")
            return
        if isinstance(stmt, Assign):
            env.declare(stmt.name, self.eval(stmt.expr, env))
            return
        if isinstance(stmt, If):
            branch = stmt.then_body if is_sigma(self.eval(stmt.cond, env)) else stmt.else_body
            self.execute_block(branch, env)
            return
        if isinstance(stmt, While):
            spins = 0
            self.loop_depth += 1
            try:
                while is_sigma(self.eval(stmt.cond, env)):
                    spins += 1
                    if spins > self.LOOP_LIMIT:
                        raise BetaError(
                            f"grind ran past {self.LOOP_LIMIT} turns. ESCAPE THE GRIND, or the condition is beta",
                            stmt.line,
                        )
                    try:
                        self.execute_block(stmt.body, env)
                    except EscapeGrind:
                        break
            finally:
                self.loop_depth -= 1
            return
        if isinstance(stmt, Func):
            env.declare(stmt.name, ("user", stmt.params, stmt.body, env))
            return
        if isinstance(stmt, Return):
            if self.func_depth == 0:
                raise BetaError("CASH OUT outside a hustle. There is nothing to cash", stmt.line)
            raise CashOut(self.eval(stmt.expr, env))
        if isinstance(stmt, Break):
            if self.loop_depth == 0:
                raise BetaError("ESCAPE THE GRIND outside a grind. There is no grind to escape", stmt.line)
            raise EscapeGrind()
        if isinstance(stmt, ExprStmt):
            self.eval(stmt.expr, env)
            return
        raise BetaError("unknown statement. The Matrix is confused", getattr(stmt, "line", None))

    def eval(self, expr, env: Environment) -> Any:
        if isinstance(expr, Num):
            return expr.value
        if isinstance(expr, Str):
            return expr.value
        if isinstance(expr, Bool):
            return expr.value
        if isinstance(expr, Seq):
            return [self.eval(item, env) for item in expr.items]
        if isinstance(expr, Input):
            try:
                raw = self.input_fn()
            except EOFError:
                return ""
            raw = raw.rstrip("\n")
            try:
                if "." in raw:
                    return float(raw)
                return int(raw)
            except ValueError:
                return raw
        if isinstance(expr, Var):
            return env.get(expr.name, expr.line)
        if isinstance(expr, Unary):
            value = self.eval(expr.expr, env)
            if expr.op == "NOT":
                return not is_sigma(value)
            if expr.op == "MINUS":
                return -as_number(value, expr.line)
        if isinstance(expr, Binary):
            return self._binary(expr, env)
        if isinstance(expr, Call):
            return self._call(expr, env)
        raise BetaError("unknown expression", getattr(expr, "line", None))

    def _binary(self, expr: Binary, env: Environment) -> Any:
        # Short-circuit logic, as a top G does not waste motion.
        if expr.op == "AND":
            left = self.eval(expr.left, env)
            if not is_sigma(left):
                return False
            return is_sigma(self.eval(expr.right, env))
        if expr.op == "OR":
            left = self.eval(expr.left, env)
            if is_sigma(left):
                return True
            return is_sigma(self.eval(expr.right, env))

        left = self.eval(expr.left, env)
        right = self.eval(expr.right, env)
        line = expr.line

        if expr.op == "PLUS":
            if isinstance(left, list) and isinstance(right, list):
                return left + right
            if isinstance(left, list):
                return left + [right]
            if isinstance(right, list):
                return [left] + right
            if isinstance(left, str) or isinstance(right, str):
                return self._stringify(left) + self._stringify(right)
            return tidy(as_number(left, line) + as_number(right, line))
        if expr.op == "MINUS":
            return tidy(as_number(left, line) - as_number(right, line))
        if expr.op == "TIMES":
            if isinstance(left, str) and isinstance(right, (int, float)) and not isinstance(right, bool):
                count = int(right)
                if count < 0:
                    raise BetaError("a string cannot be repeated a negative number of times", line)
                return left * count
            if isinstance(right, str) and isinstance(left, (int, float)) and not isinstance(left, bool):
                count = int(left)
                if count < 0:
                    raise BetaError("a string cannot be repeated a negative number of times", line)
                return right * count
            return tidy(as_number(left, line) * as_number(right, line))
        if expr.op == "DIV":
            denom = as_number(right, line)
            if denom == 0:
                raise BetaError("division by zero. Even a Bugatti stops for that", line)
            return tidy(as_number(left, line) / denom)
        if expr.op == "IDIV":
            denom = as_number(right, line)
            if denom == 0:
                raise BetaError("split by zero. Even a Bugatti stops for that", line)
            return int(as_number(left, line) // denom)
        if expr.op == "MOD":
            denom = as_number(right, line)
            if denom == 0:
                raise BetaError("modulo by zero. Beta arithmetic", line)
            return tidy(as_number(left, line) % denom)
        if expr.op == "GT":
            return self._cmp(left, right, line) > 0
        if expr.op == "LT":
            return self._cmp(left, right, line) < 0
        if expr.op == "EQ":
            return left == right
        if expr.op == "NEQ":
            return left != right
        raise BetaError(f"unknown operator {expr.op}", line)

    def _cmp(self, left: Any, right: Any, line: int) -> int:
        if isinstance(left, str) and isinstance(right, str):
            return (left > right) - (left < right)
        return (as_number(left, line) > as_number(right, line)) - (as_number(left, line) < as_number(right, line))

    def _call(self, expr: Call, env: Environment) -> Any:
        target = env.get(expr.name, expr.line)
        args = [self.eval(arg, env) for arg in expr.args]
        if not isinstance(target, tuple):
            raise BetaError(f"'{expr.name}' is not a hustle. You cannot call a Bugatti", expr.line)
        if target[0] == "builtin":
            return target[1](args, expr.line)
        _, params, body, closure = target
        if len(args) != len(params):
            raise BetaError(
                f"hustle '{expr.name}' expects {len(params)} argument(s), got {len(args)}",
                expr.line,
            )
        local = Environment(closure)
        for name, value in zip(params, args):
            local.declare(name, value)
        if self.func_depth >= self.CALL_LIMIT:
            raise BetaError(f"hustle nested past {self.CALL_LIMIT}. Cash out earlier", expr.line)
        self.func_depth += 1
        self.stack.append((expr.name, expr.line))
        try:
            self.execute_block(body, local)
        except CashOut as cash:
            return cash.value
        finally:
            self.func_depth -= 1
            self.stack.pop()
        return 0

    @staticmethod
    def _stringify(value: Any) -> str:
        if isinstance(value, bool):
            return "SIGMA" if value else "BETA"
        if isinstance(value, float):
            if value.is_integer():
                return str(int(value))
            return f"{value:.10g}"
        if isinstance(value, list):
            return "[" + ", ".join(Interpreter._stringify(item) for item in value) + "]"
        return str(value)


def execute_source(source: str, output: Callable[[str], None] | None = None, input_fn: Callable[[], str] | None = None) -> None:
    tokens = Lexer(source).tokenize()
    program = Parser(tokens).parse()
    try:
        Interpreter(output=output, input_fn=input_fn).run(program)
    except RecursionError:
        raise BetaError("the hustle recursed until the stack quit. Cash out earlier") from None


def repl() -> None:
    print("Cobratate REPL. Escape the Matrix. Type PERIOD on its own line to run a block.")
    print("Commands: :quit  :help")
    buffer: list[str] = []
    while True:
        try:
            prompt = "... " if buffer else "topg> "
            line = input(prompt)
        except EOFError:
            print()
            return
        stripped = line.strip()
        if not buffer and stripped in {":quit", ":exit", "BACK TO THE MATRIX"}:
            print("Back to the Matrix.")
            return
        if not buffer and stripped == ":help":
            print("BUGATTI name EQUALS expr")
            print("WHAT COLOR IS YOUR BUGATTI expr")
            print("IF expr THEN ... OTHERWISE YOU ARE A BETA ... PERIOD")
            print("GRIND WHILE expr ... STOP GRINDING")
            print("HUSTLE name WITH a AND b ... CASH OUT expr ... DONE HUSTLING")
            print("CALL name WITH expr AND expr")
            continue
        buffer.append(line)
        # Run immediately on a complete single line, or when the user closes a block.
        joined = "\n".join(buffer)
        closers = ("STOP GRINDING", "DONE HUSTLING", "PERIOD", "BACK TO THE MATRIX")
        openers = ("GRIND WHILE", "HUSTLE ", "IF ")
        upper = joined.upper()
        pending = any(k in upper for k in ("GRIND WHILE", "HUSTLE ", "IF ")) and not any(
            upper.rstrip().endswith(c) for c in closers
        )
        if pending and stripped.upper() not in closers:
            continue
        try:
            execute_source(joined)
        except BetaError as err:
            print(err)
        buffer = []


def main(argv: list[str]) -> int:
    args = argv[1:]
    if not args:
        repl()
        return 0
    if args[0] in {"-h", "--help"}:
        print(f"Cobratate {VERSION}")
        print("Usage: cobratate.py [program.cbt]")
        print("       cobratate.py -c CODE")
        print("       cobratate.py --version")
        print("With no file, start the REPL.")
        return 0
    if args[0] in {"-V", "--version"}:
        print(f"Cobratate {VERSION}")
        return 0
    if args[0] == "-c":
        if len(args) != 2:
            print("Usage: cobratate.py -c CODE", file=sys.stderr)
            return 2
        try:
            execute_source(args[1])
        except BetaError as err:
            print(err, file=sys.stderr)
            return 1
        return 0
    if len(args) != 1:
        print("Usage: cobratate.py [program.cbt]", file=sys.stderr)
        return 2
    path = args[0]
    try:
        with open(path, encoding="utf-8") as handle:
            source = handle.read()
    except OSError as err:
        print(f"Beta behavior detected: cannot open {path}: {err}", file=sys.stderr)
        return 1
    try:
        execute_source(source)
    except BetaError as err:
        print(err, file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
