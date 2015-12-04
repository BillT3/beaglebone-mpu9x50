import cPickle as pickle
import numpy as np
from matplotlib import pyplot as plt
import argparse

def main(args):
    with open(args.data_file, 'rb') as f:
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


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Plot pickled MPU data.')
    parser.add_argument('-d', '--data_file', type=str, help='Name of pickle file.')
    args = parser.parse_args()
    main(args)