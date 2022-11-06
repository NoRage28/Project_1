from automated_bot.utils import get_random_username, get_random_password, get_random_text
from automated_bot.client import SocialNetworkApiClient
from automated_bot.settings import NUMBER_OF_USERS, MAX_LIKES_PER_USER, MAX_POSTS_PER_USER
import random


class BotService:
    users = list()
    posts = list()

    def __init__(self, client):
        self.client = client

    def create_users(self, number_of_users: int):
        for _ in range(number_of_users):
            username = get_random_username()
            password = get_random_password()
            self.client.sign_up(username=username, password=password)
            self.users.append({'username': username, 'password': password})

    def create_posts(self, max_post_per_user: int):
        for user in self.users:
            username = user.get('username')
            password = user.get('password')
            user_token = self.client.sign_in(username=username, password=password)
            random_count_post = random.randint(1, max_post_per_user)
            for _ in range(random_count_post):
                title = get_random_text()
                content = get_random_text()
                post = self.client.create_post(title=title, content=content, user_token=user_token)
                self.posts.append(post)

    def create_likes(self, max_likes_per_user: int):
        for user in self.users:
            username = user.get('username')
            password = user.get('password')
            user_token = self.client.sign_in(username=username, password=password)
            random_count_like = random.randint(1, max_likes_per_user)
            for _ in range(1, random_count_like):
                random_post_id = random.choice(self.posts).get('id')
                self.client.post_like(user_token=user_token, post_id=random_post_id)


def main():
    client = SocialNetworkApiClient()
    bot = BotService(client)
    bot.create_users(number_of_users=NUMBER_OF_USERS)
    bot.create_posts(max_post_per_user=MAX_POSTS_PER_USER)
    bot.create_likes(max_likes_per_user=MAX_LIKES_PER_USER)


if __name__ == '__main__':
    main()
