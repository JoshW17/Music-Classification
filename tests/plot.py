import soundfile as sf
import numpy as np
import matplotlib.pyplot as plt

# Read the MP3 file
data, samplerate = sf.read('../assets/21Guns.mp3')

# Extract one channel if stereo
if len(data.shape) > 1:
    # data = data[:, 0]  # Take the first channel
    data=(data[:,0] + data[:,1])/2

# Window
window=np.hanning(len(data))
data=data*window
    
# Calculate FFT
fft_result = np.fft.fft(data)

# Calculate the frequency range
n = len(fft_result)
freq = np.fft.fftfreq(n, d=1/samplerate)

# Plot the FFT
plt.plot(abs(freq), np.abs(fft_result))
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')
plt.title('FFT of MP3 File')
plt.xlim(0,17500)
plt.show()

plt.plot(data)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Time Domain Representation of MP3 File')
plt.show()
