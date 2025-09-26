def solution(babbling):
    can_speak = ["aya", "ye", "woo", "ma"]
    result = 0

    for word in babbling:
        idx = 0
        prev = ""
        valid = True

        while idx < len(word):
            matched = False
            for speak in can_speak:
                if word.startswith(speak, idx) and speak != prev:
                    idx += len(speak)
                    prev = speak
                    matched = True
                    break
            if not matched:
                valid = False
                break

        if valid:
            result += 1

    return result