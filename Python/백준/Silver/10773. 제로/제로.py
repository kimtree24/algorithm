import sys
input = sys.stdin.readline

k = int(input().strip())

stack = []

for i in range(k):
    num = int(input().strip())
    if num == 0 and stack:
        stack.pop()
    else:
        stack.append(num)
print(sum(stack))