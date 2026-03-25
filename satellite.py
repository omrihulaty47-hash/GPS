from transmitter import *

c = 300000 #light second in km

class Satellite:
    def __init__(self, pos):
        self.transmitter = Transmitter()
        self.pos = pos

    def signal(self, r_pos):
        dist = math.dist(self.pos, r_pos) #dist between satellite and receiver
        b = 1023 * dist / c #empty bits until signal is received
        return np.pad(self.transmitter.modulate(), (b, 0), mode='constant')