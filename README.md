# github crawl

## Project Overview

The GitHub Crawl Project is a Python-based solution designed to fetch and store data on the most popular GitHub repositories created within specific timeframes (last 30 days, last 180 days). The data is fetched from the GitHub API and written to a Google Sheet for further analysis and record-keeping.

### Project Structure

``` plaintext
/path/to/your/github-crawl/
├── README.md
├── credentials
│   └── <your-gdrive-credentials>.json
├── requirements.txt
├── top_repos_this_month.py
├── write_to_sheet_30.py
├── write_to_sheet_180.py
├── .env
└── .env.example
```

### Files and Directories

- **README.md**: This file. Provides an overview and usage instructions for the project.
- **credentials/<your-gdrive-credentials,json>.**: Contains the Google API credentials required to interact with Google Sheets. Ensure this file is securely stored and not shared.
- **requirements.txt**: Lists the Python dependencies needed to run the scripts. These dependencies can be installed using pip.
- **top_repos_this_month.py**: A script that fetches the top repositories created in the current month.
- **write_to_sheet_30.py**: Fetches and writes the top repositories from the last 30 days to a Google Sheet.
- **write_to_sheet_180.py**: Fetches and writes the top repositories from the last 180 days to a Google Sheet.

## Dependencies

The project requires the following Python packages:

- gspread
- oauth2client
- requests
- python-dotenv

You can install these dependencies using the following command:

``` bash
pip install -r requirements.txt
```

## Environment Setup

### Environment Variables

The project relies on environment variables for configuration. These variables should be stored in a `.env` file in the project root directory:

- **GDRIVE_CREDENTIALS_PATH**: Path to the Google API credentials JSON file.
- **SPREADSHEET_ID**: The ID of the Google Sheet where the repository data will be written.

Example `.env` file:

``` plaintext
GDRIVE_CREDENTIALS_PATH=/path/to/github-crawl/credentials/<your-gdrive-credentials-file.json>
SPREADSHEET_ID=your_spreadsheet_id_here
```

## Usage

### Fetching and Writing Top Repositories

The project includes scripts that fetch the top GitHub repositories from different time periods and write them to a Google Sheet.

1. **Last 30 Days**:
   - Script: `write_to_sheet_30.py`
   - Description: Fetches the top repositories created in the last 30 days and writes the data to a Google Sheet tab named `{YYYY-MM-DD}_top_gh_repos_30`.

   python write_to_sheet_30.py

2. **Last 180 Days**:
   - Script: `write_to_sheet_180.py`
   - Description: Fetches the top repositories created in the last 180 days and writes the data to a Google Sheet tab named `{YYYY-MM-DD}_top_gh_repos_180`.

   python write_to_sheet_180.py

3. **Current Month**:
   - Script: `top_repos_this_month.py`
   - Description: Fetches the top repositories created in the current month. (Customize as needed.)

   python top_repos_this_month.py

### Running the Scripts

Before running any script, ensure that the environment is set up with the necessary dependencies and environment variables.

Execute the desired script from the terminal:

``` bash
python write_to_sheet_30.py  # For last 30 days
python write_to_sheet_180.py  # For last 180 days
```

The scripts will fetch the data from GitHub, process it, and write the results to the specified Google Sheet.

## Contributing

Contributions are welcome! If you have suggestions for improving this project, please submit an issue or fork the repository and submit a pull request.


## Contact

For questions or support, you can reach out to me on x @_genesisdayrit

