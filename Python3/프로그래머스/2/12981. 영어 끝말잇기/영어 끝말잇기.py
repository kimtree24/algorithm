def solution(n, words):
    sayWords = [words[0]]
    count = 1
    who = 0
    for i in range(1,len(words)):
        if words[i] not in sayWords and sayWords[-1][-1] == words[i][0]:
            count += 1
            sayWords.append(words[i])
        else:
            break
    if count == len(words):
        return [0,0]
    else:
        if (count+1)%n == 0:
            who = n
            when = (count+1)//n
        else:
            who = (count+1)%n
            when = (count+1)//n + 1
        return [who,when]
            