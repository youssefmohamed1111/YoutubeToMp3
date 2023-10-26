from pytube import YouTube
import os
video = YouTube(str(input("Enter the Video's URL : ")))
print("Processing...\n")
mp3 = video.streams.filter(only_audio=True).first()
print("Enter Destination or leave blank for current directory \n")
destination =str(input(">> ")) or '.'
print("Downloading...\n")
output = mp3.download(output_path=destination)
base ,ext = os.path.splitext(output)
new_file = base +'.mp3'
os.rename(output,new_file)
print(video.title +"  has been downloaded")




