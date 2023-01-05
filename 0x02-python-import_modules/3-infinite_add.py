#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

# -1 cause the first arg is file name
sum = 0
count = len(argv) - 1
for i in range(1, count + 1):
    sum += int(i)
print (sum)
