import time

n = int(input("Veuillez saisir un nombre : "))



def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n >= 2:
        print(time.time())
        return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(n))
