# fractune
**Sound to fractals.**

## Sound Features

### 1. Spectral Features
- Spectral Centroid: Indicates where the "center of mass" for the sound is located in frequency. It can give a sense of "brightness" or "dullness" of a sound.
- Spectral Bandwidth: Relates to the width of the band of frequencies that are present, indicating the sound's "spread" in the frequency domain.
- Spectral Contrast: Measures the difference in amplitude between peaks and valleys in the spectrum, providing a sense of the sound's timbral texture.
- Spectral Rolloff: The frequency below which a certain percentage of the total spectral energy is contained, often used to distinguish between harmonic and noise components.

### 2. Rhythmic Features
- Tempo: The overall estimated speed of the music in beats per minute (BPM).
- Beat Track: Beyond just tempo, the specific times at which beats occur.
- Onset Strength: The times at which notes or sounds start, which can be more granular than beats and useful for triggering visual changes.

### 3. Harmonic Features
- Chroma Features: Represent the intensity of each of the 12 different pitch classes and can be used to detect chords or harmonic changes.
- Tonnetz: Represents tonal centroids features, capturing harmonic relationships such as fifths, minor thirds, and major thirds, providing another view into the harmony of the piece.

### 4. Temporal Features
- Zero Crossing Rate: The rate at which the audio signal changes sign, which can be indicative of the "noisiness" or "smoothness" of a sound.
- Root Mean Square (RMS) Energy: Provides a measure of the sound's "loudness" over time.



## Mapping Audio Features to Fractal Parameters:

### 1. Tempo
The overall tempo of the piece could dictate the speed of changes or rotations within the fractal animation, with faster tempos leading to quicker movements.

```tempo, _ = librosa.beat.beat_track(y=y, sr=sr)```

### 2. Beat Tracking
Beats could trigger specific events in the visualization, such as sudden color shifts, shape changes, or the initiation of movement.


```
_, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
beat_times = librosa.frames_to_time(beat_frames, sr=sr)
```

### 3. Spectral Centroid
This feature indicates where the "center of mass" for the spectrum is located and can vary with different instruments or sounds. It could control the color palette of the fractal, with lower centroids leading to cooler colors and higher centroids to warmer colors.


```spectral_centroids = librosa.feature.spectral_centroid(y=y, sr=sr)[0]```

### 4. Chroma Features
Chroma features capture the harmonic content of music and can be used to change the fractal's geometry or symmetry in relation to the harmony or chord progressions.

```chroma = librosa.feature.chroma_stft(y=y, sr=sr)```

### 5. Spectral Bandwidth
The spectral bandwidth relates to the width of the spectrum and can influence the fractal's complexity or density, with wider bandwidths leading to more complex fractals.

```spectral_bandwidth = librosa.feature.spectral_bandwidth(y=y, sr=sr)[0]```


### 6. Mel-Frequency Cepstral Coefficients (MFCCs)
MFCCs capture timbral aspects and could be used to modify aspects of the fractal that relate to texture or fine details.

```mfccs = librosa.feature.mfcc(y=y, sr=sr)```


## Current plan:
- Dynamic Range: Map the dynamic range of the audio (difference between loud and soft parts) to the fractal's zoom level or iteration depth.
- Rhythm and Temporal Features: Use rhythm detection or onset strength to modulate the fractal's animation speed or to introduce rhythmic visual elements.
- Harmonic Changes: Use changes in chroma or harmonic content to alter fractal patterns or introduce new elements/colors.