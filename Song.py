from FreqAnal import FrequencyAnalysis


class Song():
    def __init__(self, filename):
        self.filename=filename

        # Analysis Classes
        self.Freq=FrequencyAnalysis(filename) # Plot = False
        
