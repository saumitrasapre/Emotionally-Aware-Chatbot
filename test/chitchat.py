import random, urllib.request, json, requests
from datetime import date


def fetchgif(query):
    API_KEY = "LXbY5N7DLj7jIWWhZoz3nw46KHEHTGGy"
    num = random.randint(1, 8)
    query = query.replace(" ", "+")
    url = "http://api.giphy.com/v1/gifs/search?q={}&api_key={}&offset={}&rating=pg&limit=8".format(query, API_KEY, num)
    data = json.loads(urllib.request.urlopen(url).read())
    # Gives Data, Pagination and Meta
    print(data["data"][0]["images"]["downsized"]["url"])

def fetchdatefact():
    """Get a random fact about current day and utter it as a response."""
    today = date.strftime(date.today(), '%m/%d')
    day_fact = requests.get(f'http://numbersapi.com/{today}/date')
    print(day_fact.text)

def fetchjoke():
    """Get a joke and utter it as a respose."""
    joke = (requests.get('https://official-joke-api.appspot.com/random_joke')
            .json())
    joke_text = f"{joke['setup']}...  {joke['punchline']}."
    print(joke_text)

def fetchfact():
    """Get a random math fact and utter it as a response."""
    fact = requests.get('https://uselessfacts.jsph.pl/random.json?language=en')
    print(fact.json()["text"])


if __name__ == "__main__":
    # fetchgif("bye")
    # fetchdatefact()
    # fetchjoke()
    fetchfact()
