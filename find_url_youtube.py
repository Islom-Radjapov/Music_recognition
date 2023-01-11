from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# driver = webdriver.Chrome()
def get_url_in_youtube(shazam_url):
    driver = webdriver.Chrome()

    driver.get(shazam_url)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'video-container')))

    element = driver.find_element(By.ID, "yt-videocontainer")
    url = element.get_attribute('data-href')  # find url in youtube
    driver.close()
    return url
# print(get_url_in_youtube("https://www.shazam.com/track/629328410/chumoli-feat-konsta"))
# "https://www.youtube.com/watch?v=VNBxmb9VLRM"