while True:
    num = int(input())
    if num == 0:
        break
    re_num = int(str(num)[::-1])
    if re_num == num:
        print("yes")
    else:
        print("no")