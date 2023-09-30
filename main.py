def solveForA(p, r, n, t):
    return "$" + str(round(p * (1 + (r/100) ) ** (t * n), 2))
def solveForP(a, r, n):
    return "$" + str(round(a / ((1 + r/100 ) ** n), 2))

what = input("Enter 'p' to solve for principal value, 'a' to solve for final value (enter without quotes).\n")
def solving(what):
    if what.lower() == "a":
        p = input("What is the principal value of the sum in dollars?\n")
        p = float(p)
        r = input("What is the interest rate in percent?\n")
        r = float(r)
        n = input("How many years?\n")
        n = float(n)
        t = input("How many times compounded annually? (Enter 'c' without quotes for continuous compounding.)\n")
        if t == "c":
            print("$",round(p * (2.7182818 ** (r/100 * n)), 2))
        else:
            t = float(t)
            result = solveForA(p, r, n, t)
            print(result)
    elif what.lower() == "p":
        a = input("What is the final value of the sum in dollars?\n")
        a = float(a)
        r = input("What is the interest rate in percent?\n")
        r = float(r)
        n = input("How many years?\n")
        n = float(n)
        t = input("How many times compounded annually? (Enter 'c' without quotes for continuous compounding.)\n")
        if t == "c":
            print("$", round(a / (2.7182818 ** (r / 100 * n)), 2))
        else:
            t = float(t)
            result = solveForP(a, r, n, t)
            print(result)

solving(what)