import asyncio
from shazamio import Shazam
from find_url_youtube import get_url_in_youtube
from download_youtube import download
import os
import sqlite3


async def main(audio):
	shazam = Shazam()

	out = await shazam.recognize_song(audio)
	title = str(out['track']['title'])      # music title
	aftor = str(out['track']['subtitle'])   # music aftor
	# print(out['track']['url'])        # music url in shazam
	# print(out['track']['myshazam']['apple']['actions'][0]['uri'])  # music url in apple music
	text1 = out['track']['sections'][1]['text']  # music text
	# print(out['track']['hub']['actions'][1]['uri'])   # music downloads 30 seconds
	text = ""
	for x in text1:
		text += " " + x
	connection = sqlite3.connect("database.db")
	cursor = connection.cursor()
	# cursor.execute(f"INSERT INTO music VALUES ('{title}', '{aftor}', '{text}')")
	cursor.execute("INSERT INTO music (title, aftor, text) VALUES (?, ?, ?) ", (title, aftor, text))
	connection.commit()

	connection.close()
	if out['track']['url']:
		return out['track']['url']
	else:
		return None

def start_audio(audio):
	loop = asyncio.get_event_loop()
	shazam_url = loop.run_until_complete(main(audio))
	if shazam_url:
		print(shazam_url)
		youtube_url = get_url_in_youtube(shazam_url)
		print(youtube_url)
		mp3 = download(youtube_url)
		return mp3
	else:
		print("not find shazam")
		return None




start_audio(fr"voice\voice.ogg")

os.remove(fr"voice\voice.ogg")
print("Delete")
