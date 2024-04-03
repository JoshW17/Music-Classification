import pickle
import os
from Song import Song

class SongData:
    def __init__(self, filename):
        self.storage={}
        self.filename=filename

    def load(self):
        with open(self.filename, 'rb') as file:
            self.storage=pickle.load(file)

    def write(self):
        with open(self.filename, 'wb') as file:
            pickle.dump(self.storage, file)

    def search(self, songname):
        return self.storage.get(songname, None)

    def add_song(self, filename, ImportData):
        basename=os.path.basename(filename)
        if basename not in self.storage.keys():
            self.storage[basename]=ImportData
            print(f"[LOG] -- Data added for {basename}")
            return True
        else:
            # print(f"[ERROR] -- {basename} already recorded")
            return False

    def check_song(self, filename):
        basename=os.path.basename(filename)
        print(f"[DEBUG] -- Basename: {basename}")
        print(f"[DEBUG] -- Keys: {self.storage.keys()}")
        if str(basename) in self.storage.keys():
            print("[DEBUG] -- Song found in dictionary.")
        else:
            print("[DEBUG] -- Song not found.")


class ComparisonData:
    def __init__(self, filename):
        self.storage=[[]]
        # Index 0 is Freq Data from FreqAnal.py
        self.filename=filename

    def load(self):
        with open(self.filename, 'rb') as file:
            self.storage=pickle.load(file)

    def write(self):
        with open(self.filename, 'wb') as file:
            pickle.dump(self.storage, file)

    def search(self, query):
        results=[]
        for entry in self.storage:
            if query in (entry[0], entry[1]):
                results.append(entry)
        return results            

    def add_freqdata(self, name1, name2, distance):
        if self.storage[0]:
            for entry in self.storage[0]:
                a=entry[0]
                b=entry[1]
                if name1 == a or name1 == b:
                    if name2 == a or name2 ==b:
                        # print(f"The entry for {name1} and {name2} already exists")
                        return False
        
        print(f"[LOG] -- Adding comparison data for {name1} and {name2}")
        self.storage[0].append([name1, name2, distance])
        return True
