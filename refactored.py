import soundfile as sf
import argparse
import numpy as np
import matplotlib.pyplot as plt

def input():
    parser=argparse.ArgumentParser(description="Process a file.")
    parser.add_argument('filename', type=str, help='The name of the file to process')
    args=parser.parse_args()
    return args.filename

def main():
    filename=input()
    print(filename)

if __name__ == "__main__":
    main()
