import requests

def get_repo_size(user, repo):
    url = f"https://api.github.com/repos/iden3/circom"
    response = requests.get(url)
    data = response.json()
    
    if "size" in data:
        print(f"Size of {user}/{repo}: {data['size']} KB")
    else:
        print("Error: Repository not found or API rate limit exceeded.")

get_repo_size("git", "git")
