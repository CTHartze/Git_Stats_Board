import requests

# Prompt the user to enter their GitHub username
username = input("Enter your GitHub username: ")

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
else:
    # Print an error message if the request was not successful
    print(f"Failed to retrieve user statistics: {response.status_code} - {response.reason}")
