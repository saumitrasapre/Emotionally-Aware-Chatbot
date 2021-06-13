import random
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth
from spotify_utils.moodmusic import authenticate_spotify, aggregate_top_artists, aggregate_top_tracks, select_tracks, \
    create_playlist

client_id = "f96db491f72947628c928e1e43f3cc09"
client_secret = "eb6851c2ae894a17a1bbbbe687f1a8f3"
redirect_uri = "https://localhost:8888/callback/"

scope = 'user-library-read user-top-read playlist-modify-public user-follow-read'
username = "WhoaBot"


def createplaylist(mood):
    rand1 = random.randint(1, 2)
    if rand1 == 1:
        spotify_auth = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri,scope=scope,username=username))
        # token = util.prompt_for_user_token(username, scope, client_id, client_secret, redirect_uri)
        # spotify_auth = authenticate_spotify(token)
        top_artists = aggregate_top_artists(spotify_auth)
        top_tracks = aggregate_top_tracks(spotify_auth, top_artists)
        selected_tracks = select_tracks(spotify_auth, top_tracks, mood)
        playlist_uri, playlist_url = create_playlist(spotify_auth, selected_tracks, mood)
        return playlist_url
    elif rand1 == 2:
        # token = util.prompt_for_user_token(username, scope, client_id, client_secret, redirect_uri)
        # spotify_auth = authenticate_spotify(token)
        spotify_auth = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri,scope=scope,username=username))
        myplaylists = spotify_auth.current_user_playlists()["items"]
        count = 0
        myplaylisturls = []
        for x in myplaylists:
            if x["name"].find("Eric's") == -1:
                count += 1
                myplaylisturls.append(x["external_urls"]["spotify"])
        rand2 = random.randint(0, count - 1)
        print(myplaylisturls[rand2])
        return myplaylisturls[rand2]


# if __name__ == "__main__":
#     createplaylist(0.5)
