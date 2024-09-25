def solution(new_id):
    new_id = new_id.lower() #1단계
    
    #2단계
    new_id_stack = []
    for i in range(len(new_id)):
        if (ord('a') <= ord(new_id[i])<= ord('z')) or ord('0')<= ord(new_id[i])<=ord('9') or new_id[i] == '-' or new_id[i] == '_' or new_id[i] == '.':
            new_id_stack.append(new_id[i])
    
    #3단계
    new_id_3 = []
    new_id_3.append(new_id_stack[0])
    for i in range(1, len(new_id_stack)):
        if new_id_stack[i-1] == '.' and new_id_stack[i] == '.':
            continue
        else:
            new_id_3.append(new_id_stack[i])
    #4단계
    if new_id_3 and new_id_3[0] == '.':
        del new_id_3[0]
    if new_id_3 and new_id_3[-1] == '.':
        del new_id_3[-1]
    
    #5단계
    if len(new_id_3) == 0:
        new_id_3.append('a')
    #6단계
    if len(new_id_3) >= 16:
        new_id_3 = new_id_3[:15]
        if new_id_3[-1] == '.':
            del new_id_3[-1]
    #7단계
    if len(new_id_3) <= 2:
        while True:
            if len(new_id_3) ==3:
                break
            else:
                new_id_3.append(new_id_3[-1])
    new_id = ''.join(new_id_3)
    return new_id