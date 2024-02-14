from flask import Flask

import requests

app = Flask(__name__)

@app.route('/')
def index():
    # Prompt the user to enter GitHub usernames
    usernames = input("Enter GitHub usernames separated by a space: ").split()

    # Initialize the HTML output
    output = "<html><body>"

    for username in usernames:
        # Make a GET request to the GitHub API to retrieve user statistics
        response = requests.get(f'https://api.github.com/users/{username}')

        # Check if the request was successful
        if response.status_code == 200:
            # Parse the response JSON data
            user_data = response.json()

            # Add the user statistics to the HTML output
            output += f"<h1>User: {user_data['login']}</h1>"
            output += f"<p>Name: {user_data['name']}</p>"
            output += f"<p>Public Repositories: {user_data['public_repos']}</p>"
            output += f"<p>Followers: {user_data['followers']}</p>"
            output += f"<p>Following: {user_data['following']}</p>"
            output += "<hr>"
        else:
            # Print an error message if the request was not successful
            output += f"<p>Failed to retrieve user statistics for {username}: {response.status_code} - {response.reason}</p>"

    # Close the HTML tags
    output += "</body></html>"

    # Return the HTML output
    return output

if __name__ == '__main__':
    app.run()
