import customtkinter as ctk
import pyglet

class Player():
    """Media player to handle MP3 files and audio output"""
    


class MusicPlayer():
    """GUI Media Player to allow user interface"""
    def __init__(self, master):
        super().__init__()
        self.master=master
        self.master.geometry("400x900")
        self.master.title("Music Player")
        
        # Create a frame to hold the widgets (Dan)
        self.frame = ctk.CTkFrame(self.master)
        self.frame.pack(padx=20, pady=20)
        
        self.frame_top=ctk.CTkFrame(self.frame, height=40)
        self.frame_top.pack(side="top", expand=True, fill="x")
    
    def play_music(self):
        # Add your logic here to play the selected music file
        print("Playing music...")
    
if __name__ == "__main__":
    root=ctk.CTk()

    MusicPlayer(root)

    root.mainloop()
