import numpy as np
import matplotlib.pyplot as plt
from transmitter import *
from PRN_generator import PRN


class Receiver:
    def __init__(self, N, Tch, freq, M):
        
        self.N = N
        self.Tch = Tch #ns


        self.freq = freq
        self.fc = 1/self.Tch
        self.M = M
        self.Ts = self.Tch / self.M
        self.t = np.arange(0,self.N,self.Ts)
        self.Pr = 1

    def demodulate(self, sig,fIF):
        sig = sig * np.sqrt(2) * np.cos(2*np.pi*(self.freq-fIF)*self.t)
        SI = sig * 2 * np.cos(2*np.pi*fIF*self.t)
        SQ = sig * -2 * np.sin(2*np.pi*fIF*self.t)
        
        return SI, SQ

    def cross_correlation(self, x, sv):
        code = np.resize(np.repeat(PRN.prn(sv),self.M), int(self.N/self.Ts))
        return np.correlate(x, code, mode="same")
    
