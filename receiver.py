import numpy as np
import matplotlib.pyplot as plt
from transmitter import *

class Receiver:
    def __init__(self, N, Tch, freq, M):
        code = np.zeros(1023)
        
        start_state = 1 << 9 | 1
        lfsr = start_state
        period = 0


        while True:
            bit = (((lfsr & 1) + ((lfsr & 8) >> 3)) % 2)
            code[period] = lfsr & 1
            lfsr = (lfsr >> 1) | (bit << 9)
            period += 1
            if lfsr == start_state:
                # print(period)
                break

        self.N = N
        self.Tch = Tch #ns


        self.freq = freq
        self.fc = 1/self.Tch
        self.M = M
        self.Ts = self.Tch / self.M
        self.t = np.arange(0,self.N,self.Ts)
        self.Pr = 1

        self.msg = np.resize(np.repeat(code,self.M), int(self.N/self.Ts))


    def demodulate(self, sig,fIF):
        sig = sig * np.sqrt(2) * np.cos(2*np.pi*(self.freq-fIF)*self.t)
        SI = sig * 2 * np.cos(2*np.pi*fIF*self.t)
        SQ = sig * -2 * np.sin(2*np.pi*fIF*self.t)
        
        return SI, SQ

    def cross_correlation(x, y):
        np.correlate(x, y, mode="valid")
    
transmitter = Transmitter(2000, 1, 10, 20)
transmit = transmitter.modulate()
plt.plot(transmitter.t, transmitter.msg)
plt.show()
plt.plot(transmitter.t, transmit)
plt.show()

reciver = Receiver(2000, 1, 10 ,20)
SI, SQ = reciver.demodulate(transmit, 2)
plt.plot(reciver.t, SQ)
plt.show()
plt.plot(reciver.t, SI)
plt.show()