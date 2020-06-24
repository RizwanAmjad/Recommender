import time

start = time.time()
from Recommender import Recommender


def main():
    user_list = [1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0]
    recommender_obj = Recommender('posts.csv', user_list)
    print(recommender_obj.recommend())


if __name__ == '__main__':
    main()
    print(time.time() - start)
