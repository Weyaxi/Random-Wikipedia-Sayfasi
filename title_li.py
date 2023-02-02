import requests
from bs4 import BeautifulSoup
import webbrowser
import warnings
import time

warnings.filterwarnings('ignore', '.*#ssl-warnings*',)
while True:
    try:
        URL="https://tr.wikipedia.org/wiki/Special:Random"
        html = requests.get(URL, verify=False).text.encode("utf-8")
        soup = BeautifulSoup(html, "html.parser")
        title = "".join(str(soup.title.text).split()[0:-2])
        secim = input(f"\nSeçilen makale: {title} \n Sayfa açılsın mı? ").lower()
        if secim == "e":
            webbrowser.open(f"https://tr.wikipedia.org/wiki/{title}")
            break
        elif secim == "h":
            continue
        else:
            print('Lütfen sadece evet için "e" hayır için "h" yazınız.')
            continue
    except AttributeError:
        time.sleep(5)
