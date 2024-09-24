def solution(today, terms, privacies):
    term_data = {}
    today_year = int(today[:4])
    today_mon = int(today[5:7])
    today_day = int(today[8:])
    result = []
    for i in terms:
        term, date = i.split()
        term_data[term] = int(date)
        
    for i in range(len(privacies)):
        date, term = privacies[i].split()
        year = int(date[:4])
        mon = int(date[5:7])
        day = int(date[8:])
        
        new_mon = mon + term_data[term]
        while new_mon > 12:
            year += 1
            new_mon -= 12
        
        if today_year > year:
            result.append(i+1)
        if today_year == year and today_mon > new_mon:
            result.append(i+1)
        if today_year == year and today_mon == new_mon and today_day >= day:
            result.append(i+1)
    return result
        
        