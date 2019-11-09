import math
def solution(prices, discounts):
    answer = 0
    prices.sort(reverse = True)
    discounts.sort(reverse = True)

    i = 0
    while i < len(discounts):
        answer += prices[i] * ((100 - discounts[i]) / 100)
        i += 1

    answer += sum(prices[i:])
    return math.trunc(answer)