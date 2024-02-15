from flask import Flask, render_template_string

import requests

app = Flask(__name__)

@app.route('/')
def index():
    # Prompt the user to enter GitHub usernames
    usernames = request.args.get('usernames', '').split()

    # Initialize the HTML output
    output = render_template_string("""
        <html><body>
        {% for username in usernames %}
            <h1>User: {{ username }}</h1>
            {% if response.status_code == 200 %}
                <p>Name: {{ user_data['name'] }}</p>
                <p>Public Repositories: {{ user_data['public_repos'] }}</p>
                <p>Followers: {{ user_data['followers'] }}</p>
                <p>Following: {{ user_data['following'] }}</p>
                <hr>
            {% else %}
                <p>Failed to retrieve user statistics for {{ username }}: {{ response.status_code }} - {{ response.reason }}</p>
            {% endif %}
        {% endfor %}
        </body></html>
    """, usernames=usernames)

    for username in usernames:
        try:
            # Make a GET request to the GitHub API to retrieve user statistics
            response = requests.get(f'https://api.github.com/users/{username}')

            # Check if the request was successful
            if response.status_code == 200:
                # Parse the response JSON data
                user_data = response.json()

                # Add the user statistics to the HTML output
                output = output.replace(f'{{ user_data["name"] }}', user_data['name'])
                output = output.replace(f'{{ user_data["public_repos"] }}', str(user_data['public_repos']))
                output = output.replace(f'{{ user_data["followers"] }}', str(user_data['followers']))
                output = output.replace(f'{{ user_data["following"] }}', str(user_data['following']))
        except Exception as e:
            output = output.replace(f'<h1>User: {username}</h1>', f'<p>Error: {str(e)}</p>')

    return output

if __name__ == '__main__':
    app.run()
