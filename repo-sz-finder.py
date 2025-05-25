# Helps you check the size of GitHub repositories before you clone them
import requests

def get_repo_size(url):
    fin_url = f"https://api.github.com/repos/{url}"
    response = requests.get(fin_url)
    data = response.json()
    
    if "size" in data:
        n_size = data['size'] / (1024)
        print(f"Size of repo: {n_size:.3f} MB")
    else:
        print("Error: Repository not found or API rate limit exceeded.")

url = input("Enter repository as 'user/repo': ")
get_repo_size(url)
