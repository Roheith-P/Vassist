import ipaddress
import time
import webbrowser

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

i += 1
