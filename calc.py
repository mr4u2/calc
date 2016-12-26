def add(x, y):
    return x + y

# This should have been added as feature2 but added under divide now

# This is added in Calc2 clone ----and now this again in Calc----- and modified in Calc later!!!

def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, z):
    return x / z

# Extra line feeds added
# Nu weer in subtract
# Added in divide
# test stash


# New function for bbb
def bbb(x):
    res = []
    a, b = 0, 1
    for i in range(x):
        res.append(a)
        a, b = b, a + b
    return res

# again bbb
