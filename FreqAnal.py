from re import error
import soundfile as sf
import argparse
import numpy as np
import matplotlib.pyplot as plt

class FrequencyAnalysis:
    def __init__(self, filename, plot=False, window=False):
        self.filename=filename
        self.do_plot=plot
        self.do_window=window
        self.time_domain_signal=None
        self.frequency_domain_signal=None

        # Alter these parameters to change performance
        self.window_size = 20 # I'm assuming this is measured in number of samples
        self.window_overlap = 5
        self.bin_frequencies=[60,240,500,2000,8000]
        # Got new bin frequencies from this website
        # https://www.petervis.com/hi-fi-info/jvc-sea-graphic-equalizers/frequency-spectrum-of-common-musical-instruments.html
        # Represents superlows (0-60), lows (61-240), mids (241-500), highs (501-2000), and superhighs (2001-8000)
        # This should do a better job representing a wider range of frequencies, since frequency is a logarithmic scale.
        self.fuzz=2

        try:
            self.read_file()
            print("[LOG] -- Audio data read successfully.")
            print(f"[LOG] -- Sample Rate: {self.sampling_rate}")
        except Exception as e:
            print(f"\033[91m[ERROR]\033[0m -- Error reading audio data: {e}")
            # Should format [ERROR] in red.

        try:
            self.FFT()
            print("[LOG] -- Full FFT performed successfully")
            print(f"[LOG] -- Length of FFT signal: {len(self.frequency_domain_signal)}")
        except Exception as e:
            print(f"\033[91m[ERROR]\033[0m -- Error computing full FFT: {e}")

        try:
            self.Fingerprint()
            print("[LOG] -- Characteristic Array calculated")
            print(f"[LOG] -- Characteristic Array: {self.CharacteristicArray}")
        except Exception as e:
            print(f"\033[91m[ERROR]\033[0m -- Error finding Characteristic Array: {e}")

    def CalcBinIndex(self, Freq):
        """
        Calculates the index at which a certain frequency (Hz) will appear. Rounds down.
        Freq=(n*SampFreq)/TotalN, therefore at 44100 kHz with 1024 sample FFT, Bin 2 is 86.1 Hz.
        I make an assumption here that this means that 86.1 is the upper limit to the frequencies contained in that bin.
        """
        SamplingFrequency=self.sampling_rate
        TotalN=len(self.frequency_domain_signal)
        BinNumber=(Freq*TotalN)/SamplingFrequency
        BinNumber=int(BinNumber)
        return BinNumber
        
        
    def read_file(self):
        try:
            # Read file, check number of audio channels.
            data, sample_rate=sf.read(self.filename)
            channels=data.shape[1] if len(data.shape) > 1 else 1

            # Combine channels if there are multiple
            # Taking the average of a stereo stream should give mono
            if channels > 1:
                data=np.mean(data, axis=1)

            self.time_domain_signal=data
            self.sampling_rate=sample_rate
            return True
        except Exception as e:
            print(f"Error reading audio file: {e}")
            return False

    def FFT(self):
        if self.time_domain_signal is not None:
            self.frequency_domain_signal = np.fft.fft(self.time_domain_signal)
            return True
        else:
            print("No audio data available. Read audio data first.")
            return False

    def Fingerprint(self):

        def get_bin_indeces() -> list[int]:
            """
            Takes the list of frequency breakpoints defined in self.bin_frequencies, and converts those to indeces in terms of the normalized FFT.
            """
            bins=[]
            for freq in self.bin_frequencies:
                index=self.CalcBinIndex(freq)
                bins.append(index)
            return bins
        
        def get_bin(freq):
            i=0
            while i< len(self.bins) and self.bins[i]<freq:
                i+=1
            return i

        def characterize():
            characterizations=[[0,0,0] for _ in range(len(self.bins))]
            bin_values=[ [0,0] for _ in range(len(self.bins)) ]
            for freq in range(self.bins[0], self.bins[-1]):
                magnitude=np.log(np.abs(self.frequency_domain_signal[freq]))
                bin=get_bin(freq)
                if magnitude > characterizations[bin][0]:
                    characterizations[bin][0]=magnitude
                    characterizations[bin][1]=freq
                    bin_values[bin][0]=np.abs(self.frequency_domain_signal[freq])
                    bin_values[bin][1]=np.angle(self.frequency_domain_signal[freq])
                    # Create an array of polar coordinates. These polar coordinates represent the BIN with the largest magnitude per SEGMENT.
            return bin_values

        self.bins=get_bin_indeces()
            
        if self.frequency_domain_signal is not None:
            result=characterize()
            # print(result)

        if result is not None:
            self.CharacteristicArray=result


        
def main():

    # Parse Command Line Arguments
    parser=argparse.ArgumentParser(description='Perform Frequency Analysis on an audio file')
    parser.add_argument('filename', type=str, help='Name of file to process')

    args=parser.parse_args()
    filename=args.filename


    # Run Main Code
    audio=FrequencyAnalysis(filename)
    # print(audio.frequency_domain_signal)
if __name__ == "__main__":
    main()
