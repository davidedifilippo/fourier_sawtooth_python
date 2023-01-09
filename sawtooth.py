import numpy as np
import matplotlib.pyplot as plt


A = float(input('Enter amplitude: '))
f = int(input('Enter frequency: '))
n = int(input('Number of components: '))

t = np.linspace(0, 1/f, num=1000)


# signal = ((2*A)/np.pi)*np.sin(2*np.pi*f*t) + \
#          ((2*A)/(2*np.pi))*np.sin(2*np.pi*2*f*t + np.pi) + \
#          ((2*A)/(3*np.pi))*np.sin(2*np.pi*3*f*t) +\
#          ((2*A)/(4*np.pi))*np.sin(2*np.pi*4*f*t + np.pi) +\
#          ((2*A)/(5 * np.pi)) * np.sin(2 * np.pi * 5 * f * t) +\
#          ((2*A)/(6*np.pi))*np.sin(2*np.pi*6*f*t + np.pi) + \
#          ((2*A)/(7*np.pi))*np.sin(2*np.pi*7*f*t) +\
#          ((2*A)/(8*np.pi))*np.sin(2*np.pi*8*f*t + np.pi) +\
#          ((2*A)/(9 * np.pi)) * np.sin(2 * np.pi * 9 * f * t)

signal = 0

for i in range(1, n):
    signal = signal + ((2*A)/(i*np.pi))*np.sin(2*np.pi*i*f*t + ((i+1)%2) * np.pi)


plt.title('Signal')
plt.plot(t, signal, 'g')
plt.ylabel('Amplitude')
plt.xlabel('time')

plt.show()
