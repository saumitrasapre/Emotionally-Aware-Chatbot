import json
import random
import requests
import urllib.request
# from newsapi import NewsApiClient
from datetime import date


def fetchgif(query):
    API_KEY = "LXbY5N7DLj7jIWWhZoz3nw46KHEHTGGy"
    num = random.randint(1, 10)
    query = query.replace(" ", "+")
    url = "http://api.giphy.com/v1/gifs/search?q={}&api_key={}&offset={}&rating=pg&limit=10".format(query, API_KEY, num)
    data = json.loads(urllib.request.urlopen(url).read())
    # Gives Data, Pagination and Meta
    result = data["data"][0]["images"]["downsized"]["url"]
    print(result)
    return result


def fetchdatefact():
    """Get a random fact about current day and utter it as a response."""
    today = date.strftime(date.today(), '%m/%d')
    day_fact = requests.get(f'http://numbersapi.com/{today}/date')
    return day_fact.text


def fetchjoke():
    """Get a joke and utter it as a response."""
    num = random.randint(1, 2)
    if num == 1:
        joke = (requests.get('https://official-joke-api.appspot.com/random_joke')
                .json())
        joke_text = f"{joke['setup']} \n  {joke['punchline']}"

    elif num == 2:
        url = "https://icanhazdadjoke.com/"
        result = requests.get(url, headers={"Accept": "application/json"}).json()
        joke_text = result["joke"]

    return joke_text


def fetchfact():
    """Get a random fact and utter it as a response."""
    num = random.randint(1,4)
    if num == 1:
        fact = requests.get('https://uselessfacts.jsph.pl/random.json?language=en').json()["text"]
    elif num == 2:
        fact = requests.get('https://catfact.ninja/fact?max_length=140').json()["fact"]
    elif num == 3:
        fact_num = random.randint(0, 3)
        fact = requests.get('https://cat-fact.herokuapp.com/facts').json()[fact_num]["text"]
    elif num == 4:
        fact = requests.get('http://numbersapi.com/random/trivia').text
    return fact


# def fetchtrends():
#     # Init
#     newsapi = NewsApiClient(api_key='c968320fc3d441bea38bbccee80c3658')
#
#     # /v2/top-headlines
#     # top_headlines = newsapi.get_top_headlines(q='bitcoin',
#     #                                           category='business',
#     #                                           language='en',
#     #                                           country='us')
#     # print(top_headlines)
#
#     # /v2/everything
#     # all_articles = newsapi.get_everything(q='photography',
#     #                                       sources='bbc-news,the-verge',
#     #                                       domains='bbc.co.uk,techcrunch.com',
#     #                                       language='en',
#     #                                       sort_by='relevancy',
#     #                                       page=1)
#     # print(all_articles)
#
#     # print(result)
#     # /v2/sources
#     sources = newsapi.get_sources(language="en")
#     print(sources)


def fetchspotifyaccesstoken():
    file = open("creds.txt", "r+")
    token = file.readline()
    file.close()
    if token == "":
        result = requests.post("https://accounts.spotify.com/api/token", data=
        {"grant_type": "client_credentials", "client_id": "f96db491f72947628c928e1e43f3cc09",
         "client_secret": "eb6851c2ae894a17a1bbbbe687f1a8f3"},
                               headers={"Content-Type": "application/x-www-form-urlencoded"}).json()
        token = result["access_token"]
        open("creds.txt", "w").write(token)
        return token
    else:
        myresult = requests.get("https://api.spotify.com/v1/browse/new-releases?country=IN&limit=10",
                                headers={"Content-Type": "application/json",
                                         "Authorization": "Bearer {}".format(token)})
        code = myresult.status_code
        if code == 401:
            result = requests.post("https://accounts.spotify.com/api/token", data=
            {"grant_type": "client_credentials", "client_id": "f96db491f72947628c928e1e43f3cc09",
             "client_secret": "eb6851c2ae894a17a1bbbbe687f1a8f3"},
                                   headers={"Content-Type": "application/x-www-form-urlencoded"}).json()
            token = result["access_token"]
            open("creds.txt", "w").write(token)
            return token
        else:
            return token


def fetchmusic(num):
    key = fetchspotifyaccesstoken()
    if num == 1:
        # Gets a list a new releases
        mynum = random.randint(1, 10)
        myresult = requests.get("https://api.spotify.com/v1/browse/new-releases?country=IN&limit=10",
                                headers={"Content-Type": "application/json",
                                         "Authorization": "Bearer {}".format(key)})
        mylist = myresult.json()
        myalbum = mylist["albums"]["items"][mynum]
        mydict = {"album_type": myalbum["album_type"],
                  "artist_name": myalbum["artists"][0]["name"],
                  "album_name": myalbum["name"],
                  "url": myalbum["external_urls"]["spotify"]}
        return mydict

    if num == 2:
        # Gets a random track of a random genre
        mynum = random.randint(0, 9)
        mygenrenum = random.randint(0, 21)
        genre = ["acoustic", "ambient", "blues", "chill", "club", "dance", "disney", "disco", "drum-and-bass",
                 "dubstep", "edm",
                 "electro", "electronic", "rap", "guitar", "hip-hop", "indian", "jazz", "piano", "pop", "rock",
                 "work-out"
                 ]
        mygenre = genre[mygenrenum]
        print(mygenre)
        mylist = requests.get(
            "https://api.spotify.com/v1/search?q=genre%3A{}&type=track&market=IN&limit=10".format(mygenre),
            headers={"Accept": "application/json", "Content-Type": "application/json",
                     "Authorization": "Bearer {}".format(key)}).json()
        mytrack = mylist["tracks"]["items"][mynum]
        mydict = {"album_name": mytrack["album"]["name"],
                  "artist_name": mytrack["artists"][0]["name"],
                  "track_name": mytrack["name"],
                  "url": mytrack["external_urls"]["spotify"],
                  "genre": mygenre}
        return mydict


# if __name__ == "__main__":
    # fetchgif("@seizetheawkward mental health")
# fetchmusic(2)
# fetchtrends()
# fetchmusic(2)
# fetchdatefact()
# fetchjoke()
# fetchfact()
# today = date.strftime(date.today(),'%d %B')
# print(today)
