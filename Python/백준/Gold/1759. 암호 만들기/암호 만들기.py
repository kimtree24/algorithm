import sys
input = sys.stdin.readline

l, c = map(int,input().split())
c_list = sorted(input().split())
mo = ['a', 'e', 'i', 'o', 'u']
temp = []
def dfs(cur_idx):
    # 탈출조건
    if len(temp) == l:
        cnt_mo = 0
        for i in temp:
            if i in mo:
                cnt_mo += 1
        cnt_ja = l - cnt_mo
        #유효암호
        if cnt_mo > 0 and cnt_ja > 1:
            print(''.join(temp))
            return
        return
    # 다음 가지
    for i in range(cur_idx, c):
        ch = c_list[i]
        temp.append(ch)
        dfs(i + 1)
        temp.pop()
dfs(0)
