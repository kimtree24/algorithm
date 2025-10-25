def solution(skill, skill_trees):
    skill_set = set(skill)
    cnt = 0
    for tree in skill_trees:
        filtered = ''.join(ch for ch in tree if ch in skill_set)
        if skill.startswith(filtered):
            cnt += 1
    return cnt