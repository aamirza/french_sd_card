import os

from youtube_dl import YoutubeDL

YOUTUBE_PLAYLIST = "INSERT YOUTUBE PLAYLIST URL HERE"
DOWNLOAD_FOLDER = os.path.dirname(__file__) + '/downloads'



class InvalidPlaylistError(Exception):
    """For when a YouTube playlist URL is invalid"""
    pass


class YoutubeDownloader:
    @property
    def default_params(self):
        return {
            "forcejson": True,
            "nocheckcertificate": True,
            "outputdl": f"{str(DOWNLOAD_FOLDER)}/%(title)s.%(ext)s"
        }

    @property
    def download_audio_params(self):
        return dict(**self.default_params, postprocessor=[{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }])

    @property
    def simulate_download_params(self):
        return dict(**self.default_params, simulate=True)

    @staticmethod
    def valid_link(url):
        return url.startswith('https://www.youtube.com/')

    @staticmethod
    def valid_playlist(url):
        return url.startswith('https://www.youtube.com/playlist?list=')

    @staticmethod
    def validate_playlist(url):
        if not valid_playlist_url(url):
            raise InvalidPlaylistError(f"Playlist URL is invalid: {url}")

    @classmethod
    def get_playlist_videos_info(cls, playlist_url):
        cls.validate_playlist(playlist_url)

        with YoutubeDL(cls.simulate_download_params) as youtube_dl:
            info = youtube_dl.extract_info(playlist_url, download=False)
        return info["entries"]

    @classmethod
    def download_playlist(cls, url, download_audio=True):
        cls.validate_playlist(url)

        params = cls.download_audio_params if download_audio else cls.default_params
        with YoutubeDL(params) as youtube_dl:
            info = youtube_dl.extract_info(url)
        return info["entries"]

