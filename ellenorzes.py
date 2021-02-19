import json
import webbrowser

with open("history.json", "r") as f:
    history = json.load(f)


last = list(history.items())[len(history)-1]

url, time = last

url = f"{url[:-6]}ut.pdf"

webbrowser.open(url, new=2)
