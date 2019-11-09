def solution(history):
    answer = []
    recipe = [4, 50, 10, 10, 4]
    price = [[10, 10000], [100, 3000], [30, 1000], [50, 2000], [10,1000]]
    now = [5, 100, 10, 5, 2]

    for i in history:
        money = 0
        i = float(i)
        if i > 2.5 or i <= 0:
            answer = [-1]
            break

        while i > 0:
            if int(i) == 0:
                for j in range(len(recipe) - 1):
                    if now[j] < recipe[j]:
                        money += price[j][1]
                        now[j] += price[j][0]
                    now[j] -= recipe[j]
                if now[-1] < (recipe[-1] // 2):
                    money += price[-1][1]
                    now[-1] += price[-1][0]
                    now[-1] -= recipe[-1] // 2

            else:

                for j in range(len(recipe)):
                    if now[j] < recipe[j]:
                        money += price[j][1]
                        now[j] += price[j][0]
                    now[j] -= recipe[j]
            i -= 1
        answer.append(money)

    return answer