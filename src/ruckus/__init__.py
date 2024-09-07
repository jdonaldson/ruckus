import rumps
import numpy as np
import sounddevice as sd
import threading

class RuckusApp(rumps.App):
    def __init__(self):
        super(RuckusApp, self).__init__("📻 Ruckus")
        self.menu = ["Play (5 min)", "Play (10 min)", "Play (30 min)", "Stop"]
        self.is_playing = False
        self.play_thread = None

    def generate_binaural_beat(self, duration, carrier_freq=110, beat_freq=4, sample_rate=44100):
        t = np.linspace(0, duration, int(sample_rate * duration), False)
        left_freq = carrier_freq
        right_freq = carrier_freq + beat_freq
        left_channel = np.sin(2 * np.pi * left_freq * t)
        right_channel = np.sin(2 * np.pi * right_freq * t)
        audio_data = np.column_stack((left_channel, right_channel))
        return audio_data / (np.max(np.abs(audio_data))*2)

    def play_audio(self, duration):
        audio_data = self.generate_binaural_beat(duration)
        self.is_playing = True
        sd.play(audio_data, 44100)
        sd.wait()
        self.is_playing = False

    @rumps.clicked("Play (5 min)")
    def play_5min(self, _):
        self.play_beat(300)

    @rumps.clicked("Play (10 min)")
    def play_10min(self, _):
        self.play_beat(600)

    @rumps.clicked("Play (30 min)")
    def play_30min(self, _):
        self.play_beat(1800)

    def play_beat(self, duration):
        if self.is_playing:
            rumps.notification("📻 Ruckus", "Already Playing", "Stop the current beat before starting a new one.")
        else:
            self.play_thread = threading.Thread(target=self.play_audio, args=(duration,))
            self.play_thread.start()
            rumps.notification("📻 Ruckus", "Started", f"Playing a {duration//60}-minute binaural beat.")

    @rumps.clicked("Stop")
    def stop(self, _):
        if self.is_playing:
            sd.stop()
            self.is_playing = False
            rumps.notification("📻 Ruckus", "Stopped", "Binaural beat playback stopped.")
        else:
            rumps.notification("📻 Ruckus", "Not Playing", "No binaural beat is currently playing.")

def main():
    RuckusApp().run()

if __name__ == "__main__":
    main()
