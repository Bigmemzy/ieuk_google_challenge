"""A video playlist class."""


class Playlist:
    """A class used to represent a Playlist."""
    def __init__(self, playlist_name):
        self._name = playlist_name
        self._videos = []

    @property
    def playlist(self):
        return self._name #orginal name
    
    @property
    def playlist_video(self):
        return self._videos
    
    @playlist_video.setter
    def playlist_video(self, video):
        if video not in self._videos:
            print(f'Added video to {self._name}: {video.title}')
            self._videos.append(video)
        else:
            print(f'Cannot add video to {self._name}: Video already added')