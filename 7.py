def solution(user, friends, visitors):
    answer = []
    reco = {}
    excluded = [user]

    for i in friends:
        if i[-1] == user:
            excluded.append(i[0])

    for i in friends:
        if i[-1] in excluded:
            continue
        if i[0] in excluded:
            if i[-1] in reco.keys():
                reco[i[-1]] += 10
            else:
                reco[i[-1]] = 10

    for j in visitors:
        if j in excluded:
            continue
        if j[-1] in reco.keys():
            reco[j[-1]] += 1
        else:
            reco[j[-1]] = 1

    reco = sorted(reco.items(), key = lambda x : (-x[1], x[0]))
    print(reco)
    if len(reco) > 5:
        for i in range(5):
            answer.append(reco[i][0])
    else:

        for i in range(len(reco)):
            answer.append(reco[i][0])

    return answer
