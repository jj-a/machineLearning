# recommend movie test 2
# 영화 추천 알고리즘 테스트 (피어슨 상관계수)


from recommendation.movieRecommendationEx import recommendation_by_pearson as re
from recommendation.movieRecommendationEx import dataset as data

for item in data.critics:
    print("Lisa Rose and", item, re.sim_pearson(data.critics, "Lisa Rose", item))
