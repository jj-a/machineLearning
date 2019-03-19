# recommendation algorithm
# 영화 추천 알고리즘
#
# '''
# 피어슨 상관계수(Pearson correlation coefficient) 이용
#
# 1) 두 평론가가 공통으로 평가한 영화들을 찾는다
# 2) 각각의 평론가가 평가한 영화 점수들을 합한다
# 3) 각각의 평론가가 평가한 영화 점수의 제곱의 합을 구한다
# 4) 두 평론가가 평가한 영화 점수의 곱의 합을 구한다
# 5) 아래의 공식을 이용해 피어슨 상관계수를 구한다
#
# 두 개의 데이터 집합이 한 직선으로 얼마나 잘 표현되는가를 나타내는 측정값
# # 공식:
# \[ r = \frac{\sum{(x_i-\bar{x})(y_i-\bar{y})}}{\sqrt{\sum{(x_i-\bar{x})^2}}\sqrt{(y_i-\bar{y})^2}} \] \[ \bar{x} = \frac{1}{n}\sum\limits_{i}^n{x_i} \] \[ \bar{y} = \frac{1}{n}\sum\limits_i^n{y_i} \]
# ->  \(x\)와 \(y\)가 완전 동일하면 1, 전혀 다르면 0, 반대 방향으로 완전 동일하면 -1
# '''

from math import sqrt


# Pearson correlation coefficient
def sim_pearson(prefs, p1, p2):
    # 같이 평가한 항목들의 목록을 구함
    si = dict()

    for item in prefs[p1]:
        if item in prefs[p2]:
            si[item] = 1

    # 공통 항목 개수
    n = len(si)

    # 공통 항목이 없으면 0 리턴
    if n == 0:
        return 0

    # 모든 선호도를 합산
    sum1 = sum([prefs[p1][it] for it in si])
    sum2 = sum([prefs[p2][it] for it in si])

    # 제곱의 합을 계산
    sum1Sq = sum([(prefs[p1][it])**2 for it in si])
    sum2Sq = sum([(prefs[p2][it])**2 for it in si])

    # 곱의 합을 계산
    pSum = sum([prefs[p1][it] * prefs[p2][it] for it in si])

    # 피어슨 점수 계산
    num = pSum - (sum1*sum2/n)
    den = sqrt((sum1Sq-pow(sum1,2)/n) * (sum2Sq-pow(sum2,2)/n))
    if den == 0:
        return 0

    r = num/den

    return r
