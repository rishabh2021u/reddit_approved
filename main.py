import praw, os, subprocess, time, requests, re, json, random

reddit1 = praw.Reddit(user_name='PdfFileOpener',refresh_token='2252389277312-ZCXJtfseArkexvPu2W0O7mfD4RVONw',client_id='U6nHuczXwm8okuLbFcs4Eg',client_secret='REHGpEGObR5C_sA_J-d8KQodKZNb8Q',redirect_uri='http://localhost:8080',user_agent='testscript by wwu/fakebot3',)


data=requests.get("https://gitlab.com/rishabh-modi2/public/-/raw/main/approved.json").json()


authors=[]
for contributor in reddit1.subreddit("Bharat_verse").contributor():
    authors.append(str(contributor))


for item in data:
    username=item["username"]
    if item["sub"] != "india" and username not in authors:
        reddit1.subreddit("Bharat_verse").contributor.add(username)
        print(username)
        authors.append(username)
        time.sleep(random.randint(90, 60))
  
