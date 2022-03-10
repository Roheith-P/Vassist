import ipaddress
import time
import webbrowser
import requests
from bs4 import BeautifulSoup

print("Enter Your Commands")
i = 1
while i < 6:
    iput = input(">>>")
    if iput == "Hello":
        print("hi")
    elif iput == "about":
        f = open("ver.txt", "r")
        print(f.read())
    elif iput == "time":
        t = time.localtime()
        current_time = time.strftime("%H:%M:%S", t)
        print(current_time)
    elif iput == "openlink":
        url = input("Input Your Url:")
        webbrowser.open(url)
    elif iput == "weather":


        # enter city name
        city = "lucknow"

        # creating url and requests instance
        url = "https://www.google.com/search?q=" + "weather" + city
        html = requests.get(url).content

        # getting raw data
        soup = BeautifulSoup(html, 'html.parser')
        temp = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
        str = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text

        # formatting data
        data = str.split('\n')
        time = data[0]
        sky = data[1]

        # getting all div tag
        listdiv = soup.findAll('div', attrs={'class': 'BNeawe s3v9rd AP7Wnd'})
        strd = listdiv[5].text

        # getting other required data
        pos = strd.find('Wind')
        other_data = strd[pos:]

        # printing all data
        print("Temperature is", temp)
        print("Time: ", time)
        print("Sky Description: ", sky)
        print(other_data)
    elif iput == "help":
        print("Ask Anything If You Want To!")
i += 1
