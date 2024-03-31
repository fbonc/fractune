package com.fbonc.app;

import be.tarsos.dsp.AudioDispatcher;
import be.tarsos.dsp.AudioEvent;
import be.tarsos.dsp.io.jvm.AudioDispatcherFactory;
import be.tarsos.dsp.pitch.PitchDetectionHandler;
import be.tarsos.dsp.pitch.PitchDetectionResult;
import be.tarsos.dsp.pitch.PitchProcessor;
import be.tarsos.dsp.pitch.PitchProcessor.PitchEstimationAlgorithm;

import java.io.File;

public class AudioProcessing {

    public static void main(String[] args) {
        try {
            String audioFilePath = "bliss.wav";
            File audioFile = new File(audioFilePath);
            AudioDispatcher dispatcher = AudioDispatcherFactory.fromFile(audioFile, 2048, 1024);
            
            PitchDetectionHandler pitchDetectionHandler = new PitchDetectionHandler() {
                @Override
                public void handlePitch(PitchDetectionResult pitchDetectionResult, AudioEvent audioEvent) {
                    final float pitchInHz = pitchDetectionResult.getPitch();
                    System.out.printf("Pitch: %.2f Hz\n", pitchInHz);
                }
            };
            
            PitchProcessor pitchProcessor = new PitchProcessor(PitchEstimationAlgorithm.YIN, 44100, 2048, pitchDetectionHandler);
            dispatcher.addAudioProcessor(pitchProcessor);
            
            new Thread(dispatcher, "Audio Dispatcher").start();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
