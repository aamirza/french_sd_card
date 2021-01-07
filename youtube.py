import os

from youtube_dl import YoutubeDL

from downloader import Downloader

DOWNLOAD_FOLDER = os.path.dirname(__file__) + '/downloads'


class InvalidPlaylistError(Exception):
    """For when a YouTube playlist URL is invalid"""
    pass


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

    @classmethod
    def validate_playlist(cls, url):
        if not cls.valid_playlist(url):
            raise InvalidPlaylistError(f"Playlist URL is invalid: {url}")

    def get_playlist_videos_info(self, playlist_url):
        self.validate_playlist(playlist_url)

        with YoutubeDL(self.default_params) as youtube_dl:
            info = youtube_dl.extract_info(playlist_url, download=False)
        return info["entries"]

    def download_playlist(self, url, start_at_video=1, download_audio=True):
        self.validate_playlist(url)

        params = self.download_audio_params if download_audio else self.default_params
        if start_at_video > 1:
            params = dict(**params, playliststart = start_at_video)

        with YoutubeDL(params) as youtube_dl:
            info = youtube_dl.extract_info(url)
        return info["entries"]



