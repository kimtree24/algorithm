def solution(mats, park):
    parkY = len(park)
    parkX = len(park[0])
    
    def can_place(x, y, size):
        if x + size > parkX or y + size > parkY:
            return False
        for i in range(y, y + size):
            for j in range(x, x + size):
                if park[i][j] != '-1':
                    return False
        return True

    mats.sort(reverse=True)
    for mat in mats:
        for i in range(parkY):
            for j in range(parkX):
                if park[i][j] == '-1' and can_place(j, i, mat):
                    return mat
    return -1