'''Extract sensor readings from an MPU data log pickle, and save to CSV.

This script is used to run batch-mode TRICAL (https://github.com/sfwa/TRICAL)
on the sensor data in order to calibrate the magnetometer. My logger saves the
data as a pickel file, and TRICAL wants a CSV file.

Matt Vernacchia
2015 Dec 9
'''

import argparse
import cPickle as pickle
import numpy as np

def main(args):
    # Load data from pickle file.
    with open(args.in_file, 'rb') as f:
        data = pickle.load(f)
    if args.data_name == 'gyro_data':
        # Gyro data from MPU-9150 is in deg/s.
        y = data[args.data_name]
    if args.data_name == 'accel_data':
        # Accel data from MPU-9150 is in g, convert to m/s**2.
        y = 9.81 * data[args.data_name]
    if args.data_name == 'mag_data':
        # Magnetometer data from MPU-9150 is in microtesla.
        y = data[args.data_name]

    # Write data to CSV
    np.savetxt(args.outfile, y, fmt='%.6f', delimiter=',')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convert MPU data pickle to CSV.')
    parser.add_argument('in_file', type=str, help='Pickle file of MPU IMU data.')
    parser.add_argument('data_name', type=str,
        choices=['gyro_data', 'accel_data', 'mag_data'],
        help='Key for data in the pickle dict.')
    parser.add_argument('outfile', type=str, help='Name for the new CSV file')
    args = parser.parse_args()
    main(args)
