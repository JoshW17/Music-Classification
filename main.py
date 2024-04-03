from Data import ComparisonData, SongData
from Song import Song
import pandas as pd
import argparse
import math
import os
import sys


# === [ General Variables ] ===
SongFile="./SongData"
# Stores song names and characteristics as dictionary
# Key is audio file basename, value is array of data.
# Value Contents: [Array of polar coordinates for bin max]

CompFile="./CompData"
# Array of Arrays. Each Array contains 3 values.
# Values: (Song1, Song2, Distance)
# Distance represents the linear distance between two polar coordinates


def process_song(SongFile, SongDataObject, ComparisonDataObject):
    print(f"\n[LOG] -- Processing audio file: {SongFile}\n")

    if os.path.basename(SongFile) not in SongDataObject.storage.keys():
        SongInfo=Song(SongFile)
        Import=SongInfo.Freq.CharacteristicArray
    else:
        print(f"[STATUS] -- Song: {os.path.basename(SongFile)} already processed, skipping.")
        Import=SongDataObject.storage[os.path.basename(SongFile)]

    # Compare all existing songs to the newly added song.
    # Save results for later to avoid processing.
    for key, value in SongDataObject.storage.items():
        name1=os.path.basename(SongFile)
        PolarArray1=Import
        name2=key
        PolarArray2=value
        if name1 is not name2:
            Compare(name1, PolarArray1, name2, PolarArray2, ComparisonDataObject)
    
    Result=SongDataObject.add_song(SongFile, Import)
    SongDataObject.write()
    return Result

def Scan(directory, SongDataObject, ComparisonDataObject):
    for filename in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, filename)):
            if filename.endswith('.mp3'):
                # print(filename)
                full_file=os.path.join(directory, filename)
                if filename not in SongDataObject.storage.keys():
                    process_song(full_file, SongDataObject, ComparisonDataObject)
                else:
                    print(f"[STATUS] -- Song: {filename} already processed, skipping.")

def Compare(Name1, PolarArray1, Name2, PolarArray2, ComparisonDataObject):

    # === Compare Frequency Composition ===
    distance=[]
    # Convert Polar to Cartesian
    for polar1, polar2 in zip(PolarArray1, PolarArray2):
        mag1,phase1=polar1[0],polar1[1]
        mag2,phase2=polar2[0],polar2[1]
        x1=mag1*math.cos(math.radians(phase1))
        x2=mag2*math.cos(math.radians(phase2))
        y1=mag1*math.sin(math.radians(phase1))
        y2=mag2*math.sin(math.radians(phase2))
        d=math.sqrt((x2-x1)**2 + (y2-y1)**2)
        distance.append(d)
    distance=sum(distance)/len(distance)
    Result=ComparisonDataObject.add_freqdata(Name1, Name2, distance)
    ComparisonDataObject.write()

def SortRecommendations(Name, ComparisonDataObject):

    # === Data to Compare ===
    FreqData=ComparisonDataObject.storage[0]
    name=os.path.basename(Name)

    # === Form DataFrame ===
    df=pd.DataFrame(FreqData, columns=['Song1', 'Song2', 'Distance'])

    # === Sort and remove bad values ===
    df=df[ df['Song1'].str.contains(name) | df['Song2'].str.contains(name) ]
    # df.replace(name, pd.NA, inplace=True)
    df=df.sort_values(by='Distance', ascending=True)

    print(df)

def main():

    # === Load persistant storage ===
    SongDataStorage=SongData(SongFile)
    if os.path.exists(SongFile):
        SongDataStorage.load()
    ComparisonDataStorage=ComparisonData(CompFile)
    if os.path.exists(CompFile):
        ComparisonDataStorage.load()

    # === Parse Command Line Arguments ===
    parser=argparse.ArgumentParser(description="Compare the similarity of two songs.")
    parser.add_argument('-f', '--file', nargs=1, metavar='filename', help="Files to compare")
    parser.add_argument('-S', '--Scan', metavar='directory', help='Directory to scan for songs')
    parser.add_argument('-p', '--play', action='store_true', help='Play a playlist')
    args=parser.parse_args()

    # === Choose to create or load a playlist. Play that playlist. ===
    if args.play:
        print("PLAY THINGS")
        
    # === Scan directory with -S option ===
    if args.Scan:
        directory=args.Scan
        if os.path.isdir(directory):
            print(f"[LOG] -- Beginning scan: {directory}")
            try:
                Scan(directory, SongDataStorage, ComparisonDataStorage)
            except Exception as e:
                print(f"[ERROR] -- Error scanning directory: {e}")
            sys.exit()
        else:
            raise TypeError("Arguments passed to the '-S' option must be a directory")
    # Ensure that file argument is present
    if not args.file:
        parser.error("The '-f' option requires a file argument")

    process_song(args.file[0], SongDataStorage, ComparisonDataStorage)
    
    print("\n[LOG] -- Completed Analysis\n")

    SortRecommendations(args.file[0], ComparisonDataStorage)

if __name__ == "__main__":
    main()
