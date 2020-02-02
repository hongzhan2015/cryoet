import sys
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm, colors

def main():
    file_angles = sys.argv[1]
    angles = np.loadtxt(file_angles, delimiter = ",")
    x = angles[:,0]
    y = angles[:,1]
    z = angles[:,2]
    group = angles[:,3]
    #ptl_number = len(angles)
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    p = ax.scatter(angles[:,0], angles[:,1], angles[:,2], s=20, c=group, )
    #plt.colorbar(p)
    plt.show()

if __name__ == '__main__':  
    # Calling main() function
    main()
