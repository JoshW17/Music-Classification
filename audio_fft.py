import soundfile as sf
import numpy as np
import matplotlib.pyplot as plt

filename = input('Input filename (please use full path): ')
data, fs = sf.read(filename)

# Plot raw audio data
plt.figure(1)
plt.plot(data)
plt.xlabel('Sample Index (N)')
plt.ylabel('Amplitude')
plt.title('Audio Wave in Time')

# Plot FFT of audio data shifted
plt.figure(2)

N = len(data)
x = np.linspace(-N/2, (N/2)-1, N)
fft_result = np.fft.fft(data) # FFT fo audio data

plt.plot(x, np.fft.fftshift(abs(fft_result))) # Take magnitude with abs() and shift data with fftshift()
plt.xlabel('Sample Index (N)')
plt.ylabel('Magnitude')
plt.title('FFT shifted')
plt.show()
