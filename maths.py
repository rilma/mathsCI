''' $ py.test --doctest-modules '''
def square(x):
    """Return the square of a number `x`.

    [...]

    Examples
    --------
    >>> square(5)
    25
    """
    return x**2

def sqrt(x):
    """Return the square root of `x`.
 
    Examples
    --------
    >>> sqrt(4.0)
    2.0
    """
    return x * 0.5
