def solution(citations):
    n = len(citations)
    sorted_citations = sorted(citations, reverse = True)
    h = 0
    idx = 0
    while idx < n:
        # 이번에 검증할 것
        each_citation = sorted_citations[idx]
        temp_h = 0
        
        for citation in sorted_citations:
            if each_citation <= citation:
                temp_h += 1
            else:
                break
        
        if temp_h <= each_citation:
            h = temp_h
        idx += 1
    return h
        