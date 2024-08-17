l = int(input())
input_string = input()
ans = 0

for i in range(l):
    ans += 31**i * (ord(input_string[i])-96)
    
print(ans % 1234567891)