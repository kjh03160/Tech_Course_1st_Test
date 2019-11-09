def solution(infos, actions):
    answer = []
    LOGIN = False
    ADD = []
    for i in actions:
        # if 'LOGIN' in i:
        #     if LOGIN == True or not i[6:] in infos:
        #         answer.append(False)
        #     elif i[6:] in infos:
        #         LOGIN = True
        #         answer.append(True)
        if LOGIN == False:
            if 'LOGIN' in i:
                if i[6:] in infos:
                    LOGIN = True
                    answer.append(True)
                    continue
            answer.append(False)

        elif LOGIN == True:
            if 'LOGIN' in i:
                answer.append(False)
                continue
            elif 'ADD' in i:
                a = i.split()
                ADD.append(int(a[-1]))
                answer.append(True)
                continue
            elif 'ORDER' in i:
                if len(ADD) != 0:
                    ADD = []
                    answer.append(True)
                    continue
            answer.append(False)

        #     if 'ADD' in i:
        #         a = i.split()
        #         if a[-1].isdigit():
        #             ADD.append(a[-1])
        #             answer.append(True)
        #         else:
        #             answer.append(False)
        #     elif 'ORDER' in i:
        #         if len(ADD) > 0:
        #             answer.append(True)
        #             ADD = []
        #         else:
        #             answer.append(False)
        # else:
        #     answer.append(False)

    return answer

infos = ["kim password", "lee abc"]
actions = [
    "ADD 30",
    "LOGIN kim abc",
    "LOGIN lee password",
    "LOGIN kim password",
    "LOGIN kim password",
    "ADD 30",
    "ORDER",
    "ORDER",
    "ADD 40",
    "ADD 50"
]
print(solution(infos, actions))
print("[false, false, false, true, false, true, true, false, true, true]")