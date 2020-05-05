"""
This module is for home work 5
It has a class Tone which has different functions as described in the document
"""
import matplotlib.pyplot as plt
import numpy as np
from pip._vendor.distlib.compat import raw_input
from scipy.io.wavfile import write
import os


class Tone:
    """
    Definition of class Tone
    """

    def __init__(self, f=0, dur=0, sr=44100, signal=0, orig_signal=0, overtones={}, OT_num=0):
        """
        inti method to initialize the class variables
        :param f: frequency
        :param dur: duration
        :param sr: sampling rate
        :param signal: a numpy array that stores the tone plus the overtones, if any.
        :param orig_signal:  a numpy array that stores the simple one-frequency tone with frequency f1 (i.e., no overtones).
        :param overtones: a dictionary that stores the overtones.
        :param OT_num: the number of overtones present.
        """
        self.f = f
        self.dur = dur
        self.sr = sr
        self.signal = signal
        self.orig_signal = orig_signal
        self.overtones = overtones
        self.OT_num = OT_num

    def get_tone(self, f, dur, play_sound=False):
        """
        Generates a tone at the given fundamental frequency, f1
        :param f: frequency
        :param dur: duration
        :param play_sound: keyword argument
        :return: original signal generated which is a numpy array¬
        """
        self.f = f
        self.dur = dur
        time_pts = np.linspace(0, self.dur, int(self.dur * self.sr))
        amp = 2 ** 10  # amplitude set ot 2^10
        self.orig_signal = np.int16(amp * np.sin(np.pi * 2 * self.f * time_pts))
        if play_sound:
            self.play_sound(outside_signal=self.orig_signal)
        return self.orig_signal

    def get_overtone(self, multi, play_sound=None):
        """
        Generates an overtone that has a frequency that is multi×f1
        :param multi: multi parameter
        :param play_sound: keyword argument
        :return: None
        """
        ot_f = multi * self.f
        time_pts = np.linspace(0, self.dur, int(self.dur * self.sr))
        amp = 2 ** 10  # amplitude set ot 2^10
        ot_signal = np.int16(amp * np.sin(np.pi * 2 * ot_f * time_pts))
        self.overtones[ot_f] = ot_signal
        self.OT_num += 1
        if play_sound:
            self.play_sound(outside_signal=ot_signal)
        return None

    def comb_tones(self):
        """
        Combines the tone at f1 and all overtones present
        :return: the signal list
        """
        normalize = 0
        OT_weights = self.overtones.copy()
        for i in OT_weights:
            OT_weights[i] = int(raw_input('Please enter weight for overtone {:f}: '.format(i)))
        for key in OT_weights:
            normalize += OT_weights[key] ** 2
        normalize **= .5
        for key in OT_weights:
            OT_weights[key] = OT_weights[key] / normalize
            self.signal += OT_weights[key] * self.overtones[key]
        return self.signal

    def play_sound(self, outside_signal=None, sample_rate=44100, vol=0.05):
        """
        Plays the combined tone
        :param outside_signal: outside signal
        :param sample_rate: sample rate
        :param vol: volume
        :return:
        """
        if outside_signal is None:
            write('tmp.wav', sample_rate, np.int16(vol * self.signal))
            os.system("afplay tmp.wav")
            os.system("rm tmp.wav")
        else:
            write('tmp.wav', sample_rate, outside_signal)
            os.system("afplay tmp.wav")
            os.system("rm tmp.wav")

    def plot_fourier(self, sample_rate=44100, freq_lim=2000., amp_lim=1e7):
        """
        Plots the real and imaginary parts of the DFT of the combined tone
        :param sample_rate: sample rate
        :param freq_lim: frequency limit
        :param amp_lim: amplitude limit
        :return: NA
        """
        ft = np.fft.fft(self.signal)
        freq = np.fft.fftfreq(self.signal.shape[0], d=1. / sample_rate)

        plt.figure()
        plt.plot(freq, ft.real, 'b-')
        plt.xlim([-freq_lim, freq_lim])
        plt.ylim([-amp_lim, amp_lim])
        plt.figure()
        plt.plot(freq, ft.imag, 'g-')
        plt.xlim([-freq_lim, freq_lim])
        plt.ylim([-amp_lim, amp_lim])
        plt.show()

    def plot_sound(self, t_lim=0.02):
        """
        Plots the combined tone against tim
        :param t_lim: time limit
        :return: NA
        """
        time = np.linspace(0, self.dur, int(self.dur * self.sr))
        plt.figure()
        plt.title("Sound Wave vs. Time")
        plt.plot(time, self.signal)
        plt.xlim([0, t_lim])
        plt.show()


fund1 = Tone()
fund2 = Tone()
fund3 = Tone()
fund4 = Tone()

A = fund1.get_tone(440., .5)  # A tone.
B = fund2.get_tone(493.88, .5)  # B tone.
D = fund3.get_tone(587.33, .5)  # D tone.
G = fund4.get_tone(392., .5)  # G tone.

fund1.get_overtone(2)
fund1.get_overtone(3)
fund1.get_overtone(4)
f1_rich = fund1.comb_tones()


# B D G should also have overtone, so build a function to do it                      -5

print("For A tone, the frequency, sampling_rate, duration, and number of overtones are:",
      fund1.f, ',', fund1.sr, ',', fund1.dur, ',', fund1.OT_num)

fund1.play_sound()
fund1.plot_sound()
fund1.plot_fourier(freq_lim=2000.)

melody = np.concatenate(np.array([B, A, G, A, B, B, B, B, A, A, A, A]))
mel = Tone()
mel.play_sound(outside_signal=melody)
print("Done playing the melody")
