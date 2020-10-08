import random, urllib.request, json, requests
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
    print(day_fact.text)
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

    print(joke_text)
    return joke_text


def fetchfact():
    """Get a random fact and utter it as a response."""
    num = random.randint(1, 4)
    if num == 1:
        fact = requests.get('https://uselessfacts.jsph.pl/random.json?language=en').json()["text"]
    elif num == 2:
        fact = requests.get('https://catfact.ninja/fact?max_length=140').json()["fact"]
    elif num == 3:
        fact_num = random.randint(0, 3)
        fact = requests.get('https://cat-fact.herokuapp.com/facts').json()["all"][fact_num]["text"]
    elif num == 4:
        fact = requests.get('http://numbersapi.com/random/trivia').text
    print(fact)
    return fact


# if __name__ == "__main__":
    # fetchgif("cute cat")
    # fetchdatefact()
    # fetchjoke()
    # fetchfact()
    # today = date.strftime(date.today(),'%d %B')
    # print(today)
