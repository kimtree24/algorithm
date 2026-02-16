def solution(m, musicinfos):
    # musicinfos를 통해서 나온 멜로디 정리
    # 멜로디 안에 m 있는지 찾기
    # 찾은거 여러개면 재생 시간 제일 긴 것 -> 먼저 입력된 음악 제목 반환
    
    # 멜로디 정리
    fi_info = []
    for idx, musicinfo in enumerate(musicinfos):
        start, end, title, code = musicinfo.split(',')
        start_h, start_m = map(int, start.split(':'))
        end_h, end_m = map(int, end.split(':'))
        start_t = start_h * 60 + start_m
        end_t = end_h * 60 + end_m
        time = end_t - start_t
        
        # code 전처리
        fi_code = []
        for ch in code:
            if ch == '#':
                if fi_code[-1] == "C":
                    fi_code[-1] = "c"
                elif fi_code[-1] == "D":
                    fi_code[-1] = 'd'
                elif fi_code[-1] == "E":
                    fi_code[-1] = 'F'
                elif fi_code[-1] == "F":
                    fi_code[-1] = 'f'
                elif fi_code[-1] == "G":
                    fi_code[-1] = 'g'
                elif fi_code[-1] == "A":
                    fi_code[-1] = 'a'
                elif fi_code[-1] == 'B':
                    fi_code[-1] = 'C'
            else:
                fi_code.append(ch)
        
        # 멜로디 가져오기
        melody = []
        for i in range(time):
            melody.append(fi_code[i % len(fi_code)])
        fi_info.append((idx, time, title, ''.join(melody)))
    
    # 멜로디 있는지 판단
    ans_list = []
    
    # m 전처리
    m = m.replace('C#', 'c')
    m = m.replace('D#', 'd')
    m = m.replace('E#', 'F')
    m = m.replace('F#', 'f')
    m = m.replace('G#', 'g')
    m = m.replace('A#', 'a')
    m = m.replace('B#', 'C')
    
    for each_info in fi_info:
        if m in each_info[-1]:
            ans_list.append(each_info)
    
    if not ans_list:
        return "(None)"
    
    sorted_ans = sorted(ans_list, key = lambda x : (-x[1], x[0]))
    
    return sorted_ans[0][2]