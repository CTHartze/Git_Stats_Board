import requests

# Prompt the user to enter their GitHub usernames
usernames = input("Enter GitHub usernames separated by a space: ").split()

for username in usernames:
    # Make a GET request to the GitHub API to retrieve user statistics
    response = requests.get(f'https://api.github.com/users/{username}')

    # Check if the request was successful
    if response.status_code == 200:
        # Print the user statistics
        user_data = response.json()
        print(f"User: {user_data['login']}")
        print(f"Name: {user_data['name']}")
        print(f"Public Repositories: {user_data['public_repos']}")
        print(f"Followers: {user_data['followers']}")
        print(f"Following: {user_data['following']}")
        print("----------------------------")
    else:
        # Print an error message if the request was not successful
        print(f"Failed to retrieve user statistics for {username}: {response.status_code} - {response.reason}")
