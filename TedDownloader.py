import requests
from bs4 import BeautifulSoup

import re #regular expression pattern matching

import sys #argument parsing

if len(sys.argv) >1:
    url = sys.argv[1]
else:
    sys.exit("Error: please enter TED TALK url")

r= requests.get(url)
rcontent= r.content
print("Download about to start")

soup = BeautifulSoup(rcontent,features="lxml")

for val in soup.find_all("script"):
    if(re.search("pageProps",str(val))) is not None:
        result = str(val)

result_mp4= re.search("(?P<url>https?://[^\s]+)(mp4)",result).group("url")
mp4_url = result_mp4.split('"')[0]
mp4_url += "mp4"

print("Downloading video from ..." + mp4_url)

file_name = mp4_url.split("/")[len(mp4_url.split("/"))-1].split('?')[0]

print ("storing video in ... " +file_name)

r= requests.get(mp4_url)

with open(file_name, 'wb')as f:
    f.write(r.content)

print("Process finished")