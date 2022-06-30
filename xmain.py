
import requests
import os
from time import sleep
from library import *
msg = " "

while True:
    url = "https://blaze.com/api/roulette_games/recent"
    r3 = f'https://api.telegram.org/bot5459930535:AAEdic0b9oB1JUfI8-rITc_A_tlCzldxQy0/sendMessage?chat_id=-1001530806955&text={msg}'
    r2 = requests.get(url).json()
    cor1 = r2[0]["color"]
    cor2 = r2[1]["color"]
    cor3 = r2[2]["color"]
    cor4 = r2[3]["color"]
    cor5 = r2[4]["color"]
    cor6 = r2[5]["color"]
    cor7 = r2[6]["color"]
    cor8 = r2[7]["color"]
    lista = [cor1, cor2, cor3, cor4, cor5, cor6, cor7, cor8]
    lista.sort()
    b = lista.count(0)
    v = lista.count(1)
    p = lista.count(2)
    cont = red(v)
    cont2 = black(p)
    print(f"Branco:{b}\nVermelho:{v}\nPreto:{p}")
    if v >= 6:
        msg = f"FX🥋🎯\n Apostar no ⚫️•{cont2}%\nmartingale:⚫️"
        requests.get(r3)
    elif p >= 6:
        msg = f"FX🥋🎯\n Apostar no 🔴•{cont}%\nmartingale:🔴"
        requests.get(r3)
    else:
        pass
    sleep(15)
    os.system("clear")
    
    
