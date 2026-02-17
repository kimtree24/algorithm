def balanced(p):
    # 빈 문자열인 경우 반환
    if not p:
        return ""
    cnt_open = 0
    cnt_close = 0
    for idx, ch in enumerate(p):
        if ch == '(':
            cnt_open += 1
        elif ch == ')':
            cnt_close += 1
        if cnt_open and cnt_open == cnt_close:
            u = p[:idx+1]
            v = p[idx+1:]
            break
    # u가 올바른 건지 판단
    if right(u): # 올바르면
        v = balanced(v)
        return u+v
    else:
        return make(u, v)
        
# 올바른 괄호 인지 판단
def right(u):
    stack = []
    for ch in u:
        if not stack:
            stack.append(ch)
        else:
            if stack[-1] == '(' and ch == ')':
                stack.pop()
            else:
                stack.append(ch)
    if not stack:
        return 1
    else:
        return 0

# 올바른 괄호 문자열로 만들기
def make(u, v):
    result = '('
    v = balanced(v)
    result = result + v + ')'
    u = u[1:len(u) - 1]
    new_u = []
    for ch in u:
        if ch == '(':
            new_u.append(')')
        else:
            new_u.append('(')
    result = result + ''.join(new_u)
    return result

def solution(p):
    ans = balanced(p)
    return ans
    

        
    