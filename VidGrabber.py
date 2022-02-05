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


