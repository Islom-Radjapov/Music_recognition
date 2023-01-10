import asyncio
from shazamio import Shazam
from find_url_youtube import get_url_in_youtube
from download_youtube import download

async def main(audio):
	shazam = Shazam()

	print(audio)
	out = await shazam.recognize_song(audio)
	# print(out)
	# print(out['track']['title'])      # music title
	# print(out['track']['subtitle'])   # music aftor
	# print(out['track']['url'])        # music url in shazam
	# print(out['track']['myshazam']['apple']['actions'][0]['uri'])  # music url in apple music
	# print(out['track']['sections'][1]['text'])  # music text
	# print(out['track']['hub']['actions'][1]['uri'])   # music downloads 30 seconds

	return out['track']['url']

# loop = asyncio.get_event_loop()
# loop.run_until_complete(main())

def start_audio(audio):
	loop = asyncio.get_event_loop()
	shazam_url = loop.run_until_complete(main(audio))
	print(shazam_url)
	youtube_url = get_url_in_youtube(shazam_url)
	print(youtube_url)
	mp3 = download(youtube_url)
	print(mp3)
	return mp3
