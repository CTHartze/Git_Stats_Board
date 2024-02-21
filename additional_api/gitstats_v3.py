import requests

# Prompt the user to enter their GitHub username
username = input("Enter your GitHub username: ")

# Make a GET request to the GitHub API to retrieve user statistics
response = requests.get(f'https://api.github.com/users/{username}')

# Check if the request was successful
if response.status_code == 200:
    # Parse the response JSON data
    user_data = response.json()
    
    # Make a GET request to the GitHub API to retrieve the user's repositories
    repos_response = requests.get(user_data['repos_url'])
    
    # Check if the request was successful
    if repos_response.status_code == 200:
        # Parse the response JSON data
        repos_data = repos_response.json()
        
        # Calculate the desired statistics
        total_repos = len(repos_data)
        total_commits = 0
        total_pull_requests = 0
        total_issues = 0
        total_stars = 0
        total_forks = 0
        languages = {}
        for repo in repos_data:
            # Make a GET request to the GitHub API to retrieve the repository's statistics
            stats_response = requests.get(f'{repo["url"]}/stats/participation')
            
            # Check if the request was successful
            if stats_response.status_code == 200:
                # Parse the response JSON data
                stats_data = stats_response.json()
                
                # Calculate the total commits
                total_commits += sum(stats_data['all'])
                
            # Make a GET request to the GitHub API to retrieve the repository's pull requests
            pull_requests_response = requests.get(f'{repo["url"]}/pulls')
            
            # Check if the request was successful
            if pull_requests_response.status_code == 200:
                # Parse the response JSON data
                pull_requests_data = pull_requests_response.json()
                
                # Calculate the total pull requests
                total_pull_requests += len(pull_requests_data)
                
            # Make a GET request to the GitHub API to retrieve the repository's issues
            issues_response = requests.get(f'{repo["url"]}/issues')
            
            # Check if the request was successful
            if issues_response.status_code == 200:
                # Parse the response JSON data
                issues_data = issues_response.json()
                
                # Calculate the total issues
                total_issues += len(issues_data)
                
            # Add the repository's language to the languages dictionary
            if repo['language'] is not None:
                if repo['language'] in languages:
                    languages[repo['language']] += 1
                else:
                    languages[repo['language']] = 1
                    
            # Add the repository's stars and forks to the totals
            total_stars += repo['stargazers_count']
            total_forks += repo['forks_count']
        
        # Sort the languages dictionary by value in descending order
        sorted_languages = sorted(languages.items(), key=lambda x: x[1], reverse=True)
        
        # Print the user statistics
        print(f"User: {username}")
        print(f"Most Used Languages: {sorted_languages[:3]}")
        print(f"Total Repositories: {total_repos}")
        print(f"Total Commits: {total_commits}")
        print(f"Total Pull Requests: {total_pull_requests}")
        print(f"Total Issues: {total_issues}")
        print(f"Total Stars: {total_stars}")
        print(f"Total Forks: {total_forks}")
    else:
        # Print an error message if the request was not successful
        print(f"Failed to retrieve user repositories: {repos_response.status_code} - {repos_response.reason}")
else:
    # Print an error message if the request was not successful
    print(f"Failed to retrieve user data: {response.status_code} - {response.reason}")
