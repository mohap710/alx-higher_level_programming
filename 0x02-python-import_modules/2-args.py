#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

# -1 cause the first arg is file name
count = len(argv) - 1
if count == 0:
    print("0 arguments.")
if count == 1:
    print("1 argument:")
else:
    print("{} arguments:".format(count))

for i in range(1, count + 1):
    print("{}: {}".format(i, argv[i]))
