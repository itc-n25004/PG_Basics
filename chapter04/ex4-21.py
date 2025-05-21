a = input("type a number:")
b = input("type a number:")
a = int(a)
b = int(b)
try:
    print(a / b)
except(ZeroDivisionError, ValueError):
    print("invaid input")
