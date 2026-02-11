import os
import requests

URL = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
SAVE_PATH = "data/raw/titanic.csv"

os.makedirs("data/raw", exist_ok=True)

response = requests.get(URL)

with open(SAVE_PATH, "wb") as f:
    f.write(response.content)

print("Dataset downloaded successfully!")
