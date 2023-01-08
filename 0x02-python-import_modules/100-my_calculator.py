#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    from calculator_1 import add, div, mul, sub
if len(argv) != 4:
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    exit(1)

operator = argv[2]

ops = {"+": add, "-": sub, "*": mul, "/": div}
if operator not in list(ops.keys()):
    print("Unknown operator. Available operators: +, -, * and /")
    exit(1)

a = int(argv[1])
b = int(argv[3])

result = ops[operator](a, b)
print("{} {} {} = {}".format(a, operator, b, result))
