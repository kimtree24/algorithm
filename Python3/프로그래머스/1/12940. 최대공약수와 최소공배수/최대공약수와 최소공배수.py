import math
def solution(n, m):
    answer = []
    gcd = math.gcd(n,m)
    num = 1
    num *= n/gcd
    num *= m/gcd
    num *= gcd
    return [gcd,num]