import json
import requests

def tk(link):
	url = "https://tiktok-downloader-download-tiktok-videos-without-watermark.p.rapidapi.com/vid/index"

	querystring = {"url":link}

	headers = {
		"X-RapidAPI-Key": "ea656f7642msha8d4e40b7b4d44cp1d7a18jsnee198964c754",
		"X-RapidAPI-Host": "tiktok-downloader-download-tiktok-videos-without-watermark.p.rapidapi.com"
	}

	response = requests.request("GET", url, headers=headers, params=querystring)
	rest = json.loads(response.text)
	print(rest)
	print(rest['video'][0])
	print(rest['music'][0])
	req = requests.get(rest['video'][0], headers=headers)
	with open('video.mp4', 'wb') as mp3:
		mp3.write(req.content)
	# return {"Video":rest['video'][0],"Music":rest['music'][0]}


tk("https://www.tiktok.com/@papakooll/video/7172486318830652673?_t=8XuGQr6lwkj&_r=1")