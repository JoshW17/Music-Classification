import customtkinter as ctk

class MusicPlayer:
    """GUI Media Player to allow user interface"""
    def __init__(self, master):
        self.master=master
        
        # Create a frame to hold the widgets 
        self.frame = ctk.CTkFrame(self.master)
        self.frame.pack(padx=(0,1400), pady=(500,0))
        
        # The second smaller frame 
        self.frame_top=ctk.CTkFrame(self.frame, fg_color="#999999",width=500,height=1500)
        self.frame_top.pack(side="top", expand=True, fill="x")
    
    def play_music(self):
        # Add your logic here to play the selected music file
        print("Playing music...")
    
if __name__ == "__main__":
    root=ctk.CTk()
    root.geometry("400x900")
    root.title("Music Player")   


    
    # root.mainloop()
