import sys
input = sys.stdin.readline

n = int(input().strip())
cnt = 0

for _ in range(n):
    stack = []
    word = list(input().strip())
    len_word = len(word)
    for ch in word:
        if stack and stack[-1] != ch:
            stack.append(ch)
        elif stack and stack[-1] == ch:
            stack.pop()
        elif not stack:
            stack.append(ch)
    if not stack:
        cnt += 1
print(cnt)