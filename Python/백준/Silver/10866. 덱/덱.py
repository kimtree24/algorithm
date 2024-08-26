import sys
n = int(sys.stdin.readline().rstrip())
deque = []
for _ in range(n):
    inputLine = sys.stdin.readline().rstrip()
    if inputLine.split()[0] == 'push_back' or inputLine.split()[0] == 'push_front':
        order = inputLine.split()[0]
        num = int(inputLine.split()[1])
    else:
        order = inputLine.split()[0]

    if order == 'push_front':
        deque.insert(0,num)
    if order == 'push_back':
        deque.append(num)
    if order == 'pop_front':
        if len(deque) == 0:
            print(-1)
        else:
            print(deque.pop(0))
    if order == 'pop_back':
        if len(deque) == 0:
            print(-1)
        else:
            print(deque.pop(-1))
    if order == 'size':
        print(len(deque))
    if order == 'empty':
        if len(deque) == 0:
            print(1)
        else:
            print(0)
    if order == 'front':
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[0])
    if order == 'back':
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[-1])