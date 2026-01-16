import sys

input = sys.stdin.readline

first_line = input().strip().split()
n = int(first_line[0])

nums = first_line[1:]

while len(nums) < n:
    nums.extend(input().strip().split())

rev = []
for num in nums:
    r_num = int(num[::-1].lstrip("0"))
    rev.append(r_num)
rev.sort()

for r in rev:
    print(r)