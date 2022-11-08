from requests import request, Response


class SocialNetworkApiClient:
    sign_up_url = 'http://127.0.0.1:8000/api/auth/register/'
    sign_in_url = 'http://127.0.0.1:8000/api/auth/token/'
    create_post_url = 'http://127.0.0.1:8000/api/posts/'
    like_post_url = 'http://127.0.0.1:8000/api/likes/'

    @staticmethod
    def client(method: str, url: str, headers: dict, data: dict) -> Response:
        return request(method=method, url=url, headers=headers, data=data)

    def sign_up(self, username: str, password: str) -> str:
        data = {'username': username, 'password': password, 'password2': password}
        self.client(method='post', url=self.sign_up_url, headers={}, data=data)

    def sign_in(self, username: str, password: str) -> str:
        data = {'username': username, 'password': password}
        response = self.client(method='post', url=self.sign_in_url, headers={}, data=data)
        user_token = response.json().get('access')
        return user_token

    def create_post(self, title: str, content: str, user_token: str) -> Response:
        data = {'title': title, 'content': content}
        headers = {'Authorization': f'Bearer {user_token}'}
        post_data = self.client(method='post', url=self.create_post_url, headers=headers, data=data)
        return post_data.json()

    def post_like(self, user_token: str, post_id: int):
        data = {'post_id': post_id}
        headers = {'Authorization': f'Bearer {user_token}'}
        self.client(method='post', url=self.like_post_url, headers=headers, data=data)
