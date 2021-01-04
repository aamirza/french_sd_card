import os

from youtube_dl import YoutubeDL

YOUTUBE_PLAYLIST = "INSERT YOUTUBE PLAYLIST URL HERE"
DOWNLOAD_FOLDER = os.path.dirname(__file__) + '/downloads'



class InvalidPlaylistError(Exception):
    """For when a YouTube playlist URL is invalid"""
    pass


# Params for YouTubeDL

DEFAULT_PARAMS = {
    "forcejson": True,
    "nocheckcertificate": True,
    "outputdl": f"{str(DOWNLOAD_FOLDER)}/%(title)s.%(ext)s"
}

DOWNLOAD_AUDIO_PARAMS = dict(**DEFAULT_PARAMS, postprocessor=[
    {
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }
])

SIMULATE_DOWNLOAD_PARAMS = dict(**DEFAULT_PARAMS, simulate=True)


# Use YouTube-DL to get list of videos in playlist.

def get_playlist_videos_info(playlist):
    params = SIMULATE_DOWNLOAD_PARAMS
    with YoutubeDL(params) as ydl:
        info = ydl.extract_info(playlist, download=False)
    return info["entries"]


# Decide which videos you want to download, and which you want to leave,
# using indices.

def valid_link(url):
    return url.startswith('https://www.youtube.com/')


def valid_playlist_url(url):
    return url.startswith('https://www.youtube.com/playlist?list=')


def download_playlist(url, start_at_video=0, download_audio=True):
    if not valid_playlist_url(url):
        raise InvalidPlaylistError(f"Playlist URL is invalid: {url}")

    params = DOWNLOAD_AUDIO_PARAMS if download_audio else DEFAULT_PARAMS
    with YoutubeDL(params) as youtube_download:
        playlist_info = youtube_download.extract_info(url)
    return playlist_info
