#all spanish league teams and player squad extraction

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import sqlite3
dutch_league=[]


options = Options()
options.add_argument("--headless=new")

chromeDriverPath = 'D:\programming\C programs\chromedriver'
driver = webdriver.Chrome(chromeDriverPath,options=options)
driver.get("https://www.espn.co.uk/football/table/_/league/ned.1")
dutch_league_teams=[]             #get the names of all english league teams
dutch_league_teams_link=[]        #get the link of all english league teams
dutch_league_team_image=[]
tag_name="abbr"
li = driver.find_elements(by=By.TAG_NAME,value=tag_name)
for row in li:
    dutch_league_teams.append(row.get_attribute("title"))
#print(spanish_league_teams)
xpath_tbody="/html/body/div[1]/div/div/div/main/div[3]/div/div/section/div/section/section/div[1]/div/div[2]/table/tbody"
tbody = driver.find_element(by=By.XPATH,value=xpath_tbody)
atag = tbody.find_elements(by=By.CLASS_NAME,value="AnchorLink")
img_tag = tbody.find_elements(by=By.TAG_NAME,value="img") #
for row in img_tag:                                       #
    dutch_league_team_image.append(row.get_attribute("src")) #
for row in atag:
    if row.get_attribute("href") not in dutch_league_teams_link:
        dutch_league_teams_link.append(row.get_attribute("href"))
#print(spanish_league_teams_link)
for i in range(len(dutch_league_teams_link)):
    team = dutch_league_teams[i]
    link = dutch_league_teams_link[i]
    team_img = dutch_league_team_image[i]
    driver.get(link)
    xpath_squad = "/html/body/div[1]/div/div/div/main/div[2]/div[2]/nav/ul/li[5]/a"
    squad_body = driver.find_element(by=By.XPATH,value=xpath_squad)
    squad_body.click()
    xpath_goalkeeper = "/html/body/div[1]/div/div/div/main/div[2]/div[5]/div/div/section/div/section/div[4]/div[1]/div[2]/div/div[2]/table/tbody"
    tbody = driver.find_element(by=By.XPATH,value=xpath_goalkeeper)
    goalkeeper_body = tbody.find_elements(by=By.TAG_NAME,value="a")
    goalkeepers=[]
    for row in goalkeeper_body:
        dutch_league.append({
            "Team":team,
            "Name":row.text,
            "team_logo":team_img
        })
        goalkeepers.append(row.text)
#print(goalkeepers)
    outfield_player_body = driver.find_elements(by=By.CLASS_NAME,value="Table__TBODY")
    outfield_player_body = outfield_player_body[1] #to get the second tbody tag of the page
    atag = outfield_player_body.find_elements(by=By.TAG_NAME,value="a")
    outfield_players=[]
    for row in atag:
        dutch_league.append({
            "Team":team,
            "Name":row.text,
            "team_logo":team_img
        })
        outfield_players.append(row.text)
#print(outfield_players)
#print(len(dutch_league))
# print(dutch_league_team_image)
conn = sqlite3.connect("E:\Project X\Data.db")
cursor = conn.cursor()
cursor.execute('''
create table if not exists dutch_league(
Team TEXT,
Name TEXT,
Team_logo TEXT
)''')
conn.commit()
for item in dutch_league:
    team = str(item['Team'])
    name = str(item['Name'])
    team_logo = str(item['team_logo'])
    cursor.execute('''insert into dutch_league values(?,?,?)''',(team,name,team_logo))
    conn.commit()
conn.close()