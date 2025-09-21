def solution(cards1, cards2, goal):
    idx_cards1 = 0
    idx_cards2 = 0
    for word in goal:
        if idx_cards1 < len(cards1) and word == cards1[idx_cards1]:
            idx_cards1 += 1
        elif idx_cards2 < len(cards2) and word == cards2[idx_cards2]:
            idx_cards2 += 1
        else:
            return "No"
    return "Yes"
        