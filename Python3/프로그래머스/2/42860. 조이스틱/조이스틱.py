def change_cnt(ch):
    # A에서 앞으로 이동
    front = ord(ch) - ord('A')
    # A에서 뒤로 이동
    back = 1 + ord('Z') - ord(ch)
    return min(front, back)

def move_cnt(name):
    n = len(name)
    move = n - 1
    
    for i in range(n):
        next_i = i + 1
        
        while next_i < n and name[next_i] == 'A':
            next_i += 1
        
        move = min(move, 2 * i + n - next_i)
        move = min(move, i + 2 * (n - next_i))
        
    return move

def solution(name):
    change = 0
    for ch in name:
        change += change_cnt(ch)
    
    move = move_cnt(name)
    
    return change + move