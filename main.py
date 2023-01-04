# import asyncio
# from shazamio import Shazam, Serialize
#
#
# async def main():
#   shazam = Shazam()
#   top_five_track_from_amsterdam = await shazam.top_country_tracks('NL', 5)
#   for track in top_five_track_from_amsterdam['tracks']:
#       serialized = Serialize.track(data=track)
#       print(serialized.title)
#
# loop = asyncio.get_event_loop()
# loop.run_until_complete(main())


import asyncio
from shazamio import Shazam, serializers, Serialize
import pandas as pd

async def main():
  shazam = Shazam()
  out = await shazam.recognize_song('diktafon.ogg')
  # serialized = Serialize.track(data=out)
  # for x, y in out.items():
  #   print(x, y)
  # print(out['track']['title'])      # music title
  # print(out['track']['subtitle'])   # music aftor
  # print(out['track']['href'])
  # print(serialized)
loop = asyncio.get_event_loop()
loop.run_until_complete(main())