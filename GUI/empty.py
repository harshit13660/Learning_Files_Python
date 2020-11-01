from urllib.request import urlopen


def inter():
    try:
        urlopen('https://www.google.com',timeout=1)
        print("internet is working")

    except Exception as e:
        print("no internet")

inter()
