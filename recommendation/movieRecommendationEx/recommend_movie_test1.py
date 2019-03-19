# recommend movie test 1
# 영화 추천 알고리즘 테스트 (유클리디안 거리점수)


from recommendation.movieRecommendationEx import recommendation_by_euclidean as re
from recommendation.movieRecommendationEx import dataset as data

for item in data.critics:
    print("Toby and", item, re.sim_distance(data.critics, 'Toby', item))
