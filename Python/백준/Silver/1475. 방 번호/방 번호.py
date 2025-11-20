import sys
from collections import Counter

input = sys.stdin.readline

n = input().strip()

cnt = Counter(n)

six_nine = cnt['6'] + cnt['9']
cnt['6'] = (six_nine + 1) // 2
if '9' in cnt:
    del cnt['9']
    
print(max(cnt.values()))