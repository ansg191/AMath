from amath.DataTypes import Fraction, Function
from amath.constants import inf
from .mean import mean


def slope(x1, y1, x2, y2):
    dx = x1 - x2
    dy = y1 - y2
    if dx == 0:
        return inf
    return Fraction(dy, dx)


def Sum(f, i=None, maximum=None, step=1, l=None):
    try:
        if type(f(2)) != float:
            if type(f(2)) != int:
                raise ValueError("Function must return float or integer value")
    except TypeError:
        raise TypeError("f must be a function")

    if i is not None:
        if maximum is not None:
            if l is not None:
                raise TypeError("Invalid Argument")
    if i is None:
        if maximum is None:
            if l is None:
                raise TypeError("Invalid Argument")

    if l is None:
        x = 0
        while i <= maximum:
            x += f(i)
            i += step
        return x
    else:
        x = 0
        for y in l:
            x += f(y)
        return x


def Product(f, i=None, maximum=None, step=1, l=None):
    try:
        if type(f(2)) != float:
            if type(f(2)) != int:
                raise ValueError("Function must return float or integer value")
    except TypeError:
        raise TypeError("f must be a function")

    if i is not None:
        if maximum is not None:
            if l is not None:
                raise TypeError("Invalid Argument")
            else:
                raise TypeError("Invalid Argument")
    if i is None:
        if maximum is None:
            if l is None:
                raise TypeError("Invalid Argument")
            else:
                raise TypeError("Invalid Argument")

    if l is None:
        x = 0
        while i <= maximum:
            x *= f(i)
            i += step
        return x
    elif i is not None:
        x = 0
        for y in l:
            x *= f(y)
        return x


def linregress(inp, output):
    if not isinstance(inp, list):
        raise TypeError("Input must be a list")
    if not isinstance(output, list):
        raise TypeError("Input must be a list")

    if len(inp) != len(output):
        raise TypeError("Lists must be of the same size")

    z = 0
    a = 0
    i = 0
    xm = mean(inp)
    ym = mean(output)
    for item in inp:
        z += (item - xm) * (output[i] - ym)
        i += 1

    for item in inp:
        a += (item - xm)**2

    m = z/a

    b = ym - (m * xm)

    return Function("x", "{0}x + {1}".format(m, b))
