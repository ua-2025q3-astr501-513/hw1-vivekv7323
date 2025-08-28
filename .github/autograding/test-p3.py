# This is a pytest script to test quadratic() from part 3.
# This function should be imported from the solution file.

from math import isclose
from hw1.p3 import quadratic

# -----------------------------------------------------------------------------
# Test functions for quadratic().

def test_catastrophic_cancellation():
    """Test the quadratic() function by verifying that it can compute
    accurately both roots when catastrophic cancellation may happen.

    """
    t1, t2  = 1e-8, 1e8
    a, b, c = 1.0, -t1-t2, 1.0
    x1, x2  = quadratic(a, b, c)

    print("Catastrophic Cancellation")
    print(f"{a=}, {b=}, {c=}")
    print(f"{t1=}, {t2=}")
    print(f"{x1=}, {x2=}")

    assert isclose(x1, t1)
    assert isclose(x2, t2)

def test_one_root():
    """Test the quadratic() function by verifying x2 == None when
    there is only one real root.

    """
    t1, t2  = 1.0, None
    a, b, c = 1.0, -2.0, 1.0
    x1, x2  = quadratic(a, b, c)

    print("One Root")
    print(f"{a=}, {b=}, {c=}")
    print(f"{t1=}, {t2=}")
    print(f"{x1=}, {x2=}")

    assert isclose(x1, t1)
    assert x2 is None

def test_no_root():
    """Test the quadratic() function by verifying x1 == x2 == None
    when there is no real root.

    """
    t1, t2  = None, None
    a, b, c = 1.0, -1.0, 1.0
    x1, x2  = quadratic(a, b, c)

    print("No Root")
    print(f"{a=}, {b=}, {c=}")
    print(f"{t1=}, {t2=}")
    print(f"{x1=}, {x2=}")

    assert x1 is None
    assert x2 is None
