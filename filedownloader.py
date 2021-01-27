import requests
from bs4 import BeautifulSoup as bs
import urllib
import os

print("Enter website URL : ")
url = input()
r = requests.get(url)
if r.status_code != 200:
    print("Error! Cannot access website")
else:
    soup = bs(r.text, features = "lxml")
    linkarr = soup.select('a')
    files = []
    filenames = []
    for i, link in enumerate(soup.find_all('a')):
        file_url = link.get('href')
        if file_url is not None:
            if file_url.endswith('.pdf'):
                files.append(file_url)
                filenames.append(linkarr[i].attrs['href'])

    names_urls = zip(filenames, files)
    print("Enter folder name to save to : ")
    folder = input()
    if not os.path.exists(folder):
        os.makedirs(folder)

    for name, url in names_urls:
        print(url)
        res = urllib.request.urlopen(url)
        filename = name.split("/")
        pdf = open(os.path.join(folder, filename[len(filename) - 1]), 'wb')
        pdf.write(res.read())
        pdf.close()

    print("Downloaded all files from given website!!")


