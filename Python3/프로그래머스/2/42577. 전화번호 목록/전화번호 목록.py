def solution(phone_book):
    set_book = set(phone_book)
    
    for each_phone in set_book:
        for i in range(1, len(each_phone)):
            if each_phone[:i] in set_book:
                return False
    
    return True