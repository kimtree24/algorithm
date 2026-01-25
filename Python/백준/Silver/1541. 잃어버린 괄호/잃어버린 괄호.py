import sys

input = sys.stdin.readline

expressions = input().strip()

partition = expressions.split('-')

result = sum(map(int, partition[0].split('+')))

for part in partition[1:]:
    result -= sum(map(int, part.split('+')))

print(result)