n = int(input())

stack, ans = [], []
isCan = True
now = 1
for _ in range(n):
    num = int(input())
    while now <= num:
        stack.append(now)
        ans.append("+")
        now +=1
    if num == stack[-1]:
        stack.pop()
        ans.append("-")
    else:
        print("NO")
        isCan = False
        break
 
if isCan:
    for i in ans:
        print(i)