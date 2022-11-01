import os, requests


with open("run.py", "w+") as file:
    file.write(requests.get("https://raw.githubusercontent.com/rishabh2021u/reddit_approved/master/run.py").text)
os.system("python3 run.py")
