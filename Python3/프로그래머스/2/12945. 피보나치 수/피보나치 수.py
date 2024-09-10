def solution(n):
    f0 = 0
    f1 = 1
    fn = 0
    for _ in range(n):
        fn = f0 + f1
        f0 = f1
        f1 = fn
    return f0%1234567