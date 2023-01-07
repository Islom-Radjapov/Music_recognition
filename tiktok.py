def tk(link):
	import json
	import requests
	url = "https://tiktok-downloader-download-tiktok-videos-without-watermark.p.rapidapi.com/vid/index"

	querystring = {"url":link}

	headers = {
		"X-RapidAPI-Key": "ea656f7642msha8d4e40b7b4d44cp1d7a18jsnee198964c754",
		"X-RapidAPI-Host": "tiktok-downloader-download-tiktok-videos-without-watermark.p.rapidapi.com"
	}

	response = requests.request("GET", url, headers=headers, params=querystring)
	rest = json.loads(response.text)
	return {"Video":rest['video'][0],"Music":rest['music'][0]}