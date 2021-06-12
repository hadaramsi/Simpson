# team members: Sharon Vazana, Hadar Amsalem

# simpson methods


import math
import sympy as sp
from sympy.utilities.lambdify import lambdify


def simpson(f, startPoint, endPoint, parts):
    """
    :param f: original function
    :param startPoint: start of range
    :param endPoint: end of range
    :param parts: amount of segments
    :return: approximate area of the integral
    """
    if parts % 2 == 1:
        print("Amount of parts must be even")
        return None
    x = sp.symbols('x')
    func = lambdify(x, f)
    gap = abs(endPoint - startPoint) / parts
    appr = func(startPoint)
    for i in range(1, parts):
        if i % 2 == 0:
            appr += 2 * func((i * gap) + startPoint)
        else:
            appr += 4 * func((i * gap) + startPoint)
    appr += func(endPoint)
    appr *= 1 / 3 * gap
    return appr


def errorCalculation(f, parts, endPoint, startPoint):
    """
    :param f: original function
    :param parts: amount of segments
    :param endPoint: end of range
    :param startPoint: start of range
    :return: value of error
    """
    x = sp.symbols('x')
    gap = abs(endPoint - startPoint) / parts
    func = calcDerived(calcDerived(calcDerived(calcDerived(f))))
    ksi = findUpperBound(func)
    if ksi is None:
        print("Couldn't calculate the error")
        return
    fourthDerivative = lambdify(x, func)
    return 1 / 180 * math.pow(gap, 4) * (endPoint - startPoint) * fourthDerivative(ksi)


def findUpperBound(f):
    """
    :return: estimated upper bound
    """
    x = sp.symbols('x')
    fTag = calcDerived(f)
    s = sp.solve(fTag)
    func = lambdify(x, f)
    if len(s) > 0:
        maximum = func(s[0])
        for i in range(1, len(s)):
            if func(s[i]) > maximum:
                maximum = func(s[i])
        return maximum
    return None


def calcDerived(f):
    """
    :param f: original func
    :return: the derived without lambdify
    """
    # calc the derivative from func -> lambdify
    x = sp.symbols('x')
    f_prime = f.diff(x)
    return f_prime


def driver():
    """
    the main function of the program
    """
    x = sp.symbols('x')

    # define function
    f = sp.sin(x)

    # define range
    startPoint = 0
    endPoint = math.pi

    print(simpson(f, startPoint, endPoint, 4))
    print(errorCalculation(f, 4, endPoint, startPoint))


driver()
