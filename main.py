from Song import Song
import argparse


def main():

    # Parse Command Line Arguments
    parser=argparse.ArgumentParser(description="Compare the similarity of two songs.")
    parser.add_argument('FirstFile', type=str, help='First file to compare')
    parser.add_argument('SecondFile', type=str, help='Second file to compare')
    args=parser.parse_args()
    file1=args.FirstFile
    file2=args.SecondFile

    # Run Main Code
    print(f"\n[LOG] -- Processing File 1: {file1}\n")
    Song1=Song(file1)
    print(f"\n[LOG] -- Processing File 2: {file2}\n")
    Song2=Song(file2)


    print("\n[LOG] -- Completed Analysis\n")


if __name__ == "__main__":
    main()
