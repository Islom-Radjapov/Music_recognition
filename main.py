import asyncio
from shazamio import Shazam


async def main():
	shazam = Shazam()
	out = await shazam.recognize_song('audio.ogg')
	# print(out)
	# print(out['track']['title'])      # music title
	# print(out['track']['subtitle'])   # music aftor
	# print(out['track']['url'])        # music url in shazam
	# print(out['track']['myshazam']['apple']['actions'][0]['uri'])  # music url in apple music
	# print(out['track']['sections'][1]['text'])  # music text
	# print(out['track']['hub']['actions'][1]['uri'])   # music downloads 30 seconds


loop = asyncio.get_event_loop()
loop.run_until_complete(main())

