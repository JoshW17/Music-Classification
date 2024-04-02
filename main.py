from Song import Song
import argparse


def compare_songs(song1: list[float], song2: list[float]) -> float:
    """Compares 2 songs. The first input is the reference. Output is a decimal percentage representation of how similar song2 is to song1."""
    diffs=[abs(x1-x2)/max(x1,x2) for x1,x2 in zip(song1, song2)]
    avgs=sum(diffs)/len(diffs)
    similarity=1-avgs
    return similarity


def main():

    # Parse Command Line Arguments
    parser=argparse.ArgumentParser(description="Compare the similarity of two songs.")
    parser.add_argument('FirstFile', type=str, help='First file to compare')
    parser.add_argument('SecondFile', type=str, help='Second file to compare')
    args=parser.parse_args()
    file1=args.FirstFile
    file2=args.SecondFile

    # Run Main Code
    # I am assuming that Song1 in this case is the "Reference" song
    # This means that, for later stages of our code, Song1 will be what we look for in other songs.
    # This is relevant for the 'compare_songs' method above
    print(f"\n[LOG] -- Processing File 1: {file1}\n")
    Song1=Song(file1)
    print(f"\n[LOG] -- Processing File 2: {file2}\n")
    Song2=Song(file2)


    Fingerprint1=Song1.Freq.fingerprint_tag
    Fingerprint2=Song2.Freq.fingerprint_tag

    similarity=compare_songs(Fingerprint1, Fingerprint2)

    print("\n[LOG] -- Completed Analysis\n")

    print(f"[RESULT] -- {Song1.filename} and {Song2.filename} are {similarity*100}% similar")


if __name__ == "__main__":
    main()
