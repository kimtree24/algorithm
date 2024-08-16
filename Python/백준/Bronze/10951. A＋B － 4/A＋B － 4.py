import sys
while True:
    line = sys.stdin.readline().rstrip()
    if not line:
        break
    a, b = map(int, line.split())
    print(a + b)