import asyncio
from shazamio import Shazam, serializers, Serialize

async def main():
  shazam = Shazam()
  out = await shazam.recognize_song('audio.ogg')
  print(out['track']['title'])      # music title
  print(out['track']['subtitle'])   # music aftor
  print(out['track']['url'])        # music url in shazam
  print(out['track']['myshazam']['apple']['actions'][0]['uri'])  # music url in apple music

loop = asyncio.get_event_loop()
loop.run_until_complete(main())