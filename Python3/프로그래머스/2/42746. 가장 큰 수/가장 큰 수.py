def solution(numbers):
    temp = list(map(str, numbers))
    sorted_numbers = sorted(temp,key = lambda x: x*3, reverse = True)
    
    if sorted_numbers[0][0] == '0':
        return '0'
    else:
        return ''.join(sorted_numbers)