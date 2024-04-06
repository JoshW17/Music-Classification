import customtkinter as ctk

class MusicPlayer:
    """GUI Media Player to allow user interface"""
    def __init__(self, master):
        self.master=master
        
        # Create a frame to hold the widgets 
        self.player_frame = ctk.CTkFrame(self.master, fg_color="#999999")
        self.player_frame.pack(side="left" ,padx=(10), pady=(10), ipady=(10), ipadx=(10),expand=True, fill="both")
        
        # The second smaller frame 
        self.frame_album_cover=ctk.CTkFrame(self.player_frame, fg_color="#5a4")
        self.frame_album_cover.pack(side="top", expand=True, fill="x", padx=(10))

        self.playlist_frame=ctk.CTkFrame(self.master, fg_color="#999999")
        self.playlist_frame.pack(side="right", padx=(10), pady=(10), ipady=(10), ipadx=(10), expand=True, fill="both")
    
    def play_music(self):
        # Add your logic here to play the selected music file
        print("Playing music...")
    
if __name__ == "__main__":
    root=ctk.CTk()
    root.geometry("1000x600")
    root.resizable(False, False)
    root.title("Music Player")

    GUI=MusicPlayer(root)

    root.mainloop()
