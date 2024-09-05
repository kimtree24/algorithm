def solution(s):
    num_list = list(map(int, s.split()))
    maxNum = max(num_list)
    minNum = min(num_list)
    answer = f"{minNum} {maxNum}"
    return answer