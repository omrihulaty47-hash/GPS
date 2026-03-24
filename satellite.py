from transmitter import *

class Satellite:
    def __init__(self, N, Tch, freq, M, pos):
        self.transmitter = Transmitter(N, Tch, freq, M)
        self.pos = pos

    def signal(self, sig, r_pos):
        dist = math.dist(self.pos, r_pos)
        return np.pad(sig, (dist, 0), mode='constant')

s1 = Satellite(1,1,1,1,(1,1,1))
s2 = Satellite(1,1,1,1,(1,1,1))
s3 = Satellite(1,1,1,1,(1,1,1))
s4 = Satellite(1,1,1,1,(1,1,1))
