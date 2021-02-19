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
TARGY = ["kozep/k_magyir", "emelt/e_matang", "kozep/k_tort",
         "emelt/e_angol", "kozep/k_fiz", "emelt/e_inf"]
TARGY_alt = ["magyar", "matek", "töri", "angol", "fizika", "info"]


def random_website(targy="", options=TARGY):
    url = ""
    url2 = ""
    ev = random.choice(EV)
    evszak = random.choice(EVSZAK)

    if targy.lower() in TARGY_alt:
        targy = TARGY[TARGY_alt.index(targy.lower())]

    if targy not in TARGY:
        try:
            targy = random.choice(options)
        except IndexError:
            raise IndexError(
                "Nincs választási opció, az 'options' lista üres.")

    # angol nyelvű tárgyak nincsenk ősszel (pl matek, fizika), de angol van
    while "ang" in targy and evszak == "osz":
        if "angol" in targy:
            break
        evszak = random.choice(EVSZAK)

    ev2 = str(ev)[-2:]

    honap = ""
    if evszak == "osz":
        honap = "okt"
    elif evszak == "tavasz":
        honap = "maj"

    url = f"http://dload.oktatas.educatio.hu/erettsegi/feladatok_{ev}{evszak}_{targy}_{ev2}{honap}_fl.pdf"

    if "angol" in targy:
        url2 = f"http://dload.oktatas.educatio.hu/erettsegi/feladatok_{ev}{evszak}_{targy}_{ev2}{honap}_fl.mp3"
    elif "inf" in targy:
        url2 = f"http://dload.oktatas.educatio.hu/erettsegi/feladatok_{ev}{evszak}_{targy}for_{ev2}{honap}_fl.zip"
    else:
        url2 = ""

    try:
        return (url, url2)
    finally:
        if not requests.get(url):
            raise ConnectionError(f"Valami nem jó. A {url} nem nyitható meg.")

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

    test_result += ("\n\nTeszt kész.")
    return (test_result)


def random_website_with_history_check(targy="", options=TARGY):
    x = random_website(targy, options)
    with open("history.json", "r") as f:
        history = json.load(f)

    # ha az x már volt használva (a history.json szerint), generál egy új x-et
    while x[0] in history:
        x = random_website(targy, options)

    return x


def add_website_to_history(websites):
    with open("history.json", "r") as f:
        history = json.load(f)

    history[websites[0]] = time.asctime()

    with open("history.json", "w") as f:
        json.dump(history, f, indent=4)


def open_websites(websites):
    print(f"Opening: {websites}")
    for i in reversed(websites):
        if i != "":
            webbrowser.open(i, new=2)

# A funkció, ami megnyitja a böngészőben a linket, ráadásul listát tart (history.json) a már megnyitott linkekről, hogy ugyanaz az oldal ne nyíljon meg többször.


def get_new_link(tantargy_input=""):
    x = random_website_with_history_check(tantargy_input)
    add_website_to_history(x)
    open_websites(x)


if __name__ == '__main__':
    get_new_link(input(
        f"Ha van tantárgyi preferenciád, az alábbi listából beírhatod az egyiket (ha nincs, csak nyomj egy entert):\n {TARGY_alt}\n"))
