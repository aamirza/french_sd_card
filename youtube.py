YOUTUBE_PLAYLIST = "INSERT YOUTUBE PLAYLIST URL HERE"


# Use YouTube-DL to get list of videos in playlist.

# Decide which videos you want to download, and which you want to leave.

def valid_link(playlist_url):
    return playlist_url.startswith('https://www.youtube.com/playlist?list=')
