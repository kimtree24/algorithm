import sys
input = sys.stdin.readline

n = int(input())
sol_list = list(map(int, input().strip().split()))

left, right = 0, n - 1
best_value = abs(sol_list[left] + sol_list[right])
ans = (sol_list[left], sol_list[right])

while left < right:
    cur_value = sol_list[left] + sol_list[right]

    if abs(cur_value) < best_value:
        best_value = abs(cur_value)
        ans = (sol_list[left], sol_list[right])

    if cur_value < 0:
        left += 1
    else:
        right -= 1
print(*ans)