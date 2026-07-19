import pdb

# ── Sample program with a deliberate bug ────────────────────────────────────

def divide(a, b):
    return a / b          # ZeroDivisionError when b == 0

def average(numbers):
    total = sum(numbers)
    count = len(numbers)
    return divide(total, count)

# ── 1. Normal run (works fine) ───────────────────────────────────────────────
result = average([10, 20, 30])
print(f'Average of [10, 20, 30] = {result}')

# ── 2. Post-mortem debugging with pdb.post_mortem() ─────────────────────────
# pdb.pm() relies on sys.last_exc which was removed in Python 3.14.
# Use pdb.post_mortem() with an explicit try/except instead — works on all versions.
#
# Useful pdb commands inside post-mortem:
#   l  (list)   — show source around current line
#   p <expr>    — print a value  (e.g.  p a  or  p b)
#   u  (up)     — move up one frame in the call stack
#   d  (down)   — move down one frame
#   q  (quit)   — exit pdb

import sys, traceback

try:
    result2 = average([])    # empty list → ZeroDivisionError
    print(f'Average of [] = {result2}')
except Exception:
    traceback.print_exc()
    print('\n--- Entering post-mortem debugger ---')
    pdb.post_mortem(sys.exc_info()[2])
