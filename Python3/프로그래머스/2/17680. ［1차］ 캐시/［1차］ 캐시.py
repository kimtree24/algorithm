def solution(cacheSize, cities):
    if cacheSize == 0:
        return len(cities) * 5

    cache = []
    time = 0

    for city in cities:
        city = city.lower()

        # hit
        if city in cache:
            time += 1
            # 캐시 갱신
            cache.remove(city)
            cache.append(city)
        # miss
        else:
            time += 5
            if len(cache) == cacheSize:
                # LRU 제거
                cache.pop(0)
            # 캐시에 추가
            cache.append(city)

    return time