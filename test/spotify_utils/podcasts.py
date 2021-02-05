import requests
import random
import spotipy
import spotipy.util as util

client_id = "f96db491f72947628c928e1e43f3cc09"
client_secret = "eb6851c2ae894a17a1bbbbe687f1a8f3"
redirect_uri = "https://localhost:8888/callback/"
username = "WhoaBot"
scope = 'user-library-read'


def get_podcasts(input_list):
    token = util.prompt_for_user_token(username=username,
                                       scope=scope,
                                       client_id=client_id,
                                       client_secret=client_secret,
                                       redirect_uri=redirect_uri)

    # enter term to search here
    # search_list = ['sleep stories']
    # search endpoint
    sp = spotipy.Spotify(auth=token)
    saved_podcasts = sp.current_user_saved_shows()
    endpoint_url = "https://api.spotify.com/v1/search?"
    # PERFORM THE QUERY
    id_list = []
    name_list = []
    desc_list = []
    publisher_list = []
    languages_list = []
    urls_list = []
    type_ = 'show'
    market = 'US'
    limit = 30
    for p in range(len(saved_podcasts['items'])):
        id_list.append(saved_podcasts['items'][p]['show']['id'])
        name_list.append(saved_podcasts['items'][p]['show']['name'])
        desc_list.append(saved_podcasts['items'][p]['show']['description'])
        publisher_list.append(saved_podcasts['items'][p]['show']['publisher'])
        languages_list.append(saved_podcasts['items'][p]['show']['languages'])
        urls_list.append(saved_podcasts['items'][p]['show']['external_urls']['spotify'])

    for i in range(len(input_list)):
        search = input_list[i]
        print(search)
        query = f'{endpoint_url}'
        query += f'&q={search}'
        query += f'&type={type_}'
        query += f'&market={market}'
        query += f'&limit={limit}'
        response = requests.get(query, headers={"Content-Type": "application/json", "Authorization": f"Bearer {token}"})
        json_response = response.json()
        for j in range(len(json_response['shows']['items'])):
            if json_response['shows']['items'][j] is not None:
                if json_response['shows']['items'][j]['languages'][0] == 'en' or \
                        json_response['shows']['items'][j]['languages'][0] == 'en-US' or \
                        json_response['shows']['items'][j]['languages'][0] == 'en-GB':
                    id_list.append(json_response['shows']['items'][j]['id'])
                    name_list.append(json_response['shows']['items'][j]['name'])
                    desc_list.append(json_response['shows']['items'][j]['description'])
                    publisher_list.append(json_response['shows']['items'][j]['publisher'])
                    languages_list.append(json_response['shows']['items'][j]['languages'])
                    urls_list.append(json_response['shows']['items'][j]['external_urls']['spotify'])

    num = random.randint(0, len(name_list))  ## default limit of query is 20
    print(num)
    name = name_list[num]
    description = desc_list[num]
    publisher = publisher_list[num]
    podcast_url = urls_list[num]
    return name, description, publisher, podcast_url


if __name__ == "__main__":
    name, publisher, description, podcast_url = get_podcasts(['sleep stories', 'bedtime stories'])
    print(name)
    print(publisher)
    print(description)
    print(podcast_url)
