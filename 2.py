def solution(logs):
    answer = []
    logs1 = logs.split("\n")
    time = {}
    for i in range(0, 24):
        time[i] = 0
    for i in logs1:
        hour = int(i[11:13]) + 9
        if hour >= 24:
            hour -= 24
        time[hour] += 1

    answer = list(time.values())

    return answer