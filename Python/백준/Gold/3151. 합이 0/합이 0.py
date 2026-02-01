import sys

input = sys.stdin.readline

n = int(input().strip())
students = sorted(map(int, input().strip().split()))
ans = 0

for i in range(n - 2):
    cur = students[i]
    left, right = i + 1, n - 1

    while left < right:
        temp = cur + students[left] + students[right]

        if temp == 0:
            if students[left] == students[right]:
                cnt = right - left + 1
                ans += cnt * (cnt - 1) // 2
                break
            else:
                l_cnt, r_cnt = 1, 1
                while left + 1 < right and students[left] == students[left + 1]:
                    left += 1
                    l_cnt += 1
                while right - 1 > left and students[right] == students[right - 1]:
                    right -= 1
                    r_cnt += 1
                ans += l_cnt * r_cnt
                left += 1
                right -= 1
        elif temp < 0:
            left += 1
        else:
            right -= 1
print(ans)