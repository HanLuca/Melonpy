import requests, re, json
from bs4 import BeautifulSoup
import selenium.webdriver as webdriver

options = webdriver.ChromeOptions()
options.add_argument("headless")
driver = webdriver.Chrome(options=options)

class melonAddon():

    def getSongLikesList():
        driver.get("https://www.melon.com/chart/index.htm")
        soup = BeautifulSoup(driver.page_source, 'html.parser')

        likeeList = ['likes'] # rank

        for tag in soup.findAll("tr", {"data-song-no": True}):
            likes = tag.find("button", {"class": "button_etc like"}).getText().split()[2]
            likeeList.append(likes)

        return likeeList

    # def getSongWhenRelease(SongId):
    #     driver.get(f"https://www.melon.com/song/detail.htm?songId={SongId}")
    #     soup = BeautifulSoup(driver.page_source, 'html.parser')
        
    #     releaseDay = soup.find_all("dd", limit=2)[0].getText()
    #     print(releaseDay)
