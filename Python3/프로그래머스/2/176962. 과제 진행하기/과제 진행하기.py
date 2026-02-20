def solution(plans):
    # 전처리
    arr = []
    for name, start, play in plans:
        hh, mm = map(int, start.split(':'))
        arr.append([name, hh * 60 + mm, int(play)])
    arr.sort(key=lambda x: x[1])

    ans = []
    stack = []  # [name, remaining]

    # 첫 과제 시작
    cur_name, cur_start, cur_play = arr[0]
    cur_time = cur_start

    for i in range(1, len(arr)):
        next_name, next_start, next_play = arr[i]
        available = next_start - cur_time  # 다음 과제 시작 전까지 남은 시간

        # 현재 진행 중 과제부터 처리
        while True:
            if cur_play <= available:
                # 현재 과제 완료
                cur_time += cur_play
                available -= cur_play
                ans.append(cur_name)

                # 남는 시간이 있고, 멈춘 과제가 있으면 이어서 진행
                if stack and available > 0:
                    cur_name, cur_play = stack.pop()
                    continue
                else:
                    break
            else:
                # 현재 과제 완료 못함 -> 남은 시간만 빼고 스택에 저장
                cur_play -= available
                stack.append([cur_name, cur_play])
                cur_time = next_start
                break

        # 다음 과제 시작
        cur_name, cur_play = next_name, next_play
        cur_time = next_start

    # 마지막 과제 처리
    ans.append(cur_name)

    # 남은 과제들 처리
    while stack:
        ans.append(stack.pop()[0])

    return ans