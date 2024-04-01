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
        self.windowed_frequency_domain_signal=None

        # Alter these parameters to change performance
        self.window_size = 20 # I'm assuming this is measured in number of samples
        self.window_overlap = 5
        self.bins=[40,80,120,180,300]
        self.fuzz=2

        try:
            self.read_file()
            print("[LOG] -- Audio data read successfully.")
            print(f"[LOG] -- Sample Rate: {self.sampling_rate}")
        except Exception as e:
            print(f"\033[91m[ERROR]\033[0m -- Error reading audio data: {e}")
            # Should format [ERROR] in red.

        if self.do_window == True:
            try:
                self.Windowed_FFT()
                print("[LOG] -- Windowed FFT performed successfully.")
                print(f"[LOG] -- Length of FFT signal: {len(self.windowed_frequency_domain_signal)}")
            except Exception as e:
                print("\033[91m[ERROR]\033[0m -- Error computing windowed FFT: {e}")
        elif self.do_window == False:
            try:
                self.Full_FFT()
                print("[LOG] -- Full FFT performed successfully")
                print(f"[LOG] -- Length of FFT signal: {len(self.frequency_domain_signal)}")
            except Exception as e:
                print("\033[91m[ERROR]\033[0m -- Error computing full FFT: {e}")

        try:
            self.Fingerprint()
            print("[LOG] -- Fingerprint calculated")
            print(f"[LOG] -- Fingerprint Tag: {self.fingerprint_tag}")
        except Exception as e:
            print("\033[91m[ERROR]\033[0m -- Error finding fingerprint: {e}")
        
        
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

    def Full_FFT(self):
        if self.time_domain_signal is not None:
            self.frequency_domain_signal = np.fft.fft(self.time_domain_signal)
            return True
        else:
            print("No audio data available. Read audio data first.")
            return False

    def Windowed_FFT(self):
        if self.time_domain_signal is not None:
            num_chunks=int((len(self.time_domain_signal) - self.window_size) / (self.window_size - self.window_overlap)) + 1
            self.windowed_frequency_domain_signal = np.zeros((num_chunks, self.window_size), dtype=np.complex128)

            for i in range(num_chunks):
                start=i*(self.window_size-self.window_overlap)
                end=start+self.window_size
                chunk=self.time_domain_signal[start:end]
                self.windowed_frequency_domain_signal[i]=np.fft.fft(chunk)

            return True
        else:
            print("No audio data available. Read audio data first")
            return False

    def Fingerprint(self):

        def get_bin(freq):
            i=0
            while i< len(self.bins) and self.bins[i]<freq:
                i+=1
            return i

        def window_characterize():
            characterizations=[]
            for window in self.windowed_frequency_domain_signal:
                window_characterization=[]
                for freq in range(self.bins[0], self.bins[-1]):
                    mag=abs(window[freq])
                    print(mag)

        def characterize():
            characterizations=[[0,0] for _ in range(len(self.bins))]
            for freq in range(self.bins[0], self.bins[-1]):
                magnitude=np.log(np.abs(self.frequency_domain_signal[freq]))
                bin=get_bin(freq)
                if magnitude > characterizations[bin][0]:
                    characterizations[bin][0]=magnitude
                    characterizations[bin][1]=freq
            return characterizations

        def hash(h1, h2, h3, h4):
            h1_f=(h1-(h1%self.fuzz))
            h2_f=(h2-(h2%self.fuzz))*100
            h3_f=(h3-(h3%self.fuzz))*100000
            h4_f=(h4-(h4%self.fuzz))*100000000
            return h4_f + h3_f + h2_f + h1_f
            
            
        if self.windowed_frequency_domain_signal is not None:
            result=window_characterize()
        elif self.frequency_domain_signal is not None:
            result=characterize()

        if result is not None:
            for item in result:
                if isinstance(item, list):
                    self.fingerprint_tag=hash(result[0][1], result[1][1], result[2][1], result[3][1])
                else:
                    print("I have't figured out dimensions for the windowed fft yet")
                
            # for window in result:
                # print(window)
                # hash(window[1][1], window[2][1], window[3][1], window[4][1])


        
def main():

    # Parse Command Line Arguments
    parser=argparse.ArgumentParser(description='Perform Frequency Analysis on an audio file')
    parser.add_argument('filename', type=str, help='Name of file to process')

    args=parser.parse_args()
    filename=args.filename


    # Run Main Code
    audio=FrequencyAnalysis(filename)
    if audio.read_file():
        print("Audio data read successfully.")
        print(f"Sample Rate: {audio.sampling_rate}")
    if audio.Full_FFT():
        print("Full spectrum FFT computed successfully.")
        print(f"Length: {len(audio.frequency_domain_signal)}")
    audio.Fingerprint()
    if audio.fingerprint_tag:
        print(audio.fingerprint_tag)
    

if __name__ == "__main__":
    main()
