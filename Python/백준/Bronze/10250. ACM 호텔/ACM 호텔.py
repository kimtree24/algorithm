import sys
t = int(input())
for i in range(t):
    h, w, n = map(int, sys.stdin.readline().rstrip().split())
    result_h = n % h
    result_w = n // h
    if result_h !=0:
        print(result_h * 100 + result_w+1)
    else:
        print(h*100 + result_w)