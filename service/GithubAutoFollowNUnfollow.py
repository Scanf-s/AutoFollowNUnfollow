# service/GithubAutoFollowNUnfollow.py

import requests


class GithubAutoFollowNUnfollow:
    def __init__(self, username, token):
        self.github_api_url = "https://api.github.com"
        self.github_username = username
        self.github_token = token

        self.request_headers = {
            "Authorization": f"token {self.github_token}",
            "Accept": "application/vnd.github.v3+json"
        }

    def get_users(self, behavior: str) -> set:
        """
        https://docs.github.com/ko/rest/users/followers?apiVersion=2022-11-28#list-the-people-a-user-follows
        https://docs.github.com/ko/rest/users/followers?apiVersion=2022-11-28#list-followers-of-a-user
        :param behavior:
        :return:
        """

        users = set()
        page = 1
        while True:
            response = requests.get(
                f"{self.github_api_url}/users/{self.github_username}/{behavior}?per_page=100&page={page}",
                headers=self.request_headers
            )
            response.raise_for_status()

            page_users = response.json()
            if not page_users:
                break

            users.update(user["login"] for user in page_users)
            page += 1

        return users

    def follow_user(self, follow_target: str) -> None:
        """
        https://docs.github.com/ko/rest/users/followers?apiVersion=2022-11-28#follow-a-user
        :param follow_target:
        :return:
        """

        response = requests.put(
            f"{self.github_api_url}/user/following/{follow_target}",
            headers=self.request_headers
        )
        response.raise_for_status()
        print(f"Successfully followed {follow_target}")

    def unfollow_user(self, unfollow_target: str) -> None:
        """
        https://docs.github.com/ko/rest/users/followers?apiVersion=2022-11-28#unfollow-a-user
        :param unfollow_target:
        :return:
        """

        response = requests.delete(
            f"{self.github_api_url}/user/following/{unfollow_target}",
            headers=self.request_headers
        )
        response.raise_for_status()
        print(f"Successfully unfollowed {unfollow_target}")

    def run(self):
        followers = self.get_users("followers")
        following = self.get_users("following")

        print(f"Followers: {len(followers)}")
        print(f"Following: {len(following)}")

        # Follow users who follow you, but you don't follow back
        to_follow = followers - following
        if len(to_follow) > 0:
            print("Follow target list : ")
            print(to_follow)
            for user in to_follow:
                self.follow_user(user)

        # Unfollow users who don't follow you back
        to_unfollow = following - followers
        if len(to_unfollow) > 0:
            print("UnFollow target list : ")
            print(to_unfollow)
            for user in to_unfollow:
                self.unfollow_user(user)

        print("Job Done!")
