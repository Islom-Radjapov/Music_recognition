# # from lyricsgenius import Genius
# #
# # TOKEN = "yqM_E974dstosquBK6DvXV0IskRMTSWqZyB29IEwCsstgb86leOhOhUi2nl_ubhw"
# #
# # genius = Genius(TOKEN)
# # artist = genius.search_artist("Sevinch", max_songs=5, sort="title")
# #
# # print(artist.songs)
#
# import spotipy
# from spotipy.oauth2 import SpotifyClientCredentials
#
# spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials( client_id="43de88a1f18940f99278a42d028e4b78", client_secret="15b816a617d74f4eb3796e2a190d322b"))
#
# lz_uri = 'spotify:artist:36QJpDe2go2KgaRleHCDTp'
#
# # spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
# results = spotify.artist_top_tracks(lz_uri)
#
# for track in results['tracks'][:10]:
#     print('track    : ' + track['name'])
#     print('audio    : ' + track['preview_url'])
#     print('cover art: ' + track['album']['images'][0]['url'])
#     print()

for x in range(50, 0, -1):
    print(x)