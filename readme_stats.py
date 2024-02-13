import requests

# Prompt the user to enter their GitHub username
username = input("Enter your GitHub username: ")

# Make a GET request to the github-readme-stats API to retrieve user statistics
response = requests.get(f'https://github-readme-stats.vercel.app/api?username={username}')

# Check if the request was successful
if response.status_code == 200:
    # Print the user statistics
    user_data = response.json()
    print(f"User: {user_data['username']}")
    print(f"Most Used Languages: {user_data['top_languages']}")
    print(f"Total Repositories: {user_data['total_repos']}")
    print(f"Total Commits: {user_data['commits']}")
    print(f"Total Pull Requests: {user_data['pull_requests']}")
    print(f"Total Issues: {user_data['issues']}")
    print(f"Total Stars: {user_data['total_stars']}")
    print(f"Total Forks: {user_data['total_forks']}")
else:
    # Print an error message if the request was not successful
    print(f"Failed to retrieve user statistics: {response.status_code} - {response.reason}")
