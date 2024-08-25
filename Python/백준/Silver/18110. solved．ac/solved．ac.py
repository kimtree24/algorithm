import sys
n = int(sys.stdin.readline())
lis = []
for _ in range(n):
    lis.append(int(sys.stdin.readline()))
lis.sort()

def custom_round(num):
    int_num = int(num)
    if num-int_num>=0.5:
        return int_num+1
    else:
        return int_num

cut_num = custom_round(n*0.15)
if n == 0:
    print(0)
else:
    print(custom_round(sum(lis[cut_num:n-cut_num])/(n-cut_num*2)))