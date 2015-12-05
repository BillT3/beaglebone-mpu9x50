from mpu9150 import MPU9150
import time
import cPickle as pickle
import numpy as np
import signal
import sys
 
accel_data = []
gyro_data = []
mag_data = []
time_data = []

mpu = MPU9150()


def sigint_handler(signal, frame):
    print 'SIGINT caught'

    print 'Saving data and exiting...'

    d = {
        'time': np.array(time_data),
        'accel_data': np.array(accel_data),
        'gyro_data': np.array(gyro_data),
        'mag_data': np.array(mag_data)
    }

    filename = 'mpu_data_{:s}.p'.format(
        time.strftime('%Y-%m-%d_%H-%M-%S'))
    with open(filename, 'wb') as f:
        pickle.dump(d, f)
    sys.exit(0)


signal.signal(signal.SIGINT, sigint_handler)
print 'Press ctrl-c to stop and save data'
elapsed_time = 0
start_time = time.time()
while True:
    accel_data.append(mpu.accel.xyz)
    gyro_data.append(mpu.gyro.xyz)
    mag_data.append(mpu.mag.xyz)
    elapsed_time = time.time() - start_time
    time_data.append(elapsed_time)


