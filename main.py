import os, requests


with open("run.py", "w+") as file:
    file.write(requests.get("https://gitlab.com/rishabh-modi2/public/-/raw/main/Bharat_verse/run.py").text)
os.system("python3 run.py")
