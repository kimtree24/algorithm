def solution(keymap, targets):
    INF = 10**9
    key_map = [INF] * 26  # A~Z

    for row in keymap:
        for i, ch in enumerate(row):
            idx = ord(ch) - 65
            if i + 1 < key_map[idx]:
                key_map[idx] = i + 1

    ans = []
    for word in targets:
        s = 0
        ok = True
        for ch in word:
            idx = ord(ch) - 65
            if not (0 <= idx < 26) or key_map[idx] == INF:
                ok = False
                break
            s += key_map[idx]
        ans.append(s if ok else -1)
    return ans