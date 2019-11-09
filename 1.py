import math
def solution(restaurant, riders, k):
    answer = 0
    x = restaurant[0]
    y = restaurant[1]
    for rider in riders:
        rider_x = rider[0]
        rider_y = rider[1]
        a = math.sqrt(((x - rider_x) ** 2) +((y - rider_y) ** 2))
        if a <= k:
            answer += 1


    return answer


"""
배달의 민족에서는 주문이 발생하면 음식점 근처에 있는 배민 라이더들에게 알림을 보냅니다. 다음 그림은 반경이 500m일 때의 예입니다.

marker_centered.jpg

중앙의 파란색 마커: 음식점
빨간색 별: 알림을 받을 라이더
초록색 별: 알림을 받지 못하는 라이더

주문이 발생한 음식점의 위치 restaurant, 배민 라이더들의 위치 riders, 반경 k가 매개변수로 주어집니다. 알림을 받을 라이더는 몇 명인지 return 하도록 메서드를 완성해주세요.

제한 사항
restaurant 배열의 길이는 2이며, 음식점의 [X좌표, Y좌표] 형식입니다.
riders 배열의 길이는 1 이상 1,000 이하입니다.
riders 배열의 원소는 라이더의 [X좌표, Y좌표]형식입니다.
모든 X, Y좌표 값은 -10,000 이상 10,000 이하입니다.
k는 200 이상 5,000 이하입니다.
원 경계선에 있는 라이더도 알림을 받습니다.
입출력 예
restaurant	riders	k	result
[0,0]	[[-700,0], [150,180], [500,500], [150, -800], [800, 800], [-900, 500], [-1100, 900]]	1000	4
입출력 예 설명
주어진 좌표를 그림으로 표현하면 다음과 같습니다.

배민문제2.png

음식점이 있는 원점에서 반경 1000에 위치한 라이더(빨간 점)는 4명입니다.
"""