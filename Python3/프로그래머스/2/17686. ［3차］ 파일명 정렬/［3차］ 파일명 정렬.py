import re
def solution(files):
    re_head = r'[^0-9]+'
    re_number = r'\d+'
    files_dict = {}
    for idx,each_file in enumerate(files):
        head = re.search(re_head, each_file).group().lower()
        number = int(re.search(re_number, each_file).group())
        files_dict[each_file] = (head, number, idx)
    
    sorted_files = sorted(files_dict.items(), key = lambda x : (x[1][0], x[1][1], x[1][2]))
    
    return [name for name, _ in sorted_files]
        
        
    