from collections import deque
def solution(skill, skill_trees):
    cnt = 0
    for skill_tree in skill_trees:
        idx = 0
        skill_q = deque(skill)
        while idx < len(skill_tree):
            in_skill = skill_tree[idx] in skill_q
            if in_skill and skill_tree[idx] == skill_q[0]:
                idx += 1
                skill_q.popleft()
            elif not in_skill:
                idx += 1
            else:
                break
        if idx == len(skill_tree):
            cnt += 1
    return cnt