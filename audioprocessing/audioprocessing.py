import librosa
import matplotlib.pyplot as plt
import numpy

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
    
    def get_spectral_centroids(self):
        centroids = librosa.feature.spectral_centroid(y=self.audio, sr=self.sr)
        times = librosa.frames_to_time(range(len(centroids[0])), sr=self.sr, hop_length=512)
    
        return centroids, times

    def get_chroma(self):
        return librosa.feature.chroma_stft(y=self.audio, sr=self.sr)
    
    def get_spectral_bandwidth(self):
        return librosa.feature.spectral_bandwidth(y=self.audio, sr=self.sr)[0]
    
    def get_mfccs(self):
        return librosa.feature.mfcc(y=self.audio, sr=self.sr)
    
    # def get_onset_strength(self):
    # def get_amplitude(self):

if __name__ == "__main__":

    def print_features(tempo, beat_times, spectral_centroids, chroma, spectral_bandwidth, mfccs):
        print(f"Tempo: {tempo},")
        print(f"Beat times: {beat_times},")
        print(f"Spectral Centroids: {spectral_centroids}")
        print(f"Chroma: {chroma},")
        print(f"Spectral_bandwidth: {spectral_bandwidth},")
        print(f"MFCCs: {mfccs},")

    def plot_spectral_centroids(spectral_centroids_times, spectral_centroids):
        plt.figure(figsize=(10, 4))
        plt.semilogy(spectral_centroids_times, spectral_centroids.T, label='Spectral Centroid')
        plt.ylabel('Frequency (Hz)')
        plt.xlabel('Time (s)')
        plt.title('Spectral Centroid over Time')
        plt.legend()
        plt.show()

    def plot_chroma(chroma):
        plt.figure(figsize=(10, 4))
        librosa.display.specshow(chroma, y_axis='chroma', x_axis='time')
        plt.colorbar()
        plt.title('Chroma Features')
        plt.tight_layout()
        plt.show()


    audio_loader = AudioLoader(r'audioprocessing\sounds\bliss.wav')
    audio, sr = audio_loader.load_audio()

    extractor = FeatureExtractor(audio, sr)
    tempo = extractor.get_tempo()
    spectral_centroids, spectral_centroids_times = extractor.get_spectral_centroids()
    beat_times = extractor.get_beat_times()
    chroma = extractor.get_chroma()
    spectral_bandwidth = extractor.get_spectral_bandwidth()
    mfccs = extractor.get_mfccs()


    print_features(tempo, beat_times, spectral_centroids, chroma, spectral_bandwidth, mfccs)
    # plot_spectral_centroids(spectral_centroids_times, spectral_centroids)
    # plot_chroma(chroma)


    