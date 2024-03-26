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
x = np.linspace(-N/2, (N/2)-1, N) # N for the shift
fft_result = np.fft.fft(data) # FFT fo audio data

plt.plot(x, np.fft.fftshift(abs(fft_result))) # Take magnitude with abs() and shift data with fftshift()
plt.xlabel('Frequency')
plt.ylabel('Magnitude')
plt.title('FFT shifted')
plt.show()

# Now we just need to make a "fingerprint of the song"
# We will do this by getting the highest magnitude in each "bin" of frequencies
# we will choose bins of 30 Hz - 40 Hz, 40 Hz - 80 Hz and 80 Hz - 120 Hz for
# the low tones (covering bass guitar, for example), and 120 Hz - 180 Hz and
# 180 Hz - 300 Hz for the middle and higher tones (covering vocals and most other instruments)

bins = [80, 120, 180, 300] # bins -> 0,1,2,3 / above 300 dont care

def getBin(freq): # gives us which bin of frequencies we are in
    i = 0
    while bins[i] < freq:
        i = i + 1
    return i

highestMag = [[0, 0], [0, 0], [0, 0], [0, 0]]
for freq in range(40,300):  # get the highest magnitude and its corresponding frequency for each bin
    magnitude = abs(fft_result[freq])
    bin = getBin(freq)
    if magnitude > highestMag[bin][0]:
        highestMag[bin][0] = magnitude # get the highest magnitude
        highestMag[bin][1] = freq # corresponding frequency
print(highestMag)

FUZZ_FACTOR = 2 # assuse recorded in a not ideal room / give some wiggle

def hash(h1, h2, h3, h4):
    return (h4 - (h4 % FUZZ_FACTOR)) * 100000000 + (h3 - (h3 % FUZZ_FACTOR)) * 100000 + (h2 - (h2 % FUZZ_FACTOR)) * 100 + (h1 - (h1 % FUZZ_FACTOR)) # generate a hash for the song or "fingerprint"

fingerprint = hash(highestMag[0][1], highestMag[1][1], highestMag[2][1], highestMag[3][1])
print(fingerprint)
