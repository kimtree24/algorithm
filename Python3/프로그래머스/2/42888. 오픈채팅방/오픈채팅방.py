def solution(record):
    name = {}
    for r in record:
        parts = r.split()
        cmd, uid = parts[0], parts[1]
        if cmd in ("Enter", "Change"):
            name[uid] = parts[2]

    ans = []
    for r in record:
        parts = r.split()
        cmd, uid = parts[0], parts[1]
        if cmd == "Enter":
            ans.append(f"{name[uid]}님이 들어왔습니다.")
        elif cmd == "Leave":
            ans.append(f"{name[uid]}님이 나갔습니다.")
    return ans