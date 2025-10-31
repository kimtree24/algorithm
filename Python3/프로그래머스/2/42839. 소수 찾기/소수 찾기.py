from itertools import permutations

def is_prime(number):
    if number == 1 or number == 0:
        return False

    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def solution(numbers):
    digits = list(numbers)
    
    num_set = set()
    
    for i in range(1, len(digits) + 1):
        for p in permutations(digits, i):
            num_set.add(int(''.join(p)))
    cnt = 0
    for num in num_set:
        if is_prime(num):
            cnt+=1
    return cnt
    