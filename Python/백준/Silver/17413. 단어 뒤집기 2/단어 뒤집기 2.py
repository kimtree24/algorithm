import sys
string = sys.stdin.readline().strip()
n = len(string)
word = []
i = 0
while i < n:
    if string[i] == '<':
        idx = 0
        while i + idx < n and string[i+idx] != '>':
            idx +=1
        word.append(string[i:i+idx+1])
        i += idx+1
    else:
        start = i
        while i < n and string[i] != '<' and string[i] != ' ':
            i +=1
        word.append(string[start:i])
        if i < n and string[i] == ' ':
            word.append(' ')
            i += 1

for i in range(len(word)):
    if word[i][0] == '<':
        continue
    else:
        word[i] = word[i][::-1]
result = ''.join(word)
print(result)