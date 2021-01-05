import os

from youtube_dl import YoutubeDL

YOUTUBE_PLAYLIST = "INSERT YOUTUBE PLAYLIST URL HERE"
DOWNLOAD_FOLDER = os.path.dirname(__file__) + '/downloads'



class InvalidPlaylistError(Exception):
    """For when a YouTube playlist URL is invalid"""
    pass


class YoutubeDownloader:
    DEFAULT_PARAMS = {"forcejson": True, "nocheckcertificate": True,
                      "outputdl": f"{str(DOWNLOAD_FOLDER)}/%(title)s.%(ext)s"}
    DOWNLOAD_AUDIO_PARAMS = dict(**DEFAULT_PARAMS,
                                 postprocessors=[{'key': 'FFmpegExtractAudio',
                                                  'preferredcodec': 'mp3',
                                                  'preferredquality': '192',}]
                                 )
    SIMULATE_DOWNLOAD_PARAMS = dict(**DEFAULT_PARAMS, simulate=True)

    @staticmethod
    def valid_link(url):
        return url.startswith('https://www.youtube.com/')

    @staticmethod
    def valid_playlist(url):
        return url.startswith('https://www.youtube.com/playlist?list=')

    @classmethod
    def validate_playlist(cls, url):
        if not cls.valid_playlist(url):
            raise InvalidPlaylistError(f"Playlist URL is invalid: {url}")

    @classmethod
    def get_playlist_videos_info(cls, playlist_url):
        cls.validate_playlist(playlist_url)

        with YoutubeDL(cls.DOWNLOAD_AUDIO_PARAMS) as youtube_dl:
            info = youtube_dl.extract_info(playlist_url, download=False)
        return info["entries"]

    @classmethod
    def download_playlist(cls, url, download_audio=True):
        cls.validate_playlist(url)

        params = cls.DOWNLOAD_AUDIO_PARAMS if download_audio else cls.DEFAULT_PARAMS
        with YoutubeDL(params) as youtube_dl:
            info = youtube_dl.extract_info(url)
        return info["entries"]

