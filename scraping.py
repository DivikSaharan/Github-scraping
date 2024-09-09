import requests
from bs4 import BeautifulSoup
import pprint

def get_repo_details(repo_url):
    repo_response = requests.get(repo_url, headers={'User-Agent': "Mozilla/5.0"})
    if repo_response.status_code != 200:
        print(f"Error occurred while accessing {repo_url}")
        return None
    
    repo_content = repo_response.content
    repo_dom = BeautifulSoup(repo_content, 'html.parser')
    
    repo_details = {}
    
    repo_name = repo_dom.find('strong', {'itemprop': 'name'}).text.strip()
    repo_details['name'] = repo_name
    
    description_tag = repo_dom.find('p', {'class': 'f4 my-3'})
    repo_details['description'] = description_tag.text.strip() if description_tag else 'No description available'
    
    stars_tag = repo_dom.select_one('a[href$="/stargazers"]')
    repo_details['stars'] = stars_tag.text.strip() if stars_tag else '0'
    
    forks_tag = repo_dom.select_one('a[href$="/network/members"]')
    repo_details['forks'] = forks_tag.text.strip() if forks_tag else '0'
    
    watchers_tag = repo_dom.select_one('a[href$="/watchers"]')
    repo_details['watchers'] = watchers_tag.text.strip() if watchers_tag else '0'
    
    languages = repo_dom.find_all('span', class_='color-fg-default text-bold mr-1')
    repo_details['languages'] = [lang.text.strip() for lang in languages]
    
    contributors_tag = repo_dom.select_one('a[href$="/contributors"]')
    repo_details['contributors'] = contributors_tag.text.strip() if contributors_tag else 'No data'
    
    commits_tag = repo_dom.find('span', class_='d-none d-sm-inline')
    repo_details['commits'] = commits_tag.text.strip().split()[0] if commits_tag else 'No data'
    
    repo_size_tag = repo_dom.select_one('div.repository-content span.d-none.d-sm-inline-block')
    repo_details['size'] = repo_size_tag.text.strip() if repo_size_tag else 'No data'

    return repo_details

def get_repo():
    url = "https://github.com/mParthSaharanf?tab=repositories"
    response = requests.get(url, headers={'User-Agent': "Mozilla/5.0"})
    if response.status_code != 200:
        print("Error occurred while accessing the profile page")
        return
    html_content = response.content
    dom = BeautifulSoup(html_content, 'html.parser')
    all_repo = []
    
    my_repo = dom.select("div#user-repositories-list li")
    
    for each_myrepo in my_repo:
        href_link = each_myrepo.a.attrs['href']
        repo_url = "https://github.com" + href_link
        print(f"Scraping repository: {repo_url}")
        
        repo_details = get_repo_details(repo_url)
        if repo_details:
            all_repo.append(repo_details)
    
    return all_repo

if __name__ == "__main__":
    print("Started scraping")
    all_repos = get_repo()
    pprint.pprint(all_repos)