import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

N = 100

rng = np.random.default_rng()
Tch = 2 #ns
msg = np.array(rng.integers(0,1,size=(N//Tch), endpoint=True))

print(len(msg))

freq = 1000
fc = 1/Tch
M = 2000
Ts = Tch / M
t = np.arange(0,N,Ts)
msg_sig = np.repeat(msg, len(t)/len(msg))
Pr = 1

def butter_bandpass_filter(data, lowcut, highcut, fs, order=5):
    # Design filter using SOS for stability
    sos = signal.butter(order, [lowcut, highcut], btype='bandpass', fs=fs, output='sos')
    # Apply filter with zero phase shift
    return signal.sosfiltfilt(sos, data)

def modulate(msg):
    msg[msg == 0] = -1
    carrier_wave = np.sqrt(2*Pr) * np.cos(2*np.pi*freq*t)
    transmit = carrier_wave * msg
    return transmit

def demodulate(sig,fIF):
    # sig = butter_bandpass_filter(sig * np.sqrt(2) * np.cos(2*np.pi*(freq-fIF)*t), 50, 200, 1/Ts)
    sig = sig * np.sqrt(2) * np.cos(2*np.pi*(freq-fIF)*t)
    SI = sig * 2 * np.cos(2*np.pi*fIF*t)
    SQ = sig * -2 * np.sin(2*np.pi*fIF*t)
    
    plt.plot(t,SI)
    plt.show()
    plt.plot(t,SQ)
    plt.show()

transmit = modulate(msg_sig)
plt.plot(t,msg_sig)
plt.show()
# print(t)
# plt.plot(t[:100],np.sqrt(2*Pr)*np.cos(2*np.pi*freq*t)[:100])
# plt.show()
# plt.plot(t[:100],transmit[:100])
# plt.show()

demodulate(transmit,100)

