url = "https://www.instagram.com/reel/Cm_kjvBKMOx/?utm_source=ig_web_copy_link"
path = 'estet.mp4'


from instascrape import Reel
import time

# session id
SESSIONID = "Paste session Id Here"

# Header with session id
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.74 \
    Safari/537.36 Edg/79.0.309.43"
}

# Passing Instagram reel link as argument in Reel Module
insta_reel = Reel(url)
print(insta_reel)
# Using  scrape function and passing the headers
insta_reel.scrape()

# Giving path where we want to download reel to the
# download function
insta_reel.download(fp=path)

# printing success Message
print('Downloaded Successfully.')