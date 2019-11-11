import math
def solution(prices, discounts):
    answer = 0
    prices.sort(reverse = True)
    discounts.sort(reverse = True)

    i = 0
    length = 0
    if len(prices) >= len(discounts):
        length = len(discounts)
    else:
        length = len(prices)
        
    while i < length:
        answer += prices[i] * ((100 - discounts[i]) / 100)
        i += 1

    answer += sum(prices[i:])
    return math.trunc(answer)
