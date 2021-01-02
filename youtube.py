import os

from youtube_dl import YoutubeDL

YOUTUBE_PLAYLIST = "INSERT YOUTUBE PLAYLIST URL HERE"
DOWNLOAD_FOLDER = os.path.dirname(__file__) + '/downloads'


class InvalidPlaylistError(Exception):
    """For when a YouTube playlist URL is invalid"""
    pass


# Use YouTube-DL to get list of videos in playlist.

def get_playlist_videos_info(playlist):
    params = {"simulate": True, "forcejson": True, "nocheckcertificate": True}
    with YoutubeDL(params) as ydl:
        info = ydl.extract_info(playlist, download=False)
    return info["entries"]

# Decide which videos you want to download, and which you want to leave,
# using indices.

def valid_link(url):
    return url.startswith('https://www.youtube.com/')


def valid_playlist_url(url):
    return url.startswith('https://www.youtube.com/playlist?list=')


def download_playlist(url):
    if not valid_playlist_url(url):
        raise InvalidPlaylistError(f"Playlist URL is invalid: {url}")
