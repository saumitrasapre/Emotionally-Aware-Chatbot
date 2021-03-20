import requests

API_ENDPOINT = "http://15edc48cb096.ngrok.io"


def get_nmt_response(question):
    data = {'question': str(question)}
    r = requests.post(url=API_ENDPOINT, data=data)
    print(r.text)
    return r.text
