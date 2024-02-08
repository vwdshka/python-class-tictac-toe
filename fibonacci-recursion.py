import random
n = random.randint(1, 10)
l = 25

print("The random integer is: ", n)

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print("Fibonacci sequence:")

def printOut():
    for i in range(l):
        print(fibonacci(i), end=' ')

printOut()