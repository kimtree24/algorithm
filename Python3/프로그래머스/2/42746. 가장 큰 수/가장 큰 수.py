def solution(numbers):
    temp = []
    for number in numbers:
        temp.append(str(number))
    sorted_numbers = sorted(temp,key = lambda x: x*3, reverse = True)
    
    ans = ''.join(sorted_numbers)
    if ans[0] == '0':
        return '0'
    else:
        return ans