from itertools import permutations

def is_prime(number):
    if number == 1 or number == 0:
        return False

    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def solution(numbers):
    nums = list(numbers)
    n = len(nums)
    used = [False] * n
    made = set()
    
    def dfs(path_chars):
        if path_chars:
            num = int(''.join(path_chars))
            made.add(num)

        used_in_this_depth = set()
        for i in range(n):
            if used[i]:
                continue
            ch = nums[i]
            if ch in used_in_this_depth:
                continue
            used_in_this_depth.add(ch)
            
            used[i] = True
            dfs(path_chars + [ch])
            used[i] = False
    dfs([])
    
    return sum(1 for x in made if is_prime(x))
    