import sys
n, m = map(int, sys.stdin.readline().rstrip().split())
card = list(map(int, sys.stdin.readline().rstrip().split()))
card = sorted(card, reverse = True)

max_sum = 0

for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            cur_sum = (card[i]+card[k]+card[j])
            if (cur_sum <=m):
                max_sum = max(max_sum, cur_sum)
print(max_sum)