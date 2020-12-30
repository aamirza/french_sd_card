from youtube_dl import YoutubeDL

YOUTUBE_PLAYLIST = "INSERT YOUTUBE PLAYLIST URL HERE"


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