def solution(forms):
    answer = []
    for i in range(len(forms) - 1):
        for j in range(len(forms[i][1]) - 1):
            if len(forms[i][1]) == 1:
                break
            a = forms[i][1][j:j+2]
            for k in range(i + 1, len(forms)):
                if a in forms[k][1] and not forms[k][0] in answer:
                    answer.append(forms[k][0])
                    if forms[i][0] not in answer:
                        answer.append(forms[i][0])

    answer.sort()
    return answer
