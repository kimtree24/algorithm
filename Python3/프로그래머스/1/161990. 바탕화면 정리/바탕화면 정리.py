def solution(wallpaper):
    rows = len(wallpaper)
    cols = len(wallpaper[0])

    min_r, min_c = rows, cols
    max_r, max_c = -1, -1

    for r, line in enumerate(wallpaper):
        for c, ch in enumerate(line):
            if ch == '#':
                if r < min_r:
                    min_r = r
                if c < min_c:
                    min_c = c
                if r > max_r:
                    max_r = r
                if c > max_c:
                    max_c = c
    return [min_r, min_c, max_r + 1, max_c + 1]