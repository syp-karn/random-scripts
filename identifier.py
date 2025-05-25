# figure it out lol, yk what it does
import re

def extract_profile_urls(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    return set(re.findall(r'href="(https://www.instagram.com/[^/]+/?)"', content))

def find_non_followers(following_file, followers_file):
    following = extract_profile_urls(following_file)
    followers = extract_profile_urls(followers_file)
    non_followers = following - followers
    non_following = followers - following
    
    return non_followers, non_following
if __name__ == "__main__":
    following_file = r"<path_to_file>"
    followers_file = r"<path_to_file>"
    
    non_followers, non_following = find_non_followers(following_file, followers_file)
    
    print("Profiles you follow but don’t follow you back:")
    for profile in non_followers:
        print(profile)

    print("\nProfiles following you but you don’t follow back:")
    for profile in non_following:
        print(profile)
