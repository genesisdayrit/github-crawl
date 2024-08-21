import os
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime, timedelta
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Read the credentials file path and spreadsheet ID from the environment variables
creds_file = os.getenv('GDRIVE_CREDENTIALS_PATH')
spreadsheet_id = os.getenv('SPREADSHEET_ID')

if not creds_file:
    raise ValueError("The environment variable GDRIVE_CREDENTIALS_PATH is not set.")
if not spreadsheet_id:
    raise ValueError("The environment variable SPREADSHEET_ID is not set.")

# Define the scope and credentials
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name(creds_file, scope)
client = gspread.authorize(creds)

# Open the Google Sheet
spreadsheet = client.open_by_key(spreadsheet_id)

# Calculate date range for the last 30 days
current_date = datetime.now()
start_date = current_date - timedelta(days=30)
current_date_str = current_date.strftime('%Y-%m-%d')
start_date_str = start_date.strftime('%Y-%m-%d')

# GitHub Search API URL template
url_template = f'https://api.github.com/search/repositories?q=created:{start_date_str}..{current_date_str}&sort=stars&order=desc&per_page=100&page='

# Optionally, include your GitHub token for higher rate limits
headers = {
    'Accept': 'application/vnd.github.v3+json',
    # 'Authorization': 'token YOUR_GITHUB_TOKEN'
}

# Initialize an empty list to collect repository data
all_repositories = []

# Paginate through the results
page = 1
while True:
    response = requests.get(f"{url_template}{page}", headers=headers)
    
    if response.status_code == 200:
        repositories = response.json().get('items', [])
        if not repositories:
            break  # No more repositories to fetch
        
        all_repositories.extend(repositories)
        if len(all_repositories) >= 1000:
            break  # Stop if we reach the GitHub API limit of 1000 results
        page += 1
    else:
        raise ValueError(f"Failed to fetch repositories: {response.status_code}")

# Prepare data to be written to the sheet
repo_data = [["Name", "Full Name", "Owner", "Owner's Profile", "Description", "URL", "Stars", "Forks", "Primary Language", 
              "Creation Date", "License", "Watchers", "Default Branch", "Homepage", "Size", "Is Fork", "Topics", "Visibility"]]

for repo in all_repositories:
    repo_data.append([
        repo['name'],
        repo['full_name'],
        repo['owner']['login'],
        repo['owner']['html_url'],
        repo['description'],
        repo['html_url'],
        repo['stargazers_count'],
        repo['forks_count'],
        repo['language'],
        repo['created_at'],
        repo['license']['name'] if repo['license'] else 'No license',
        repo['watchers_count'],
        repo['default_branch'],
        repo['homepage'] if repo['homepage'] else 'No homepage',
        repo['size'],
        repo['fork'],
        ', '.join(repo['topics']) if repo['topics'] else 'No topics',
        repo['visibility']
    ])

# Determine the tab name
tab_name = f"{current_date.strftime('%Y-%m-%d')}_top_gh_repos_30"

# Check if the worksheet exists
try:
    sheet = spreadsheet.worksheet(tab_name)
    spreadsheet.del_worksheet(sheet)  # Delete the existing worksheet if found
except gspread.exceptions.WorksheetNotFound:
    pass

# Create a new sheet with the required name
new_sheet = spreadsheet.add_worksheet(title=tab_name, rows=len(repo_data), cols=len(repo_data[0]))

# Write all the data at once
new_sheet.update('A1', repo_data)

print(f"Output successfully written to new sheet '{tab_name}' in the spreadsheet.")

