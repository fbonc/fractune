import librosa

#filename = r'audioprocessing\sounds\bliss.mp3'

class AudioLoader:
    def __init__(self, filepath) -> None:
        self.filepath = filepath

    def load_audio(self):
        y, sr = librosa.load(self.filepath)
        return y, sr
    

class FeatureExtractor:
    def __init__(self, audio, sr) -> None:
        self.audio = audio
        self.sr = sr

    def get_tempo(self):
        return librosa.beat.tempo(y=self.audio, sr=self.sr)
    
    def get_beat_times(self):
        _, beat_frames = librosa.beat.beat_track(y=self.audio, sr=self.sr)
        return librosa.frames_to_time(beat_frames, sr=self.sr)
    
    def get_spectral_centroid(self):
        return librosa.feature.spectral_centroid(y=self.audio, sr=self.sr)

    def get_chroma(self):
        return librosa.feature.chroma_stft(y=self.audio, sr=self.sr)
    
    def get_spectral_bandwidth(self):
        return librosa.feature.spectral_bandwidth(y=self.audio, sr=self.sr)[0]
    
    def get_mfccs(self):
        return librosa.feature.mfcc(y=self.audio, sr=self.sr)



audio_loader = AudioLoader(r'audioprocessing\sounds\bliss.wav')
audio, sr = audio_loader.load_audio()

extractor = FeatureExtractor(audio, sr)
tempo = extractor.get_tempo()
spectral_centroid = extractor.get_spectral_centroid()
beat_times = extractor.get_beat_times()
chroma = extractor.get_chroma()
spectral_bandwidth = extractor.get_spectral_bandwidth()
mfccs = extractor.get_mfccs()


print(f"---Tempo: {tempo},")
print(f"---Beat times: {beat_times},")
print(f"---Spectral Centroid: {spectral_centroid}")
print(f"---Chroma: {chroma},")
print(f"---Spectral_bandwidth: {spectral_bandwidth},")
print(f"---MFCCs: {mfccs},")

