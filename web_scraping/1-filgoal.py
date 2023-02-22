import requests
import csv
from bs4 import BeautifulSoup
def main():
    date = "2023-02-19"
    page = requests.get(f"https://www.filgoal.com/matches/?date={date}")
    web_scraping(page)

def web_scraping(page):
    src = page.content
    soup = BeautifulSoup(src, "lxml")

    championship_list = soup.find("div", {'id': 'match-list-viewer'}).find_all("div", {'class': 'mc-block'})
    
    for championship in championship_list:
        # getting championship name
        champion_name = championship.find("span").text
    
        matches_list = championship.find_all("div", {"class": "cin_cntnr"})

        # iterate for each match in every championship
        for match in matches_list:
            match_info(match)


def match_info(match):
    team_a = match.find("div", "cin_cntnr").find("div", {"class": "f"}).find("strong").text
    team_a_result = match.find("div", {"class": "f"}).find("b").text
    team_b = match.find("div", {"class": "s"}).find("strong").text
    team_b_result = match.find("div", {"class": "s"}).find("b").text
    
    result = f"{team_a_result} - {team_b_result}"
    

main()