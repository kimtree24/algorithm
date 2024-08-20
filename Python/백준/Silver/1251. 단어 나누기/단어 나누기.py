string = input()
n = len(string)

result = None

for i in range(1, n - 1):
    for j in range(i + 1, n):
        part1 = string[:i][::-1]
        part2 = string[i:j][::-1]
        part3 = string[j:][::-1]

        temp = part1 + part2 + part3

        if result == None or temp < result:
            result = temp
            
print(result)