import numpy as np
import matplotlib.pyplot as plt
from PRN_generator import PRN 

class Transmitter:
    
    def __init__(self, N = 1000, Tch = 1, freq = 1000, M = 2000, sv=1):
        
        code = PRN.prn(sv)

        self.N = N
        self.Tch = Tch #ns

        self.freq = freq
        self.fc = 1/self.Tch
        self.M = M
        self.Ts = self.Tch / self.M
        self.t = np.arange(0,self.N,self.Ts)
        self.Pr = 1

        self.msg = np.resize(np.repeat(code,self.M), int(self.N/self.Ts))

    def modulate(self):
        msg = self.msg
        msg[msg == 0] = -1
        carrier_wave = np.sqrt(2*self.Pr) * np.cos(2*np.pi*self.freq*self.t)
        transmit = carrier_wave * msg
        return transmit
