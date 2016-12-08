def add(x, y):
    return x + y

# This should have been added as feature2 but added under divide now


def subtract(x, y):
    return x - y


# test 2345
def multiply(x, y):
    return x * y


def divide(x, z):
    return x / z

# Extra linefeeds added
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
