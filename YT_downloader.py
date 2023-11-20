from pytube import YouTube
from sys import argv

link = argv[1]
yt = YouTube(link)

print("Title: ", yt.title)
print("Author: ", yt.author)
print ("Views: ", yt.views)
print("Usage: python YT_downloader.py 'https://www.youtube.com/'")

yd = yt.streams.get_highest_resolution()

yd.download(r'\Users\arnas\Downloads')
