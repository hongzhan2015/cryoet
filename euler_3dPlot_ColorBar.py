import sys
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib import cm, colors
from physt import special
import physt
from scipy.special import sph_harm

def main():
    file_angles = sys.argv[1]
    angles = np.loadtxt(file_angles, delimiter = ",")
    X = angles[:,0]
    Y = angles[:,1]
    Z = angles[:,2]
    h = special.spherical_histogram(angles, theta_bins=20, phi_bins=20)
    globe = h.projection("theta", "phi")
    m = np.amax(globe.bins)
    n = np.amin(globe.bins)
    norm = mpl.colors.Normalize(vmin=n, vmax=m)
    ax = globe.plot.globe_map(density=True, figsize=(7,7), cmap="Reds")
    plt.colorbar(cm.ScalarMappable(norm=norm, cmap="Reds"), ax=ax)
    plt.show() 

if __name__ == '__main__':  
    # Calling main() function
    main()