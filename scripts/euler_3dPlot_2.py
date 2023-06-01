import sys
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm, colors
from physt import special

def main():
    file_angles = sys.argv[1]
    angles = np.loadtxt(file_angles, delimiter = ",")
    ptl=len(angles)
    h = special.spherical_histogram(angles, theta_bins=16, phi_bins=16)
    globe = h.projection("theta", "phi")
    p = globe.plot.globe_map(density=True, figsize=(5,5), cmap="Reds")
    cbar=plt.colorbar(p)

    plt.show()
    
    

if __name__ == '__main__':  
    # Calling main() function
    main()