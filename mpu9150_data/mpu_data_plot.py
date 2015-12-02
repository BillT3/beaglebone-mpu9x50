import cPickle as pickle
import numpy as np
from matplotlib import pyplot as plt


with open('mpu_data_2015-12-02_06-23-06.p', 'rb') as f:
    d = pickle.load(f)

colors = ['r', 'g', 'b']

plt.subplot(3,1,1)
for i in xrange(3):
    plt.plot(d['time'], d['accel_data'][:,i], color=colors[i])
plt.xlabel('Time [s]')
plt.ylabel('Acceleration [g]')

plt.subplot(3,1,2)
for i in xrange(3):
    plt.plot(d['time'], d['gyro_data'][:,i], color=colors[i])
plt.xlabel('Time [s]')
plt.ylabel('Ang rate [deg / s]')

plt.subplot(3,1,3)
for i in xrange(3):
    plt.plot(d['time'], d['mag_data'][:,i], color=colors[i])
plt.xlabel('Time [s]')
plt.ylabel('Magnetic field [uT]')

plt.show()