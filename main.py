from pytube import YouTube
from tkinter import *
from tkinter import filedialog
import directory

directory_object = directory.Directory()
idle_state = "Idle"

def begin_download():
    link = entry.get()
    try:
        youtube = YouTube(link)
        video = youtube.streams.get_highest_resolution()
        if directory_object.hasDirectory():
            video.download(output_path=directory_object.getDirectory())
        else:
            video.download()
    except:
        label = Label(root, text="The url isn't working")
        label.pack()

root = Tk()
root.title("Video downloader")
label_1 = Label(root, text="Youtube Video Downloader")
label_1.grid(row=0, column=1)

label_url = Label(root, text="Enter url:")
label_url.grid(row=1, column=0)

entry = Entry(root, width = 50)
entry.grid(row=1, column=1, columnspan=2, padx=20)

directory_button = Button(root, text="Directory", command=directory_object.setDirectory)
directory_button.grid(row=2, column=1)

download_button = Button(root, text="Download", command=begin_download)
download_button.grid(row=2, column=2)

root.mainloop()
