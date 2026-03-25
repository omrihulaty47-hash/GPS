# from satellite import *

# p0 = (0, 0, 0) #my position

# s1 = Satellite((1000, 1000, 1000))
# s2 = Satellite((2000, 2000, 2000))
# s3 = Satellite((3000, 3000, 3000))
# s4 = Satellite((4000, 4000, 4000))

# arrays = [s1.signal(p0), s2.signal(p0), s3.signal(p0), s4.signal(p0)]

# values = np.concatenate(arrays)
# indices = np.concatenate([np.arange(len(a)) for a in arrays])

# result = np.bincount(indices, weights=values)

from transmitter import *
from receiver import *
import scipy.signal as sig

def window_avg(signal, win):
    weights = np.ones(win) / win
    return np.convolve(signal, weights, mode='same')


signal = np.zeros(20000)

for i in range(3):
    sv = (i+1) * 3
    transmitter = Transmitter(10000, 10, 1000, 20, sv = sv)
    transmit = transmitter.modulate()
    transmit = Transmitter.delay_transmit(transmit, (i+1) * 1000)
    signal += transmit

reciver = Receiver(10000, 10, 1000, 20)
SI, SQ = reciver.demodulate(signal, 2)

taus = []

for i in range(10):
    x = reciver.cross_correlation(SI, i+1)
    # peaks, properties = sig.find_peaks(x, prominence=100)
    # print(peaks)
    if len(x[x>20000]) > 0:
        taus.append((reciver.t-reciver.t[len(reciver.t)//2])[x>20000][0])
    # taus.append(None if len([x>20000]) == 0 else reciver.t[x>20000][0])
    # plt.plot(reciver.t-reciver.t[len(reciver.t)//2], x)
    # plt.show()

print(taus)