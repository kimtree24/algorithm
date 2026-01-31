import sys
input = sys.stdin.readline

n = int(input())
pos = []
neg = []
ones = 0
zero = 0

for _ in range(n):
    x = int(input())
    if x > 1:
        pos.append(x)
    elif x == 1:
        ones += 1
    elif x == 0:
        zero += 1
    else:
        neg.append(x)

pos.sort(reverse=True)
neg.sort()

result = 0

# 양수 처리
i = 0
while i < len(pos):
    if i + 1 < len(pos):
        result += pos[i] * pos[i+1]
        i += 2
    else:
        result += pos[i]
        i += 1

# 음수 처리
i = 0
while i < len(neg):
    if i + 1 < len(neg):
        result += neg[i] * neg[i+1]
        i += 2
    else:
        # 남은 음수 하나
        if zero == 0:
            result += neg[i]
        i += 1

# 1은 그냥 더함
result += ones

print(result)