import requests
import json

def inst(link):

    url = "https://instagram-downloader-download-instagram-videos-stories.p.rapidapi.com/index"

    querystring = {"url":link}

    headers = {
        "X-RapidAPI-Key": "ea656f7642msha8d4e40b7b4d44cp1d7a18jsnee198964c754",
        "X-RapidAPI-Host": "instagram-downloader-download-instagram-videos-stories.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    rest = json.loads(response.text)
    if 'error' in rest:
        return "error"
    else:
        dict1 = {}

        if rest['Type'] == 'Post-Image':
            dict1['type'] = 'image'
            dict1['media'] = rest['media']
            return dict1

        elif rest['Type'] == 'Post-Video':
            dict1['type'] = 'video'
            dict1['media'] = rest['media']
            print(dict1)
            # savae video
            req = requests.get(rest['media'], headers=headers)
            with open('video.mp4', 'wb') as mp3:
                mp3.write(req.content)
            # - - - - - - -
            return dict1
        elif rest['Type'] == 'Corousel':
            dict1['type'] = 'corousel'
            dict1['media'] = rest['media']
            return dict1
        else:
            return "bad"

inst('https://www.instagram.com/reel/CnG9Ll1pDVF/?utm_source=ig_web_copy_link')