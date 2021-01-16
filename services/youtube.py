"""
The Youtube class is a "Downloader" (downloader.py) for downloading all the
audio in a Youtube playlist.
"""

from youtube_dl import YoutubeDL

from services.downloader import Downloader


class InvalidPlaylistError(Exception):
    """For when a YouTube playlist URL is invalid"""
    pass


def raise_error_if_invalid_playlist(func):
    """Wrapper function for validating a playlist URL. URL should be the first
    argument passed to the function."""
    def wrapper_raise_error_when_invalid_playlist(self, *args, **kwargs):
        # URL should be the first argument passed.
        url = args[0]
        if not YoutubeDownloader.valid_playlist(url):
            raise InvalidPlaylistError(f"Playlist URL is invalid: {url}")
        value = func(self, *args, **kwargs)
        return value
    return wrapper_raise_error_when_invalid_playlist


class YoutubeDownloader(Downloader):
    def __init__(self, download_folder=None, url=None):
        super().__init__(download_folder, url)

    def download(self, start_at_position=1):
        return self.download_playlist(self.url,
                                      start_at_video=start_at_position)

    def get_info(self):
        return self.get_playlist_videos_info(self.url)

    @property
    def default_params(self):
        """"Params for YoutubeDL"""
        return {"forcejson": True, "nocheckcertificate": True,
                "outputdl": f"{self.download_folder}/%(title)s.%(ext)s"}

    @property
    def simulate_download_params(self):
        """"Params for YoutubeDL"""
        return dict(**self.default_params, simulate=True)

    @property
    def download_audio_params(self):
        """"Params for YoutubeDL"""
        return dict(**self.default_params,
                    postprocessors=[{'key': 'FFmpegExtractAudio',
                                     'preferredcodec': 'mp3',
                                     'preferredquality': '192',}]
                    )

    @staticmethod
    def valid_link(url):
        """Checks for valid Youtube URL"""
        return url.startswith('https://www.youtube.com/')

    @staticmethod
    def valid_playlist(url):
        """Checks for valid Youtube playlist URL"""
        return url.startswith('https://www.youtube.com/playlist?list=')

    @raise_error_if_invalid_playlist
    def get_playlist_videos_info(self, playlist_url):
        """Return information about each video in the playlist."""
        with YoutubeDL(self.default_params) as youtube_dl:
            info = youtube_dl.extract_info(playlist_url, download=False)
        return info["entries"]

    @raise_error_if_invalid_playlist
    def download_playlist(self, url, start_at_video=1, download_audio=True):
        """Download all the videos (audio) of a Youtube playlist"""
        params = self.download_audio_params if download_audio else self.default_params
        if start_at_video > 1:
            params = dict(**params, playliststart = start_at_video)

        with YoutubeDL(params) as youtube:
            playlist_info = youtube.extract_info(url)

        number_of_videos_downloaded = len(playlist_info["entries"])
        return number_of_videos_downloaded



