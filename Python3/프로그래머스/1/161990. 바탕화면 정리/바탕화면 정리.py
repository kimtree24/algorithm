def solution(wallpaper):
    min_file_x = 50
    min_file_y = 50
    max_file_x = 0
    max_file_y = 0
    
    for row in range(len(wallpaper)):
        for col in range(len(wallpaper[row])):
            if wallpaper[row][col] == "#":
                min_file_x = min(min_file_x, col)
                min_file_y = min(min_file_y, row)
                max_file_x = max(max_file_x, col)
                max_file_y = max(max_file_y, row)
            else:
                continue
    
    luy = max(0, min_file_x)
    lux = max(0, min_file_y)
    rdy = min(50, max_file_x + 1)
    rdx = min(50, max_file_y + 1)
    return [lux, luy, rdx, rdy]
            