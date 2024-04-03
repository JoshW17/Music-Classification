import customtkinter as ctk
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

class MusicPlayer:
    """GUI Media Player to allow user interface"""
    def __init__(self, master):
        super().__init__()
        self.master=master
        self.master.geometry("400x900")
        self.master.title("Music Player")
        
        # Create a frame to hold the widgets
        self.frame = ctk.CTkFrame(self.master)
        self.frame.pack(padx=20, pady=20)
        
        self.frame_top=ctk.CTkFrame(self.frame, height=40)
        self.frame_top.pack(side="top", expand=True, fill="x")
    
    def play_music(self):
        # Add your logic here to play the selected music file
        print("Playing music...")
    
if __name__ == "__main__":
    root=ctk.CTk()

    Player=PlayerBackend()
    PlayerBackend.play_song(Player, "./assets/Numb.mp3")

    # Song("./assets/Numb.mp3")
    
    # root.mainloop()
