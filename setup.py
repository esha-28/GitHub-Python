import sys
from cx_Freeze import setup, Executable


setup(name='Youtube Downloader',version='1.0', description='download youtube video and convert desktop video to mp3', executables=[Executable("youtube_downloader.py",shortcutDir="DesktopFolder")])