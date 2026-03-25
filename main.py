from satellite import *

p0 = (0, 0, 0) #my position

s1 = Satellite((1000, 1000, 1000))
s2 = Satellite((2000, 2000, 2000))
s3 = Satellite((3000, 3000, 3000))
s4 = Satellite((4000, 4000, 4000))

arrays = [s1.signal(p0), s2.signal(p0), s3.signal(p0), s4.signal(p0)]

values = np.concatenate(arrays)
indices = np.concatenate([np.arange(len(a)) for a in arrays])

result = np.bincount(indices, weights=values)