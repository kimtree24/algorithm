import sys
n, c = map(int, sys.stdin.readline().rstrip().split())
data = list(map(int, sys.stdin.readline().rstrip().split()))
data.sort()

def binary(start, end, data, c):
    while start<=end :
        mid = (start+end)//2
        if data[mid] == c:
            return 1
        elif data[mid] < c:
            start = mid+1
        else:
            end = mid - 1
    return 0

def sol(n, c, data):
    if binary(0, n-1, data, c) == 1:
        return True
    pointer1 = 0
    pointer2 = n-1
    while(pointer1 < pointer2):
        tempSum = data[pointer1] + data[pointer2]
        if tempSum > c:
            pointer2 -=1
        elif tempSum == c:
            return True
        else:
            temptempSum = c - tempSum
            if temptempSum != data[pointer1] and temptempSum != data[pointer2] and binary(0, n-1, data, temptempSum) == 1:
                return True
            pointer1 += 1
    return False

if sol(n, c, data):
    print(1)
else:
    print(0)