import requests
import json

# import requests
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
        dict = {}

        if rest['Type'] == 'Post-Image':
            dict['type'] = 'image'
            dict['media'] = rest['media']
            return dict

        elif rest['Type'] == 'Post-Video':
            dict['type'] = 'video'
            dict['media'] = rest['media']
            return dict
        elif rest['Type'] == 'Corousel':
            dict['type'] = 'corousel'
            dict['media'] = rest['media']
            return dict
        else:
            return "bad"    

# inst('https://www.instagram.com/p/CZbMuQfIfKv/')    