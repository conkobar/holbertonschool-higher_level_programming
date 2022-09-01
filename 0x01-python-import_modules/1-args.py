#!/usr/bin/python3

if __name__ == "__main__":
    # print number of args given
    import sys

    args = (len(sys.argv) - 1)

    if args == 0:
        print("{:d} arguments.".format(0, sys.argv[args]))

    if args == 1:
        print("{:d} argument:".format(1))

    if args > 1:
        print("{:d} arguments:".format(args))

    for i in range(1, (args + 1)):
        print("{:d}: {}".format(i, sys.argv[i]))
