import time
t = time.time()
print("Started")
from Recommender import Recommender
import pandas as pd

to_be_recommended = pd.read_csv('train.csv')
to_be_recommended.set_index(to_be_recommended.Id, inplace=True)
to_be_recommended.drop(['Id', 'Genre'], axis=1, inplace=True)
print(to_be_recommended.columns)

# ['Action', 'Adventure', 'Animation', 'Biography', 'Comedy', 'Crime',
#        'Documentary', 'Drama', 'Family', 'Fantasy', 'History', 'Horror',
#        'Music', 'Musical', 'Mystery', 'N/A', 'News', 'Reality-TV', 'Romance',
#        'Sci-Fi', 'Short', 'Sport', 'Thriller', 'War', 'Western']
user_interested_tags = [1, 0, 1, 0, 1, 1,
       0, 0, 1, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0,
       1, 0, 0, 1, 1, 0]
recommender = Recommender(to_be_recommended, user_interested_tags)
print(recommender.recommend())
print(time.time() - t)
