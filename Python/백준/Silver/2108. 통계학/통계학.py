import sys
n = int(sys.stdin.readline())
num_list = []
for i in range(n):
    num_list.append(int(sys.stdin.readline()))

print(round(sum(num_list) / n))

num_list.sort()

print(num_list[n // 2])

count = 1
big_count = 1
mode_list = []
for i in range(1,n):
    if num_list[i] == num_list[i-1]:
        count +=1
    else:
        if count > big_count:
            big_count = count
            mode_list = []
            mode_list.append(num_list[i-1])
        elif count == big_count:
            mode_list.append(num_list[i-1])
        count = 1
        
if count > big_count:
    mode_list = [num_list[-1]]
elif count == big_count:
    mode_list.append(num_list[-1])
        
if len(mode_list) == 1:
    print(mode_list[0])
else:
    print(mode_list[1])

print(num_list[-1]-num_list[0])