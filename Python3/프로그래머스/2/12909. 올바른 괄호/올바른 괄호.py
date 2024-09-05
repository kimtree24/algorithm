def solution(s):
    ans = True
    stack = []
    
    for i in s:
        if i == "(":
            stack.append("(")
        elif i == ")":
            if stack:
                stack.pop()
            else:
                ans = False
                break
    if stack:
        ans = False
    return ans