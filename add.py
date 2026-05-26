"""Simple addition utility

Usage:
  python add.py 2 3   # prints 5
  python add.py        # prompts for two numbers
"""
import sys


def add(a, b):
    """Return the sum of a and b as numbers (int or float)."""
    return a + b


def _to_number(s):
    try:
        if "." in s:
            return float(s)
        return int(s)
    except Exception:
        return float(s)


if __name__ == "__main__":
    if len(sys.argv) >= 3:
        x = _to_number(sys.argv[1])
        y = _to_number(sys.argv[2])
    else:
        x = _to_number(input("Enter first number: ").strip())
        y = _to_number(input("Enter second number: ").strip())
    result = add(x, y)
    # print without trailing .0 for integer-looking floats
    if isinstance(result, float) and result.is_integer():
        print(int(result))
    else:
        print(result)
