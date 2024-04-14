from FreqAnal import FrequencyAnalysis
from librosa.onset import onset_strength
from librosa.feature.rhythm import tempo

class Song():
    def __init__(self, filename):
        self.filename=filename

        # Analysis Classes
        self.Freq=FrequencyAnalysis(filename)

        self.sampling_rate=self.Freq.sampling_rate
        self.TimeData=self.Freq.time_domain_signal
        self.FreqData=self.Freq.frequency_domain_signal

        onset_env=onset_strength(y=self.TimeData, sr=self.sampling_rate)
        self.tempo=tempo(onset_envelope=onset_env, sr=self.sampling_rate)
        

        
