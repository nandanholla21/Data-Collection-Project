from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import sqlite3
options = Options()
import time
# options.add_argument("--headless=new")
# options.add_argument("--incognito")
urls = []
img_urls = []
chromeDriverPath = 'D:\programming\C programs\chromedriver'
driver = webdriver.Chrome(chromeDriverPath,options=options)
iterate_urls = ["https://www.premierleague.com/players?se=578&cl=1","https://www.premierleague.com/players?se=578&cl=2",
"https://www.premierleague.com/players?se=578&cl=127","https://www.premierleague.com/players?se=578&cl=130",
"https://www.premierleague.com/players?se=578&cl=131","https://www.premierleague.com/players?se=578&cl=43",
"https://www.premierleague.com/players?se=578&cl=4","https://www.premierleague.com/players?se=578&cl=6",
"https://www.premierleague.com/players?se=578&cl=7","https://www.premierleague.com/players?se=-1&cl=34",
"https://www.premierleague.com/players?se=578&cl=10","https://www.premierleague.com/players?se=578&cl=163","https://www.premierleague.com/players?se=578&cl=11",
"https://www.premierleague.com/players?se=578&cl=12","https://www.premierleague.com/players?se=578&cl=23",
"https://www.premierleague.com/players?se=578&cl=15","https://www.premierleague.com/players?se=578&cl=18",
"https://www.premierleague.com/players?se=578&cl=21","https://www.premierleague.com/players?se=578&cl=25",
"https://www.premierleague.com/players?se=578&cl=38"]
nationality_img=[]
player_name = []
iterate_urls = iterate_urls[19::]
c=0
time.sleep(1)
for u in iterate_urls:
    driver.get(u)
    time.sleep(1)
    try:
        xpath_of_accept_cookies = "/html/body/div[3]/div[2]/div/div/div[2]/div/div/button"
        button = driver.find_element(by=By.XPATH,value=xpath_of_accept_cookies)
        button.click()
    except Exception:
        pass
    time.sleep(2)
    anchor_tag_xpath = "/html/body/main/div[1]/nav/a[1]"  # this was a ad. not every time this would be displayed
    # time.sleep(1)
    try:
        skip = driver.find_element(by=By.XPATH,value=anchor_tag_xpath)
        skip.click()
    except Exception:
        pass
    time.sleep(2)
    xpath_a = "/html/body/main/div[2]/div/div/div/table/tbody/tr/td"
    a_tag = driver.find_elements(by=By.XPATH, value=xpath_a)
    for ele in a_tag:
        try:
            anchor_t = ele.find_element(by=By.TAG_NAME,value="a")
            urls.append(anchor_t.get_attribute("href"))
            # break
        except NoSuchElementException:
            pass
    break
for url in urls:
    driver.get(url)
    anchor_tag_xpath = "/html/body/main/div[1]/nav/a[1]"  # this was a ad. not every time this would be displayed
    time.sleep(2)
    try:
        skip = driver.find_element(by=By.XPATH,value=anchor_tag_xpath)
        skip.click()
    except Exception:
        pass
    time.sleep(2)
    img_xpath = "/html/body/main/section/div[2]/div[1]/img"
    img = driver.find_element(by=By.XPATH,value=img_xpath)
    img_urls.append(img.get_attribute("src"))
    time.sleep(1)
    nationality_img_xpath = "/html/body/main/div[2]/div/div/div[2]/section[1]/div[1]/div[1]/div[2]/span[1]/img"
    img = driver.find_element(by=By.XPATH,value=nationality_img_xpath)
    nationality_img.append(img.get_attribute("src"))
    name_xpath="/html/body/main/div[2]/div/div/div[2]/section[1]/h3"
    time.sleep(2)
    name_div_xpath = "/html/body/main/section/div[2]/div[2]/h1/div"
    time.sleep(2)
    class_name = 't-colour'
    parent_div = driver.find_elements(by=By.CLASS_NAME,value="t-colour")
    two_divs = parent_div[0].find_elements(by=By.TAG_NAME,value='div')
    first_name=""
    last_name=""
    name=""
    try:
        if len(two_divs) == 0:
            raise Exception
        elif len(two_divs) == 1:
            first_name = two_divs[0].text
            name = first_name
            player_name.append(name)
        elif len(two_divs) == 2:
            first_name = two_divs[0].text
            last_name = two_divs[1].text
            name = first_name +" "+last_name 
            player_name.append(name)
        else:
            pass
    except Exception:
        pass
    # first_name_xpath = "/html/body/main/section/div[2]/div[2]/h1/div/div[1]" # for arsenal
    # first_name_xpath="/html/body/main/section/div[2]/div[3]/h1/div/div[1]" # for aston villa
    # last_name_xpath = "/html/body/main/section/div[2]/div[2]/h1/div/div[2]" # for arsenal
    # last_name_xpath="/html/body/main/section/div[2]/div[3]/h1/div/div[2]" # for aston villa
    # first_name = driver.find_elements(by=By.XPATH,value=first_name_xpath)
    # time.sleep(1)
    # last_name = driver.find_elements(by=By.XPATH,value=last_name_xpath)
    # time.sleep(1)
    # try:
    #     if len(first_name)!=0 and len(last_name) ==0:
    #         name = first_name[0].text
    #         player_name.append(name)
    #     elif len(first_name)!=0 and len(last_name)!=0:
    #         name =first_name[0].text+" "+last_name[0].text
    #         player_name.append(name)
    #     else:
    #         raise IndexError
    # except IndexError:
    #     pass
print(img_urls)
print(len(img_urls))
print(len(nationality_img))
print(len(player_name))
print(player_name)

full_dict=[]
for i in range(len(img_urls)):
    full_dict.append({"Img_Url":img_urls[i],
                       "Nationality":nationality_img[i],
                       "Name":player_name[i] 
                     }
                     )
conn = sqlite3.connect("E:\Project X\Data.db")
cursor = conn.cursor()
cursor.execute('''
create table if not exists premier_league_image(
Nationality_Logo TEXT,
Name TEXT,
Player_Image TEXT
)''')
conn.commit()
for i in range(len(full_dict)):
    cursor.execute('''insert into premier_league_image values(?,?,?)''',(full_dict[i]['Nationality'],full_dict[i]['Name'],full_dict[i]["Img_Url"]))
    conn.commit()
conn.close()