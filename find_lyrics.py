
# environment variables (put into terminal)
''' 
export SPOTIPY_CLIENT_ID='OWN_PUBLIC_CLIENT_ID'
export SPOTIPY_CLIENT_SECRET='OWN_CLIENT_SECRET_ID'
export SPOTIPY_REDIRECT_URI='OWN_REDIRECT_URI'
export GENIUS_ACCESS_TOKEN='OWN_ACCESS_TOKEN'
'''

import os
import json
import lyricsgenius as lg
import spotipy as sp

# set environment variables
spotify_client_id = os.environ['SPOTIPY_CLIENT_ID']
spotify_secret = os.environ['SPOTIPY_CLIENT_SECRET']
spotify_redirect_uri = os.environ['SPOTIPY_REDIRECT_URI']
genius_access_token = os.environ['GENIUS_ACCESS_TOKEN']

scope = 'user-read-currently-playing'

# get token
oauth_object = sp.SpotifyOAuth(client_id=spotify_client_id,
                                    client_secret=spotify_secret,
                                    redirect_uri=spotify_redirect_uri,
                                    scope=scope)
print(oauth_object)

token_dict = oauth_object.get_access_token()
token = token_dict['access_token']

# create spotify object
spotify_object = sp.Spotify(auth=token)

# create genius object
genius_object = lg.Genius(genius_access_token)

current = spotify_object.currently_playing()
print(json.dumps(current, sort_keys=False, indent=4))

# find lyrics to song currently playing
current = spotify_object.currently_playing()
status = current['currently_playing_type']

artist_name = current['item']['album']['artists'][0]['name']
song_title = current['item']['name']

length = current['item']['duration_ms']
progress = current['progress_ms']
time_left = int((length-progress)/1000)

song = genius_object.search_song(title=song_title, artist=artist_name)
lyrics = song.lyrics
print(lyrics)

