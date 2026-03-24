import numpy as np
import matplotlib.pyplot as plt

class Transmitter:
    
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
        # print(len(self.msg))

    def modulate(self):
        msg = self.msg
        msg[msg == 0] = -1
        carrier_wave = np.sqrt(2*self.Pr) * np.cos(2*np.pi*self.freq*self.t)
        transmit = carrier_wave * msg
        return transmit
    

# transmitter = Transmitter(2000, 1, 10, 20)
# transmit = transmitter.modulate()
# plt.plot(transmitter.t[:1000], transmit[:1000])
# plt.show()