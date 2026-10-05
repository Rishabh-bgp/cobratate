"""Regression checks for the Cobratate interpreter."""

import unittest
import cobratate


def run(source: str, stdin: list[str] | None = None) -> str:
    lines = list(stdin or [])

    def read() -> str:
        if not lines:
            raise EOFError
        return lines.pop(0)

    out: list[str] = []
    cobratate.execute_source(source, output=out.append, input_fn=read)
    return "".join(out)


class CobratateTests(unittest.TestCase):
    def test_exact_division_stays_integral(self):
        self.assertEqual(run('WHAT COLOR IS YOUR BUGATTI 42 DIVIDED BY 2'), "21\n")

    def test_split_by_floors(self):
        self.assertEqual(run('WHAT COLOR IS YOUR BUGATTI 7 SPLIT BY 2'), "3\n")

    def test_parenthesized_call_does_not_swallow_plus(self):
        source = '''
        HUSTLE id WITH n
          CASH OUT n
        DONE HUSTLING
        WHAT COLOR IS YOUR BUGATTI CALL id (2) PLUS "!"
        '''
        self.assertEqual(run(source), "2!\n")

    def test_comma_arguments(self):
        source = '''
        HUSTLE add WITH a AND b
          CASH OUT a PLUS b
        DONE HUSTLING
        WHAT COLOR IS YOUR BUGATTI CALL add (20, 22)
        '''
        self.assertEqual(run(source), "42\n")

    def test_local_assignment_does_not_leak(self):
        source = '''
        BUGATTI wealth EQUALS 1
        HUSTLE touch
          BUGATTI wealth EQUALS 99
          CASH OUT wealth
        DONE HUSTLING
        WHAT COLOR IS YOUR BUGATTI CALL touch
        WHAT COLOR IS YOUR BUGATTI wealth
        '''
        self.assertEqual(run(source), "99\n1\n")

    def test_index_and_slice(self):
        source = '''
        WHAT COLOR IS YOUR BUGATTI CALL at WITH "cobra" AND 0
        WHAT COLOR IS YOUR BUGATTI CALL at ("cobra", MINUS 1)
        WHAT COLOR IS YOUR BUGATTI CALL piece ("cobratate", 0, 5)
        '''
        self.assertEqual(run(source), "c\na\ncobra\n")

    def test_unclosed_block(self):
        with self.assertRaises(cobratate.BetaError) as caught:
            run("GRIND WHILE SIGMA\nWHAT COLOR IS YOUR BUGATTI 1")
        self.assertIn("never closed", str(caught.exception))

    def test_break_and_return_out_of_place(self):
        with self.assertRaises(cobratate.BetaError):
            run("ESCAPE THE GRIND")
        with self.assertRaises(cobratate.BetaError):
            run("CASH OUT 1")

    def test_division_by_zero_and_bad_index(self):
        with self.assertRaises(cobratate.BetaError):
            run("WHAT COLOR IS YOUR BUGATTI 1 DIVIDED BY 0")
        with self.assertRaises(cobratate.BetaError):
            run('WHAT COLOR IS YOUR BUGATTI CALL at WITH "ab" AND 5')

    def test_loop_limit(self):
        original = cobratate.Interpreter.LOOP_LIMIT
        cobratate.Interpreter.LOOP_LIMIT = 20
        try:
            with self.assertRaises(cobratate.BetaError) as caught:
                run("GRIND WHILE SIGMA\nBUGATTI x EQUALS 1\nSTOP GRINDING")
        finally:
            cobratate.Interpreter.LOOP_LIMIT = original
        self.assertIn("grind ran past", str(caught.exception))

    def test_call_limit(self):
        source = '''
        HUSTLE forever WITH n
          CASH OUT CALL forever WITH n PLUS 1
        DONE HUSTLING
        WHAT COLOR IS YOUR BUGATTI CALL forever WITH 0
        '''
        with self.assertRaises(cobratate.BetaError) as caught:
            run(source)
        self.assertIn("nested past", str(caught.exception))

    def test_garage_and_kind(self):
        source = '''
        BUGATTI g EQUALS [2, 3, 5]
        WHAT COLOR IS YOUR BUGATTI CALL at (g, MINUS 1)
        WHAT COLOR IS YOUR BUGATTI g PLUS [7]
        WHAT COLOR IS YOUR BUGATTI CALL kind WITH g
        WHAT COLOR IS YOUR BUGATTI CALL max (2, 9, 4)
        '''
        self.assertEqual(run(source), "5\n[2, 3, 5, 7]\ngarage\n9\n")

    def test_put_returns_a_new_garage(self):
        source = '''
        BUGATTI row EQUALS [1, 2, 3]
        WHAT COLOR IS YOUR BUGATTI CALL put (row, 1, 9)
        WHAT COLOR IS YOUR BUGATTI row
        '''
        self.assertEqual(run(source), "[1, 9, 3]\n[1, 2, 3]\n")

    def test_version_constant(self):
        self.assertEqual(cobratate.VERSION, "1.2.0")

        self.assertTrue(cobratate.VERSION)

    def test_input_number_and_text(self):
        source = '''
        BUGATTI a EQUALS ASK THE MATRIX
        BUGATTI b EQUALS ASK THE MATRIX
        WHAT COLOR IS YOUR BUGATTI a PLUS 1
        WHAT COLOR IS YOUR BUGATTI b PLUS "!"
        '''
        self.assertEqual(run(source, ["41\n", "king\n"]), "42\nking!\n")


if __name__ == "__main__":
    unittest.main()
