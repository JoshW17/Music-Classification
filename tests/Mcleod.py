import numpy as np
import soundfile as sf

def fft_mp3(input_file, output_file):
    data, samplerate = sf.read(input_file)
    fft_data=np.fft.fft(data)
    np.save(output_file, fft_data)
    np.savetxt(output_file + '.txt', fft_data)

fft_mp3('../assets/TheBoxer.mp3', 'SimonAndGarfunkel-TheBoxer')
fft_mp3('../assets/VivaLaVida.mp3', 'Coldplay-VivaLaVida')


