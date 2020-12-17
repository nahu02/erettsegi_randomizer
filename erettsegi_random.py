import random
import json
import os
import requests
import webbrowser
import time

# pl. http://dload.oktatas.educatio.hu/erettsegi/feladatok_2020tavasz_kozep/k_magyir_20maj_fl.pdf
# ev = 2020 | evszak = tavasz | targy = kozep/k_magyir | ev2 = 20 | honap = maj

EV = [2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]
EVSZAK = ["osz", "tavasz"]
TARGY = ["kozep/k_magyir", "emelt/e_matang", "kozep/k_tort", "emelt/e_angol", "kozep/k_fiz", "emelt/e_inf"]
TARGY_alt = ["magyar", "matek", "töri", "angol", "fizika", "info"]


def random_website(targy=""):
    url = ""
    url2 = ""
    ev = random.choice(EV)
    evszak = random.choice(EVSZAK)
    
    if targy.lower() in TARGY_alt:
        targy = TARGY[TARGY_alt.index(targy.lower())]

    if targy not in TARGY: 
        targy = random.choice(TARGY)

    #angol emelt matek nincs ősszel
    while targy == "emelt/e_matang" and evszak == "osz":
        evszak = random.choice(EVSZAK)

    ev2 = str(ev)[-2:]

    honap = ""
    if evszak == "osz":
        honap = "okt"
    elif evszak == "tavasz":
        honap = "maj"

    url = f"http://dload.oktatas.educatio.hu/erettsegi/feladatok_{ev}{evszak}_{targy}_{ev2}{honap}_fl.pdf"

    if targy == "emelt/e_angol":
        url2 = f"http://dload.oktatas.educatio.hu/erettsegi/feladatok_{ev}{evszak}_{targy}_{ev2}{honap}_fl.mp3"
    elif targy == "emelt/e_inf":
        url2 = f"http://dload.oktatas.educatio.hu/erettsegi/feladatok_{ev}{evszak}_emelt/e_inffor_{ev2}{honap}_fl.zip"
    else:
        url2 = ""
    
    return (url, url2)
    
# Debug funkció random generált linkek működésének tesztelésére. raange: hány linket teszteljen le.
def test_links(raange):
    test_result = ""
    for i in range(raange):
        x = random_website()
        for z in x:
            if z != "":
                request = requests.get(z)
                if request.status_code != 200:
                    test_result += (f"\nProbléma! {z} nem megnyitható!")
                else:
                    test_result += (f"\n{z} működik.")

    test_result +=  ("\n\nTeszt kész.")
    return (test_result)

# A funkció, ami megnyitja a böngészőben a linket, ráadásul listát tart (history.json) a már megnyitott linkekről, hogy ugyanaz az oldal ne nyíljon meg többször.
def get_new_link(tantargy_input=""):
    x = random_website(tantargy_input)
    with open("history.json", "r") as f:
        history = json.load(f)

    while x[0] in history: #ha az x már volt használva (a history.json szerint), generál egy új x-et
        x = random_website(tantargy_input)
    
    history[x[0]] = time.asctime()

    with open("history.json", "w") as f:
        json.dump(history, f, indent=4)
    
    print (x)
    for i in reversed(x):
        if i != "":
            webbrowser.open(i, new=2)

if __name__ == '__main__':
    get_new_link(input(f"Ha van tantárgyi preferenciád, az alábbi listából beírhatod az egyiket (ha nincs, csak nyomj egy entert):\n {TARGY_alt}\n"))

