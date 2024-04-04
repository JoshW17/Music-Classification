import vlc
import time

class PlayerBackend:
    def __init__(self):
        self.instance=vlc.Instance()
        self.player=self.instance.media_player_new()

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

    def play(self):
        self.player.play()

    def pause(self):
        self.player.pause()

    def stop(self):
        self.player.stop()

    def get_position(self):
        return self.player.get_time()

    def load_playlist(self, playlist):
        media_list=self.instance.media_list_new()
        for song in playlist:
            media=self.instance.media_new(song)
            media_list.add_media(media)
        self.player.set_media_list(media_list)
