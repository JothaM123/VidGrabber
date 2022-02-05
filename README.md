# VidGrabber
This is VidGrabber, the free YouTube downloader written in Python.

[Click here to download](https://github.com/JothaM123/VidGrabber/blob/main/VidGrabber.exe?raw=true)

# Source Code 
```python
from pytube import YouTube
from termcolor import cprint
from colorama import init

init()
print("""
▀█ █▀ ▀█▀  █▀▀▄ █▀▀▀ █▀▀█ █▀▀█ █▀▀▄ █▀▀▄ █▀▀ █▀▀█
 █▄█   █   █  █ █ ▀█ █▄▄▀ █▄▄█ █▀▀▄ █▀▀▄ █▀▀ █▄▄▀
  ▀   ▀▀▀  ▀▀▀  ▀▀▀▀ ▀ ▀▀ ▀  ▀ ▀▀▀  ▀▀▀  ▀▀▀ ▀ ▀▀
""")


while 1:
  link= input("🌐 Please Enter The Video URL ▶")
  vid = YouTube(link)

  video=vid.streams.get_highest_resolution()

  video.download()
  cprint("""
  ┌─────────────────────────────────────┐
  │                                     │
  │  Successfuly Downloaded The Video   │
  │                                     │
  └─────────────────────────────────────┘
  ""","green")
  input("⌨️ Please Press Enter To Download Another Video")



```
