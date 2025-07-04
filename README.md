# What is this?

This program is designed to reduce the hassle of following and following by hand. When you run this program, it automatically follows/unfollows.

I've only done a simple test (tested by canceling the follow and following the user again using this Python script), so it may not function properly or might need improvement in the future.

# How to install

## 1. Install dependencies
```shell
curl -LsSf https://astral.sh/uv/install.sh | sh
uv venv .venv
uv sync
```

## 2. Make .env file and set environment variables

```shell
# In project...
vim .env

# .env file seems like..
# GITHUB_API_URL=https://api.github.com
# GITHUB_USERNAME=YOUR GITHUB USER NAME
# GITHUB_TOKEN=YOUT GITHUB AUTH TOKEN
```

## 3. Run main.py
```shell
source .venv/bin/activate
python main.py
```

# Sample

There are two users I have to follow

![스크린샷 2024-09-07 11-46-14](https://github.com/user-attachments/assets/a1708383-8ac6-4986-a362-398e443b2043)

Run python script

![스크린샷 2024-09-07 11-47-12](https://github.com/user-attachments/assets/614e255d-0ccb-4b0f-ac12-b9c9d65dc04b)


Result

![image](https://github.com/user-attachments/assets/53db713c-6801-4b22-b9aa-86f731df7a2f)
