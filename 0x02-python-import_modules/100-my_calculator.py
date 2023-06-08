#!/usr/bin/python3

if __name__ == "__main__":
    """Build my own calculator!"""
    import sys
    from calculator_1 import mul, sub, add, div

    op = '+*/-'
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    if sys.argv[2] not in op:
        print("Unknown operator. Available operators: +, -, * and / ")
        sys.exit(1)

    dict = {'*': mul(int(sys.argv[1]), int(sys.argv[3])),
            '-': sub(int(sys.argv[1]), int(sys.argv[3])),
            '+': add(int(sys.argv[1]), int(sys.argv[3])),
            '/': div(int(sys.argv[1]), int(sys.argv[3])),
            }

    for key, value in dict.items():
        if key == sys.argv[2]:
            print(value)
