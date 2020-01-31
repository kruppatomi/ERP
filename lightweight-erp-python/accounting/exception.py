def divide(a, b):
    if b == 0:
        raise ZeroDivisionError
    return a / b


try:
    print(divide(10, 0))

except ZeroDivisionError:
    print("Invalid argument")