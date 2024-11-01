def add (*args):
    total = 0
    for n in args:
        total = total + n
    return total

print(add(1,2,3))

def calculate(n, **kwargs):
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2, add=3, multiply=5)