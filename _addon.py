import requests
from bs4 import BeautifulSoup
from selenium import webdriver

options = webdriver.ChromeOptions()

options.add_argument("headless")
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(options=options)

class MelonAddon:

    @staticmethod
    def getSongLikesList():
        driver.get("https://www.melon.com/chart/index.htm")
        soup = BeautifulSoup(driver.page_source, 'html.parser')

        likeeList = []

        for tag in soup.find_all("tr", {"data-song-no": True}):
            likes = tag.find("button", {"class": "button_etc like"}).getText().split()[2]
            likeeList.append(likes)

        return likeeList

    @staticmethod
    def getSongWhenRelease(SongId):
        html = requests.get(
            f"https://www.melon.com/song/detail.htm?songId={SongId}",
            headers={
                "User-Agent": "github.com/hanluca/Melonpy"
            }
        ).text
        soup = BeautifulSoup(html, "lxml")
        
        releaseDay = soup.find_all("dd", limit=2)[1].getText()
        return releaseDay

    @staticmethod
    def getCommentAmount(SongId):
        driver.get(f"https://www.melon.com/song/detail.htm?songId={SongId}")
        soup = BeautifulSoup(driver.page_source, 'html.parser')

        commentAmount = soup.find("span", {"class": "text", "id": "revCnt"}).getText()
        return commentAmount