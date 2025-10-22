from collections import Counter
import math
def solution(str1, str2):
    # 문자열 바탕으로 2개씩 묶어서 집합 만들기
    # str1관련
    str1_ = []
    for i in range(len(str1)-1):
        first_ch = str1[i]
        second_ch = str1[i+1]
        if (ord('a') <= ord(first_ch) <= ord('z') or ord('A') <= ord(first_ch) <= ord('Z')) and (ord('a') <= ord(second_ch) <= ord('z') or ord('A') <= ord(second_ch) <= ord('Z')):
            str1_.append(str1[i:i+2].lower())
    # str2관련
    str2_ = []
    for i in range(len(str2)-1):
        first_ch = str2[i]
        second_ch = str2[i+1]
        if (ord('a') <= ord(first_ch) <= ord('z') or ord('A') <= ord(first_ch) <= ord('Z')) and (ord('a') <= ord(second_ch) <= ord('z') or ord('A') <= ord(second_ch) <= ord('Z')):
            str2_.append(str2[i:i+2].lower())
    dict_str1 = Counter(str1_)
    dict_str2 = Counter(str2_)
    intersection = dict_str1 & dict_str2
    sum_section = dict_str1 | dict_str2
    num_inter = sum(intersection.values())
    num_sum = sum(sum_section.values())
    
    if not dict_str1 and not dict_str2:
        return 1 * 65536
    else:
        return math.floor((num_inter / num_sum) * 65536)
    