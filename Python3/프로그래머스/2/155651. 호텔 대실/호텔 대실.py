def to_min(t):
    h, m = map(int, t.split(':'))
    return h * 60 + m

def solution(book_time):
    events = []
    for s, e in book_time:
        start = to_min(s)
        end = to_min(e) + 10
        events.append((start, +1))
        events.append((end, -1))
    events.sort(key = lambda x : (x[0], x[1]))
    
    cur = 0
    ans = 0
    for _, d in events:
        cur += d
        ans = max(ans, cur)
    return ans