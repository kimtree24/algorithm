t = int(input())

for _ in range(t):
    n = int(input())
    things_list = set()
    each_things = {}
    for _ in range(n):
        name, things = input().split()
        things_list.add(things)
        each_things.setdefault(things, []).append(name)
    result = 1
    for things in things_list:
        result *= len(each_things[things]) + 1

    print(result - 1)