import random

import spotipy
import spotipy.util as util
from moodmusic import authenticate_spotify, aggregate_top_artists, aggregate_top_tracks, select_tracks, create_playlist

client_id = "e1b138fd248d419bbcb11a2db7e2dd62"
client_secret = "2096188098364e368ee023312ff6d37d"
redirect_uri = "https://localhost:8888/callback/"

scope = 'user-library-read user-top-read playlist-modify-public user-follow-read'
username = "WhoaBot"


def createplaylist(mood):
    rand1 = random.randint(1,2)
    if rand1 == 1:
        token = util.prompt_for_user_token(username, scope, client_id, client_secret, redirect_uri)
        spotify_auth = authenticate_spotify(token)
        top_artists = aggregate_top_artists(spotify_auth)
        top_tracks = aggregate_top_tracks(spotify_auth, top_artists)
        selected_tracks = select_tracks(spotify_auth, top_tracks, mood)
        playlist_uri, playlist_url = create_playlist(spotify_auth, selected_tracks, mood)
        return playlist_url
    elif rand1 == 2:
        token = util.prompt_for_user_token(username, scope, client_id, client_secret, redirect_uri)
        spotify_auth = authenticate_spotify(token)
        myplaylists = spotify_auth.current_user_playlists()["items"]
        count = 0
        myplaylisturls = []
        for x in myplaylists:
            if x["name"].find("Whoabot's") == -1:
                count+=1
                myplaylisturls.append(x["external_urls"]["spotify"])
        rand2 = random.randint(0, count - 1)
        return myplaylisturls[rand2]
