import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from gtts import gTTS
from playsound import playsound
import os
import random

chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(executable_path="./drivers/chromedriver_win32/chromedriver.exe",
                          options=chrome_options)


def generate_text():
    num = random.randint(1, 3)
    title = "Mad-Lib"
    if num == 1:
        url_text = "http://fucklorem.com/"
        driver.get(url_text)
        drp = Select(driver.find_element_by_tag_name("select"))
        drp.select_by_visible_text("1")
        text = driver.find_element_by_id("ta").text
        # html = requests.get(url_text)
        # soup = BeautifulSoup(html.content,'html.parser')
        # text = soup.find(name="textarea",class_="chisel_d normal", id="ta").text
        return [], num, title, text

    elif num == 2:
        url_text = "https://litipsum.com/api/4/json"
        result = requests.get(url_text).json()
        title = result["title"]
        print(title)
        mytext = result["text"]
        text = str(max(mytext, key=len)).replace(";", "")
        return [], num, title, text

    elif num == 3:
        url_text = "http://madlibz.herokuapp.com/api/random?minlength=5"
        result = requests.get(url_text).json()
        title = result["title"]
        fields = result["blanks"]
        text = result["value"]
        print(title)
        print(fields)
        print(text)
        return fields, num, title, text


def generate_madlib(text):
    url_madlib = "http://libberfy.herokuapp.com?blanks=10&q={}".format(text)
    madlib = str(requests.get(url_madlib).json()["madlib"])
    print(madlib)
    fields = []
    for x in madlib.split():
        if x.find('<') != -1:
            x = x.split(">", 1)[0]
            x = x.replace("<", "")
            x = x.replace(">", "")
            x = x.replace("_", " ")
            fields.append(x)
    print(fields)
    return fields, madlib


def generate_audio(message):
    language = 'en'
    filename = "Madlib.mp3"
    myObj = gTTS(text=str(message), lang=language)
    myObj.save(filename)
    return filename
