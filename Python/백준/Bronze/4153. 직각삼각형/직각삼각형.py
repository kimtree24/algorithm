import sys

while True:
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    if a == 0 and b == 0 and c == 0:
        break
    a, b, c = sorted([a,b,c])
    if (pow(a,2)+pow(b,2) == pow(c,2)):
        print("right")
    else:
        print("wrong")