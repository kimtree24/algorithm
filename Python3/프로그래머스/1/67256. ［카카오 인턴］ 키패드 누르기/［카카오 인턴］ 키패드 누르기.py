def solution(numbers, hand):
    keypad = {
        1: (0, 0), 2: (0, 1), 3: (0, 2),
        4: (1, 0), 5: (1, 1), 6: (1, 2),
        7: (2, 0), 8: (2, 1), 9: (2, 2),
        '*': (3, 0), 0: (3, 1), '#': (3, 2)
    }
    left_hand = '*'
    right_hand = '#'
    
    result = []
    
    dominant_hand = 'R' if hand == 'right' else 'L'
    
    def get_distance(pos1, pos2):
        x1, y1 = keypad[pos1]
        x2, y2 = keypad[pos2]
        return abs(x1 - x2) + abs(y1 - y2)
    
    for num in numbers:
        if num in [1, 4, 7]:
            result.append('L')
            left_hand = num
        elif num in [3, 6, 9]:
            result.append('R')
            right_hand = num
        else:
            left_distance = get_distance(left_hand, num)
            right_distance = get_distance(right_hand, num)
            
            if left_distance < right_distance:
                result.append('L')
                left_hand = num
            elif left_distance > right_distance:
                result.append('R')
                right_hand = num
            else:
                if dominant_hand == 'R':
                    result.append('R')
                    right_hand = num
                else:
                    result.append('L')
                    left_hand = num
    
    return ''.join(result)