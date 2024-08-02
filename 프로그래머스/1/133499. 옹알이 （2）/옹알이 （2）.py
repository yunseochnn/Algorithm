def solution(babbling):
    cnt = 0
    babble = ["aya", "ye", "woo", "ma"]
    for word in babbling:
        for i in babble:
            if i*2 not in word:
                word = word.replace(i," ")
        if word.isspace():
            cnt += 1
    return cnt