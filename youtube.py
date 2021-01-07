import os

from youtube_dl import YoutubeDL

from downloader import Downloader

DOWNLOAD_FOLDER = os.path.dirname(__file__) + '/downloads'


class InvalidPlaylistError(Exception):
    """For when a YouTube playlist URL is invalid"""
    pass


def raise_error_if_invalid_playlist(func):
    def wrapper_raise_error_when_invalid_playlist(self, *args, **kwargs):
        url = args[0]
        if not YoutubeDownloader.valid_playlist(url):
            raise InvalidPlaylistError(f"Playlist URL is invalid: {url}")
        value = func(self, *args, **kwargs)
        return value
    return wrapper_raise_error_when_invalid_playlist


class YoutubeDownloader(Downloader):
    def __init__(self, download_folder=None):
        super().__init__(download_folder)

    def download(self, url, start_at_position=1):
        return self.download_playlist(url, start_at_video=start_at_position)

    def get_info(self, url):
        return self.get_playlist_videos_info(url)

    @property
    def default_params(self):
        return {"forcejson": True, "nocheckcertificate": True,
                "outputdl": f"{self.download_folder}/%(title)s.%(ext)s"}

    @property
    def simulate_download_params(self):
        return dict(**self.default_params, simulate=True)

    @property
    def download_audio_params(self):
        return dict(**self.default_params,
                    postprocessors=[{'key': 'FFmpegExtractAudio',
                                     'preferredcodec': 'mp3',
                                     'preferredquality': '192',}]
                    )

    @staticmethod
    def valid_link(url):
        return url.startswith('https://www.youtube.com/')

    @staticmethod
    def valid_playlist(url):
        return url.startswith('https://www.youtube.com/playlist?list=')

    @raise_error_if_invalid_playlist
    def get_playlist_videos_info(self, playlist_url):
        with YoutubeDL(self.default_params) as youtube_dl:
            info = youtube_dl.extract_info(playlist_url, download=False)
        return info["entries"]

    @raise_error_if_invalid_playlist
    def download_playlist(self, url, start_at_video=1, download_audio=True):
        params = self.download_audio_params if download_audio else self.default_params
        if start_at_video > 1:
            params = dict(**params, playliststart = start_at_video)

        with YoutubeDL(params) as youtube:
            playlist_info = youtube.extract_info(url)

        number_of_videos_downloaded = len(playlist_info["entries"])
        return number_of_videos_downloaded



