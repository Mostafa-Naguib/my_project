"""
We're creating a project where the user can type a specific date, 
so the program creates a csv file contain all the matches details relate to this date
_________________________________________________________________
1-main ---> take the date from the user and then give it to "web_scrapping" function hoping that could give a list of the match details, 
 so it stores it in a csv file.....
2-web_scrapping ---> in this function we take the returning contents from get request as an argument and 
 then we use BeautifulSoup function get all the information as HTML elements and then we search for championships_list, 
 we iterate over each championship looking for their matches passing each match for "match_info function"
3-in this function we get the names of each team, the result of the match and the time of the this match
 and then we store them in dictionary meanwhile we append the dictionary to a list
"""



import requests
import csv
from bs4 import BeautifulSoup
import datetime
import re

matches_list = []

def main():
    global matches_list
    # prompting the user to enter a specific date
    while 1:
        try:
            date = input("Enter the date in the following format YYYY-MM-DD: ")
            date_format = r"%Y-%m-%d"
            datetime.datetime.strptime(date, date_format)
            break
        except ValueError:
            print("Incorrect data format, should be YYYY-MM-DD")

    page = requests.get(f"https://www.filgoal.com/matches/?date={date}")

    web_scraping(page)

    keys = matches_list[0].keys()
    # here we create a csv file and then we store matches_list in it
    with open("filgoal.csv", "w", encoding="utf-8") as file:
            writer = csv.DictWriter(file, keys)
            writer.writeheader()
            writer.writerows(matches_list)



def web_scraping(page):
    global championship_title

    src = page.content
    soup = BeautifulSoup(src, "lxml")

    championship_list = soup.find("div", {'id': 'match-list-viewer'}).find_all("div", {'class': 'mc-block'})
    
    # iterating over each championships
    for championship in championship_list:
        # getting championship name
        championship_title = championship.find("span").text.strip()

        matches_list = championship.find_all("div", {"class": "cin_cntnr"})        
        
        # iterating over each match in the championships
        for match in matches_list:
            match_info(match)

def match_info(match):
    # getting teams' name and the result of the match
    part_one = match.find("div", "c-i-next")
    team_a = part_one.find("div", {"class": "f"}).find("strong").text.strip()
    team_a_result = part_one.find("div", {"class": "f"}).find("b").text.strip()
    team_b = part_one.find("div", {"class": "s"}).find("strong").text.strip()
    team_b_result = part_one.find("div", {"class": "s"}).find("b").text.strip()

    # getting the result of the match
    result = f"{team_a_result}-{team_b_result}".strip()
    
    # getting the time of the match
    part_two = match.find("div", "match-aux").find_all("span")
    date = part_two[len(part_two)-1].text.strip()
    time = re.search("(\d{2}:\d{2})", date).group(1)
    

    matches_list.append({"نوع البطولة":championship_title, "الفريق الأول":team_a, "الفريق الثاني": team_b, 
    "ميعاد المباراة": time, "النتيجة": result})


main()
