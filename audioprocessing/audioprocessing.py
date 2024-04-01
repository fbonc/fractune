import librosa

filename = r'audioprocessing\sounds\bliss.mp3'

def beat_processing(filename):
    # 'y' = file as waveform
    # 'sr' = sampling rate
    y, sr = librosa.load(filename, duration=39)

    tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
    print('Estimated tempo: {:.2f} beats per minute'.format(tempo))

    # frame indices of beat events into timestamps
    beat_times = librosa.frames_to_time(beat_frames, sr=sr)
    print(beat_times)

