from scipy.io.wavfile import read
help(read)

(fs, x) = read('../../sounds/flute-A4.wav')
print(fs)

print(x)

print(x.size)

print(x.size/fs)

print(x.size/float(fs))

import matplotlib.pyplot as plt
plt.plot(x)
plt.show()

import numpy as np
t = np.arange(x.size)/float(fs)
plt.plot(t,x)
plt.show()

y = x[44100:45100]
from scipy.io.wavfile import write
write('test.wav', fs, y)