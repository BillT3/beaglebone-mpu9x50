from mpu9150 import MPU9150
import time
import cPickle as pickle
import numpy as np

accel_data = []
gyro_data = []
mag_data = []
time_data = []

mpu = MPU9150()

elapsed_time = 0
start_time = time.time()
while elapsed_time < 100:
    accel_data.append(mpu.accel.xyz)
    gyro_data.append(mpu.gyro.xyz)
    mag_data.append(mpu.mag.xyz)
    elapsed_time = time.time() - start_time
    time_data.append(elapsed_time)

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

