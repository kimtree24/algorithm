input_str = input()
result = []
for i in range(26):
    result.append(-1)
k = 0
for i in input_str:
    num_chr = ord(i)
    if(result[num_chr-97] == -1):
        result[num_chr-97] = k
    k+=1
print(' '.join(map(str, result)))