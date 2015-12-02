from mpu9150 import MPU9150
import time

imu = MPU9150()

print('Time          Accel          Gyro        Magneto')
start = time.time()
for i in xrange(100):
    print(time.time()-start, imu.accel.xyz, imu.gyro.xyz, imu.mag.xyz)
    
