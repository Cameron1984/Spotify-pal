import os
import spotipy
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyPKCE
import pprint

#loads the .env so things stored in there not explicitly loaded
load_dotenv()

#store ID and URI from env
CLIENT_ID = os.getenv("CLIENT_ID")
REDIRECT_URI = os.getenv("REDIRECT_URI")

#what we want permission to access
SCOPE = "user-read-currently-playing"

#sp is a client object used to ask spotify for things
sp = spotipy.Spotify(
    auth_manager=SpotifyPKCE( 
        client_id=CLIENT_ID,
        redirect_uri=REDIRECT_URI,
        scope=SCOPE,
    )
)

#Current is json. returns dict (current) of other dicts (item)
current = sp.current_user_playing_track()
#pprint.pp(current)

'''
if not current:
    print("Nothing currently playing")
else:
    mins_curr = current["progress_ms"] // 60000
    secs_curr = (current["progress_ms"] % 60000) // 1000
    mins_total = current["item"]["duration_ms"] // 60000
    secs_total = (current["item"]["duration_ms"] % 60000) // 1000

    print(current["item"]["name"]) 
    print(current["item"]["artists"][0]["name"]) 
    print(current["is_playing"])
    print(f"{mins_curr}:{secs_curr}/{mins_total}:{secs_total}")
    print(current["item"]["album"]["name"])
    print(current["item"]["album"]["images"][0]["url"])
'''

def display_song(current):
    print("─────────────────────────────────")
    if not current:
        print("Nothing currently playing")
    else:
        mins_curr = current["progress_ms"] // 60000
        secs_curr = (current["progress_ms"] % 60000) // 1000
        mins_total = current["item"]["duration_ms"] // 60000
        secs_total = (current["item"]["duration_ms"] % 60000) // 1000
        

        print("NOW PLAYING")
        print(current["item"]["name"]) 
        print(current["item"]["album"]["name"])
        print(current["item"]["artists"][0]["name"],"\n") 

        print(f"{mins_curr}:{secs_curr:02d}/{mins_total}:{secs_total:02d}")

    print("─────────────────────────────────")

display_song(current)