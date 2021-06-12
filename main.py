# team members: Sharon Vazana, Hadar Amsalem

# simpson methods
# שרונית סימפסון עובד, רומברג לא.. יש רק התחלה שלו

import math


def simpson(f ,startPoint, endPoint ,parts):
    if parts % 2 == 1:
        print("the parts need to be zogi")
        return None
    gap = abs(endPoint-startPoint)/parts
    appr = f(startPoint)
    for i in range(1, parts):
        if i % 2 == 0:
            appr += 2 * f((i * gap)+startPoint)
        else:
            appr += 4 * f((i * gap) + startPoint)
    appr += f(endPoint)
    appr *= 1 / 3 * gap
    return appr


def romberg(f ,startPoint, endPoint, epsilon = 0.0001):
    apprF = iterationRom(f ,startPoint, endPoint, 1)
    apprS = iterationRom(f ,startPoint, endPoint, 2)
    apprT = iterationRom(f ,startPoint, endPoint, 3)
    R1 = apprS + 1/3 * (apprS-apprF)
    R2 = apprT + 1/3 * (apprT-apprS)
    i  =4
    while R1-R2 > epsilon:
        apprS = apprT
        apprT = apprT = iterationRom(f ,startPoint, endPoint, i)
        i += 1
        R1 = R2
        R2 = apprT + 1 / 3 * (apprT - apprS)
    return R2


def iterationRom(f ,startPoint, endPoint, parts):
    gap = abs(endPoint - startPoint) / parts
    appr = f(startPoint)
    div = 2
    for i in range(1, parts):
        appr += 2 * f(startPoint + endPoint / div)
        div += div
    appr += f(endPoint)
    appr *= 1 / div * endPoint
    return appr


def errorCalculation(f, calc, parts, endPoint, startPoint):
    gap = abs(endPoint - startPoint) / parts
    return 1/180 * math.pow(gap, parts) * (endPoint-startPoint) * f(1)


def driver():
    """
    the main function of the program
    """
    f = math.sin

    # define range
    startPoint = 0
    endPoint = math.pi
    calc = simpson(f, startPoint, endPoint, 4)
    print(calc)
    print(iterationRom(f ,startPoint, endPoint, 5))
    print(calc)
    print(errorCalculation(f, calc, 4, endPoint, startPoint))


driver()
