import customtkinter as ctk
import tkinter as tk
from tkinter import ttk

class MusicPlayer:
    """GUI Media Player to allow user interface"""
    def __init__(self, master):
        self.master=master
        
        # Create a frame to hold the widgets 
        self.player_frame = ctk.CTkFrame(self.master, fg_color="#999999")
        self.player_frame.pack(side="left" ,padx=(10), pady=(10), ipady=(10), ipadx=(10),expand=True, fill="both")
        
        # The title of the music player 
        label = ctk.CTkLabel(self.player_frame, text="Music Player", text_color='black')
        label.pack(padx=0,pady=0)

        # The frame to hold the album cover 
        self.frame_album_cover=ctk.CTkFrame(self.player_frame, fg_color="#5a4", width=300, height=300)
        self.frame_album_cover.pack(side="top", fill="x",padx=(10))

        # The frame to hold the playlist 
        self.playlist_frame=ctk.CTkFrame(self.master, fg_color="#999999")
        self.playlist_frame.pack(side="right", padx=(10), pady=(10), ipady=(10), ipadx=(10), expand=True, fill="both")

        # The title of the playlist
        label = ctk.CTkLabel(self.playlist_frame, text="Recommended Songs", text_color='black')
        label.pack(padx=0,pady=0)

        # The grid for the playlist songs 
        playlist = ttk.Treeview(self.playlist_frame, columns=('Song', 'Artist'), show='headings')
        playlist.heading('Song', text='Song')
        playlist.heading('Artist', text='Artist')
        data = [('I Want It That Way', 'Backstreet Boys'), ('Never Gonna Give You Up', 'Rick Astley'), ('All Star', 'Smash Mouth')]
        for Song, Artist in data:
            playlist.insert('', tk.END, values=(Song, Artist))
        playlist.pack(expand=True, fill='both')

        # Scrollbar for the playlist
        # tree=ttk.Treeview(playlist)
        # scrollbar = ttk.Scrollbar(playlist, orient='vertical', command=tree.yview)
        # tree.configure(yscrollcommand=scrollbar.set)
        # tree.pack(side='left', fill='both', expand=True)
        # scrollbar.pack(side='right', fill='y')

        # Button Frame
        self.button_frame=ctk.CTkFrame(self.player_frame)
        self.button_frame.pack(side="top", fill="x", expand=True)
        
        # Forward button
        forward = ctk.CTkButton(master=self.button_frame, text=" ---> ")
        forward.pack(padx=20, pady=10, side="left")
        # Pause button
        pause = ctk.CTkButton(master=self.button_frame, text=" | | ")
        pause.pack(padx=20, pady=10, side="left")
        # Back button 
        back = ctk.CTkButton(master=self.button_frame, text=" <--- ")
        back.pack(padx=20, pady=10, side="left")
        
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
