def solution(id_list, report, k):
    report = set(report)
    
    report_count = {}
    
    user_reports = {}
    
    for user in id_list:
        report_count[user] = 0
        user_reports[user] = []
    
    for r in report:
        reporter, reported = r.split()
        report_count[reported] += 1
        user_reports[reporter].append(reported)
    
    
    banned = {user for user, count in report_count.items() if count >= k}
    
    result = []
    for user in id_list:
        count = sum(1 for reported in user_reports[user] if reported in banned)
        result.append(count)
    
    return result