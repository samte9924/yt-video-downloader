from pytubefix import YouTube
from pytubefix.cli import on_progress

location = "/Users/Samuel/Videos/Youtube Downloads"

yt = YouTube(str(input("Video URL to download: \n>")), on_progress_callback=on_progress)
vt = str(input("video or audio? \n>")).lower()

try:
    if vt == "video":
        video = yt.streams.get_highest_resolution()
        if video:
            video.download(output_path=location)
            print("Video downloaded")
        else:
            print("No video was found")
    elif vt == "audio":
        audio = yt.streams.filter(only_audio=True).first()
        if audio:
            audio.download(mp3=True, output_path=location)
            print("Audio downloaded")
        else:
            print("No audio was found")
    else:
        print("Error: Invalid type")
except Exception as e:
    print("Error while downloading: ", e)

print("Completed")
