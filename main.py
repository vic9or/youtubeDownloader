from pytube import YouTube

from sys import argv

link = argv[1]

youtube = YouTube(link)
video = youtube.streams.get_highest_resolution()
video.download()
