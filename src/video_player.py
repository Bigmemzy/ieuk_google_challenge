"""A video player class."""

from src.video_playlist import Playlist
from .video_library import VideoLibrary
from random import choice


class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()
        self._current_video = None
        self._pause = False
        self._list_of_playerlists = {}

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def format_video(self, video):
        return f"{video.title} ({video.video_id}) [{' '.join(video.tags)}]"

    def show_all_videos(self):
        """Returns all videos."""

        list_all_videos = self._video_library.get_all_videos()
        ordered_videos = []
        for video in list_all_videos:
            ordered_videos.append(self.format_video(video))
        
        ordered_videos.sort()
        print("Here's a list of all available videos:")
        for video in ordered_videos:
            print(f'\t {video}')
        
    
    def play_video(self, video_id):
        """Plays the respective video.

        Args:
            video_id: The video_id to be played.
        """
        
        new_video = self._video_library.get_video(video_id)
        if new_video:
            if self._current_video:
                print(f'Stopping video: {self._current_video.title}')
            self._current_video = new_video
            self._pause = False
            print(f'Playing video: {self._current_video.title}')
        else:
            print('Cannot play video: Video does not exist')
        

    def stop_video(self):
        """Stops the current video."""
        if self._current_video:
            print(f'Stopping video: {self._current_video.title}')
            self._current_video = None
        else:
            print('Cannot stop video: No video is currently playing')
        

    def play_random_video(self):
        """Plays a random video from the video library."""
        random_video = choice(self._video_library.get_all_videos())
        self.play_video(random_video.video_id)
        

    def pause_video(self):
        """Pauses the current video."""

        if self._current_video and self._pause != True:
            print(f'Pausing video: {self._current_video.title}')
            self._pause = True
        elif self._current_video and self._pause == True:
            print(f'Video already paused: {self._current_video.title}')
        else:
            print('Cannot pause video: No video is currently playing')

        

    def continue_video(self):
        """Resumes playing the current video."""

        if self._current_video and self._pause:
            print(f'Continuing video: {self._current_video.title}')
            self._pause = False
        elif self._current_video and self._pause != True:
            print(f'Cannot continue video: Video is not paused')
        else:
            print(f'Cannot continue video: No video is currently playing')        


    def show_playing(self):
        """Displays video currently playing."""
        if self._current_video:
            format_video = f'Currently playing: {self.format_video(self._current_video)}'
            if self._pause:
                print(format_video, '- PAUSED')
            else:
                print(format_video)
        else:
            print('No video is currently playing')
        

    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """

        if playlist_name.upper() not in self._list_of_playerlists:
            new_playlist = Playlist(playlist_name)
            self._list_of_playerlists[playlist_name.upper()] = new_playlist
            print(f'Successfully created new playlist: {playlist_name}')
        else:
            print('Cannot create playlist: A playlist with the same name already exists')


    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        if playlist_name.upper() not in self._list_of_playerlists:
            print(f'Cannot add video to {playlist_name}: Playlist does not exist')
            return None

        selected_playlist = self._list_of_playerlists[playlist_name.upper()]
        video = self._video_library.get_video(video_id)
        
        if video:
            selected_playlist.playlist_video = video
        else:
            print(f'Cannot add video to {playlist_name}: Video does not exist')

    def show_all_playlists(self):
        """Display all playlists."""

        print("show_all_playlists needs implementation")

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("show_playlist needs implementation")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        print("remove_from_playlist needs implementation")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("clears_playlist needs implementation")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("deletes_playlist needs implementation")

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        print("search_videos needs implementation")

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        print("search_videos_tag needs implementation")

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")
