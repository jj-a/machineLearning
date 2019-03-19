# recommendation algorithm
# 영화 추천 알고리즘

'''
유클리디안 거리점수(Euclidean Distance) 이용

각 점(평점 데이터) 사이의 거리
# 공식:
\[ \sqrt{(x_1-x_2)^2+(y_1-y_2)^2} \]
# 파이썬 코드:
from math import sqrt
sqrt(pow(x1-x2) + pow(y1-y2))

# 역수 (값이 클수록 유사도가 큼)
1/(1+sqrt(pow(x1-x2) + pow(y1-y2)))
'''


from math import sqrt


# Euclidean Distance
def sim_distance(prefs, person1, person2):
    # 공통 항목 추출
    si = dict()

    for item in prefs[person1]:
        if item in prefs[person2]:
            si[item] = 1

    # 공통 평가 항목이 없는 경우 0 리턴
    if len(si) == 0: return 0

    # person1의 item이 person2에서도 존재한다면, person1과 person2의 item 평점 차이의 제곱한 값을 더한 후 제곱 근을 계산
    sum_of_squares = sum([(prefs[person1][item] - prefs[person2][item])**2 for item in prefs[person1] if item in prefs[person2]])

    return 1/(1+sqrt(sum_of_squares))
