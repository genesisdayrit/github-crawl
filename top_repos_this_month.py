import requests
from datetime import datetime, timedelta

def fetch_popular_repositories():
    # Get the current date
    current_date = datetime.now()

    # Calculate the date 30 days ago
    start_date = current_date - timedelta(days=30)

    # Format the dates in YYYY-MM-DD format
    current_date_str = current_date.strftime('%Y-%m-%d')
    start_date_str = start_date.strftime('%Y-%m-%d')

    # GitHub Search API URL
    url = f'https://api.github.com/search/repositories?q=created:{start_date_str}..{current_date_str}&sort=stars&order=desc'

    # Optionally, include your GitHub token for higher rate limits
    headers = {
        'Accept': 'application/vnd.github.v3+json',
        # 'Authorization': 'token YOUR_GITHUB_TOKEN'
    }

    # Make the API request
    response = requests.get(url, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        repositories = response.json().get('items', [])

        # Print the most popular repositories
        if repositories:
            print(f"Most popular repositories created in the last 30 days:\n")
            for repo in repositories:
                print(f"Name: {repo['name']}")
                print(f"Stars: {repo['stargazers_count']}")
                print(f"URL: {repo['html_url']}\n")
        else:
            print("No repositories found for the last 30 days.")
    else:
        print(f"Failed to fetch repositories: {response.status_code}")

if __name__ == "__main__":
    fetch_popular_repositories()

