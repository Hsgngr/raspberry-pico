"""
This script converts given wav file to frequency f0 and saves as list.
"""
import numpy as np
from scipy.io import wavfile
from scipy.signal import correlate, fftconvolve
import matplotlib.pyplot as plt
from contextlib import redirect_stdout

def indexes(y, thres=0.3, min_dist=1, thres_abs=False):
    """Peak detection routine borrowed from 
    https://bitbucket.org/lucashnegri/peakutils/src/master/peakutils/peak.py
    """
    if isinstance(y, np.ndarray) and np.issubdtype(y.dtype, np.unsignedinteger):
        raise ValueError("y must be signed")

    if not thres_abs:
        thres = thres * (np.max(y) - np.min(y)) + np.min(y)

    min_dist = int(min_dist)

    # compute first order difference
    dy = np.diff(y)

    if np.all(dy) == 0:
        return 0

    # propagate left and right values successively to fill all plateau pixels (0-value)
    zeros, = np.where(dy == 0)

    # check if the signal is totally flat
    if len(zeros) == len(y) - 1:
        return np.array([])

    if len(zeros):
        # compute first order difference of zero indexes
        zeros_diff = np.diff(zeros)
        # check when zeros are not chained together
        zeros_diff_not_one, = np.add(np.where(zeros_diff != 1), 1)
        # make an array of the chained zero indexes
        zero_plateaus = np.split(zeros, zeros_diff_not_one)

        # fix if leftmost value in dy is zero
        if zero_plateaus[0][0] == 0:
            dy[zero_plateaus[0]] = dy[zero_plateaus[0][-1] + 1]
            zero_plateaus.pop(0)

        # fix if rightmost value of dy is zero
        if len(zero_plateaus) and zero_plateaus[-1][-1] == len(dy) - 1:
            dy[zero_plateaus[-1]] = dy[zero_plateaus[-1][0] - 1]
            zero_plateaus.pop(-1)

        # for each chain of zero indexes
        for plateau in zero_plateaus:
            median = np.median(plateau)
            # set leftmost values to leftmost non zero values
            dy[plateau[plateau < median]] = dy[plateau[0] - 1]
            # set rightmost and middle values to rightmost non zero values
            dy[plateau[plateau >= median]] = dy[plateau[-1] + 1]

    # find the peaks by using the first order difference
    peaks = np.where(
        (np.hstack([dy, 0.0]) < 0.0)
        & (np.hstack([0.0, dy]) > 0.0)
        & (np.greater(y, thres))
    )[0]

    # handle multiple peaks, respecting the minimum distance
    if peaks.size > 1 and min_dist > 1:
        highest = peaks[np.argsort(y[peaks])][::-1]
        rem = np.ones(y.size, dtype=bool)
        rem[peaks] = False

        for peak in highest:
            if not rem[peak]:
                sl = slice(max(0, peak - min_dist), peak + min_dist + 1)
                rem[sl] = True
                rem[peak] = False

        peaks = np.arange(y.size)[~rem]

    return peaks

def freq_from_autocorr_improved(signal, fs):
    signal -= np.mean(signal)  # Remove DC offset
    corr = fftconvolve(signal, signal[::-1], mode='full')
    corr = corr[len(corr)//2:]

    d = np.diff(corr)

    if np.all(d) == 0:
        return 0
    else:
        # Find the first peak on the left
        index = indexes(corr, thres=0.8, min_dist=5)
        if len(index) == 0:
            return 0
        else:
            i_peak = index[0]
            i_interp = parabolic(corr, i_peak)[0]

    return fs / i_interp

def parabolic(f, x):
    xv = 1/2. * (f[x-1] - f[x+1]) / (f[x-1] - 2 * f[x] + f[x+1]) + x
    yv = f[x] - 1/4. * (f[x-1] - f[x+1]) * (xv - x)
    return (xv, yv)

def convert_freq_to_tones(signal, fs, length):
    tones = []

    for i in range(0, len(signal), int(fs*length)):
        small_part = signal[i:i+int(fs*length)]

        #plt.plot(small_part)
        #plt.plot(t, y)
        #plt.show()
        if i > 10 * fs:  # if you wanna record more than 10 seconds comment out here.
            break # and here

        tone = freq_from_autocorr_improved(small_part, fs)
        if type(tone) == list:
            tones.append(0)
        else:
            tones.append(round(tone))

    return tones

def wav_to_freq(file,length=0.01):
    fs, signal = wavfile.read(file)
    signal = np.array(signal).mean(axis=1)
    #signal = signal[:, 0]  # use the first channel (or take their average, alternatively)
    tones = convert_freq_to_tones(signal, fs, length)
    return tones


def record_tones(song_file,tones_file,length=0.01):
    with open(tones_file, 'w') as f:
        with redirect_stdout(f):
            print(wav_to_freq(song_file, length))


if __name__ == "__main__":

    song_file = "ringtone/nokia3310.wav"
    write_file = 'tones.txt'
    record_tones(song_file,write_file,length=0.01)