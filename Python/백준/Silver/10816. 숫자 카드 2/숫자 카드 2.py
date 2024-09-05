import sys
from collections import Counter

n = int(sys.stdin.readline().rstrip())
cardList = list(map(int, sys.stdin.readline().rstrip().split()))
m = int(sys.stdin.readline().rstrip())
numList = list(map(int, sys.stdin.readline().rstrip().split()))

count = Counter(cardList)

for i in numList:
    if i in count:
        print(count[i],  end=' ')
    else:
        print(0, end=' ')