import re
from collections import Counter

def solution(s):
    nums = re.findall(r'\d+', s)
    cnt = Counter(map(int, nums))
    return [num for num, _ in cnt.most_common()]