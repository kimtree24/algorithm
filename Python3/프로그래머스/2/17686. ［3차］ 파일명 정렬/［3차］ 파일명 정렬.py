import re
_pat = re.compile(r'^([^\d]+)(\d{1,5})')

def solution(files):
    def key(name):
        m = _pat.match(name)
        head, num = m.group(1), m.group(2)
        return (head.lower(), int(num))
    return sorted(files, key=key)