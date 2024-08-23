import sys

t = int(input())
for i in range(t):
    n, m = map(int, sys.stdin.readline().rstrip().split())
    list_doc = list(map(int, sys.stdin.readline().rstrip().split()))
    count = 0

    while True:
        if list_doc[0] == max(list_doc):
            count +=1
            if m == 0:
                print(count)
                break
            else:
                list_doc.pop(0)
                m-=1
        else:
            list_doc.append(list_doc.pop(0))
            if m == 0:
                m = len(list_doc)-1
            else:
                m-=1