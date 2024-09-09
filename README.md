# Github-scraping
# GitHub Repository Scraper

A Python script to scrape details of repositories from a GitHub user's profile page. The script collects various details such as the repository name, description, stars, forks, watchers, languages, contributors, commits, and size.

## Features

- Scrapes repository information including:
  - Name
  - Description
  - Stars
  - Forks
  - Watchers
  - Languages used
  - Contributors
  - Commits
  - Size
- Outputs data in a readable format

## Requirements

- Python 3.x
- `requests` library
- `beautifulsoup4` library

You can install the required libraries using pip:

```bash
pip install requests beautifulsoup4
```

## How to Use ?
1. Clone the Repository:
```
git clone https://github.com/yourusername/your-repository.git
```
2. Navigate to the Project Directory:
```
cd your-repository
```
3. Run the Script:
Open the script file and modify the URL inside the `get_repo()` function to the desired GitHub profile page. Then run the script:
```
python script_name.py
```
Replace `script_name.py` with the name of your Python script file.
4. View the Output:
The script will print out the details of each repository to the console.


## Code Explanation
   - `get_repo_details(repo_url)`: Fetches and parses details for a specific repository given its URL. It extracts information such as the repository name, description, stars, forks, watchers, languages, 
     contributors, commits, and size.

   - `get_repo()`: Scrapes the list of repositories from a specified GitHub user's profile page and retrieves details for each repository using the `get_repo_details()` function.


## Example Output
Here's an example of what the output might look like:
```
Started scraping
Scraping repository: https://github.com/username/repository1
{'name': 'repository1',
 'description': 'Description of repository1',
 'stars': '123',
 'forks': '45',
 'watchers': '67',
 'languages': ['Python', 'JavaScript'],
 'contributors': '10',
 'commits': '200',
 'size': '1.2 MB'}
...
```

## Contributing
Feel free to contribute by creating a pull request. If you encounter any issues or have suggestions for improvements, please open an issue.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Contact
For any questions or comments, please contact DivikSaharan .






