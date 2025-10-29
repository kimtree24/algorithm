def solution(numbers):
    ans = []
    for number in numbers:
        if number % 2 == 0:
            ans.append(number+1)
        else:
            idx = 0
            mock = 0
            remain = number
            while True:
                if remain % 2 == 0:
                    ans.append(number + 2 ** (idx-1))
                    break
                else:
                    idx += 1
                    remain = remain // 2
    return ans
                
                