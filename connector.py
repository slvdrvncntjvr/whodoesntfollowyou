import json

try:
    with open('followers.json', 'r') as file:
        followers_json = json.load(file)
except FileNotFoundError:
    print("Error: 'followers.json' not found.")
    exit()
except json.JSONDecodeError:
    print("Error: invalid JSON.")
    exit()

try:
    with open('following.json', 'r') as file:
        following_json = json.load(file)
except FileNotFoundError:
    print("Error: 'following.json' not found.")
    exit()
except json.JSONDecodeError:
    print("Error: 'following.json' contains invalid JSON.")
    exit()

print("Sample followers data:", followers_json[:2])  
print("Full following data:", following_json)  

following_list = []
if isinstance(following_json, dict):
    for entry in following_json.get("relationships_following", []):
        if "string_list_data" in entry:
            following_list.append(entry["string_list_data"][0]["value"])
else:
    print("Unexpected structure in 'following.json'.")
    exit()

followers_list = []
if isinstance(followers_json, list):
    for entry in followers_json:
        if "string_list_data" in entry:
            followers_list.append(entry["string_list_data"][0]["value"])
else:
    print("Unexpected structure in 'followers.json'.")
    exit()

non_followers = [
    user for user in following_list if user.lower() not in map(str.lower, followers_list)
]

following_list = [user.strip() for user in following_list]
followers_list = [user.strip() for user in followers_list]

missing_users = [
    user for user in following_list if user.lower() not in map(str.lower, followers_list)
]

print("Following list:", following_list)
print("Followers list:", followers_list)
print("Missing users (non-followers):", missing_users)
    

if non_followers:
    print("People you follow who don't follow you back:")
    for user in non_followers:
        print(user)
else:
    print("Everyone you follow follows you back!")
