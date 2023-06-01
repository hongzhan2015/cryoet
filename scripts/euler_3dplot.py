import sys
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

def main():
    file_angles = sys.argv[1]
    angles = np.loadtxt(file_angles, delimiter = ",")
    #ptl_number = len(angles)
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    ax.scatter(angles[:,0], angles[:,1], angles[:,2])
    plt.show()

if __name__ == '__main__':  
    # Calling main() function
    main()