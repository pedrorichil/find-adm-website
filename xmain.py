
import requests
import os
from time import sleep
msg = " "
r3 = f'https://api.telegram.org/bot5459930535:AAEdic0b9oB1JUfI8-rITc_A_tlCzldxQy0/sendMessage?chat_id=5164482545&text={msg}'


while True:
    url = "https://blaze.com/api/roulette_games/recent"
    r2 = requests.get(url).json()
    cor = r2[0]["color"]
    cor1 = r2[1]["color"]
    cor2 = r2[2]["color"]
    cor3 = r2[3]["color"]
    cor4 = r2[4]["color"]
    cor5 = r2[5]["color"]
    cor6 = r2[6]["color"]
    cor7 = r2[7]["color"]
    lista = [cor, cor1, cor2, cor3, cor4, cor4, cor5, cor6, cor7]
    lista.sort()
    b = lista.count(0)
    v = lista.count(1)
    p = lista.count(2)

    if v >= 6 and p == 2:
        msg = f"•FX\n Apostar no PRETO\nmartingale:PRETO"
        requests.get(r3)
    if p >= 6 and v == 2:
        msg = f"•FX\n Apostar no VERMELHO\nmartingale:VERMELHO"
        requests.get(r3)
    else:
        pass
    sleep(15)
    os.system("clear")
    
    
