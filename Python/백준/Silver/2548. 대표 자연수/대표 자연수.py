import sys

n = int(input())
list_num = list(map(int, sys.stdin.readline().rstrip().split()))


def represent_num(n, list_num):
    list_num.sort()
    print(list_num[(n-1)//2])
    

represent_num(n, list_num)