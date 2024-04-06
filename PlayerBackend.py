import vlc
import time

class PlayerBackend:
    def __init__(self):
        self.instance=vlc.Instance()
        self.player=self.instance.media_player_new()
        self.playlist_player=vlc.MediaListPlayer()

    def play_song(self, file):
        media=self.instance.media_new(file)
        self.player.set_media(media)
        self.player.play()
        self.persist_song()

    def persist_song(self):
        """Necessary until GUI is implemented, to ensure the program doesn't exit before the song ends"""
        state=self.player.get_state()
        while state != vlc.State.Ended:
            state=self.player.get_state()
            time.sleep(1)

    def persist_playlist(self):
        """ ALso necessary until GUI"""
        state=self.playlist_player.get_state()
        while state != vlc.State.Ended:
            state=self.playlist_player.get_state()
            time.sleep(1)

    def play(self):
        self.player.play()

    def play_playlist(self):
        self.playlist_player.play()

    def pause(self):
        self.player.pause()

    def pause_playlist(self):
        self.playlist_player.pause()

    def stop(self):
        self.player.stop()

    def stop_playlist(self):
        self.playlist_player.stop()

    def get_position(self):
        return self.player.get_time()

    def get_playlist_position(self):
        return self.playlist_player.get_time()

    def load_playlist(self, playlist:list[str]):
        media_list=self.instance.media_list_new()
        for song in playlist:
            media=self.instance.media_new(song)
            media_list.add_media(media)
        self.playlist_player.set_media_list(media_list)
