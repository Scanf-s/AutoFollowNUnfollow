import logging
import os
from dotenv import load_dotenv
from service.GithubAutoFollowNUnfollow import GithubAutoFollowNUnfollow

# Load environment variables from .env file
load_dotenv()

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def get_github_credentials():
    your_username = os.getenv("GITHUB_USERNAME")
    your_token = os.getenv("GITHUB_TOKEN")

    if not your_username or not your_token:
        raise ValueError("GitHub username and token must be set in the .env file!! Please see README.md")

    return your_username, your_token


if __name__ == "__main__":
    try:
        username, token = get_github_credentials()
        github_instance = GithubAutoFollowNUnfollow(username, token)
        github_instance.run()
    except ValueError as e:
        logging.error(f"Error: {e}")
        logging.error("Please make sure GITHUB_USERNAME and GITHUB_TOKEN are set in your .env file!! Plz see README.md")
