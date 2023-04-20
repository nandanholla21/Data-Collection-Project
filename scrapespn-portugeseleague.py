#all spanish league teams and player squad extraction

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

portugese_league=[]


options = Options()
options.add_argument('--headless')
chromeDriverPath = 'D:\programming\C programs\chromedriver'
driver = webdriver.Chrome(chromeDriverPath,options=options)
driver.get("https://www.espn.co.uk/football/table/_/league/por.1")
portugese_league_teams=[]             #get the names of all english league teams
portugese_league_teams_link=[]        #get the link of all english league teams
tag_name="abbr"
li = driver.find_elements(by=By.TAG_NAME,value=tag_name)
for row in li:
    portugese_league_teams.append(row.get_attribute("title"))
#print(spanish_league_teams)
xpath_tbody="/html/body/div[1]/div/div/div/main/div[3]/div/div/section/div/section/section/div[1]/div/div[2]/table/tbody"
tbody = driver.find_element(by=By.XPATH,value=xpath_tbody)
atag = tbody.find_elements(by=By.CLASS_NAME,value="AnchorLink")
for row in atag:
    if row.get_attribute("href") not in portugese_league_teams_link:
        portugese_league_teams_link.append(row.get_attribute("href"))
#print(spanish_league_teams_link)
for i in range(len(portugese_league_teams_link)):
    team = portugese_league_teams[i]
    link = portugese_league_teams_link[i]
    driver.get(link)
    xpath_squad = "/html/body/div[1]/div/div/div/main/div[2]/div[2]/nav/ul/li[5]/a"
    squad_body = driver.find_element(by=By.XPATH,value=xpath_squad)
    squad_body.click()
    xpath_goalkeeper = "/html/body/div[1]/div/div/div/main/div[2]/div[5]/div/div/section/div/section/div[4]/div[1]/div[2]/div/div[2]/table/tbody"
    tbody = driver.find_element(by=By.XPATH,value=xpath_goalkeeper)
    goalkeeper_body = tbody.find_elements(by=By.TAG_NAME,value="a")
    goalkeepers=[]
    for row in goalkeeper_body:
        portugese_league.append({
            "Team":team,
            "Name":row.text
        })
        goalkeepers.append(row.text)
#print(goalkeepers)
    outfield_player_body = driver.find_elements(by=By.CLASS_NAME,value="Table__TBODY")
    outfield_player_body = outfield_player_body[1] #to get the second tbody tag of the page
    atag = outfield_player_body.find_elements(by=By.TAG_NAME,value="a")
    outfield_players=[]
    for row in atag:
        portugese_league.append({
            "Team":team,
            "Name":row.text
        })
        outfield_players.append(row.text)
#print(outfield_players)
print(len(portugese_league))