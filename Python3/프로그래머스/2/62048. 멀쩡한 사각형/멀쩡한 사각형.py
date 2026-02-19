def get_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def solution(w,h):
    # 수식 -> 망가지는 사각형 수 = w + h - gcd(w,h)
    # 최대공약수 구하기
    gcd = get_gcd(w, h)
    return w * h - (w + h - gcd)