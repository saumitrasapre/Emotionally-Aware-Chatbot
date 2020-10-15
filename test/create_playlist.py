import random

import spotipy.util as util
from moodmusic import authenticate_spotify, aggregate_top_artists, aggregate_top_tracks, select_tracks, create_playlist

client_id = "client_id"
client_secret = "client_secret"
redirect_uri = "https://localhost:8888/callback/"

scope = 'user-library-read user-top-read playlist-modify-public user-follow-read'

username = "WhoaBot"


def createplaylist():
    token = util.prompt_for_user_token(username, scope, client_id, client_secret, redirect_uri)
    mood = float("{:.2f}".format(random.uniform(0.0, 1.0)))
    spotify_auth = authenticate_spotify(token)
    top_artists = aggregate_top_artists(spotify_auth)
    top_tracks = aggregate_top_tracks(spotify_auth, top_artists)
    selected_tracks = select_tracks(spotify_auth, top_tracks, mood)
    playlist_uri, playlist_url = create_playlist(spotify_auth, selected_tracks, mood)
    return playlist_url
