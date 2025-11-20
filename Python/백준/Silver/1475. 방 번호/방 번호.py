import sys
import math
from collections import defaultdict
input = sys.stdin.readline

n = input().strip()

num_list = list(n)
num_dict = defaultdict(int)
for num in num_list:
    if num == '9' or num == '6':
        num_dict['6'] += 1
    else:
        num_dict[num] += 1
if num_dict.get('6'):
    num_dict['6'] = math.ceil(num_dict.get('6') / 2)
print(max(num_dict.values()))