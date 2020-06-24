import pandas as pd

class Recommender:

    def __init__(self, post_list, user_interests):
        """
        Recommender class constructor
        takes two parameters post_list and user_interests
        post_list is the 2d iterateable of Pandas preffered
        user_interest is any 1d iterateable

        """
        self.posts = post_list
        self.user = pd.Series(user_interests, index=self.posts.columns)

    def recommend(self):
        """
        takes no parameter
        :return: sorted indexes of the post DataFrame which is attribute of Recommender class
        """
        result = self.posts * self.user
        # print(result.sum())
        return result.sum(axis=1).sort_values(ascending=False).index
