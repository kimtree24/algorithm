import sys
input = sys.stdin.readline

n = int(input())
array = [input().strip() for _ in range(n)]

def solution(array):
    array = list(set(array))
    sorted_array = sorted(array, key = lambda x : (len(x),x))
    return sorted_array

ans = solution(array)

for word in ans:
    print(word)