import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def ZXZeuler2matrix(ZXZ):
    """
    Converts ZXZ euler angles ([1,3] numpy array) into a [3,3] rotation matrix defining the same rotation
    Rewritten from dynamo function 'dynamo_euler2matrix'
    :param ZXZ: euler angles in ZXZ convention in degrees
    :type ZXZ: [1,3] numpy array
    :return: rotation matrix
    """
    tdrot = ZXZ[0]
    tilt = ZXZ[1]
    narot = ZXZ[2]

    tdrot = tdrot * np.pi / 180
    narot = narot * np.pi / 180
    tilt = tilt * np.pi / 180

    costdrot = np.cos(tdrot)
    cosnarot = np.cos(narot)
    costilt = np.cos(tilt)
    sintdrot = np.sin(tdrot)
    sinnarot = np.sin(narot)
    sintilt = np.sin(tilt)

    m11 = costdrot * cosnarot - sintdrot * costilt * sinnarot
    m12 = - cosnarot * sintdrot - costdrot * costilt * sinnarot
    m13 = sinnarot * sintilt
    m21 = costdrot * sinnarot + cosnarot * sintdrot * costilt
    m22 = costdrot * cosnarot * costilt - sintdrot * sinnarot
    m23 = -cosnarot * sintilt
    m31 = sintdrot * sintilt
    m32 = costdrot * sintilt
    m33 = costilt

    rotation_matrix = np.array([[m11, m12, m13], [m21, m22, m23], [m31, m32, m33]])
    return rotation_matrix

def matrix2ZXZeuler(rotation_matrix):
    "Converts rotation matrix ([3,3] numpy array) into ZXZ euler angles ||| taken from dynamo function dynamo_matrix2euler"
    # Set a tolerance because of indetermination in defining narot and tdrot
    tolerance = 1e-4

    # Check special cases
    # rm(3,3) != -1
    if np.absolute(rotation_matrix[2, 2] - 1) < tolerance:
        tdrot = 0
        tilt = 0
        narot = np.arctan2(rotation_matrix[1, 0], rotation_matrix[2, 2]) * 180 / np.pi

        ZXZeuler = np.array([tdrot, tilt, narot])
        return ZXZeuler


    # rm(3,3) != -1
    elif np.absolute(rotation_matrix[2, 2] + 1) < tolerance:
        tdrot = 0
        tilt = 180
        narot = np.arctan2(rotation_matrix[1, 0], rotation_matrix[0, 0]) * 180 / np.pi

        ZXZeuler = np.array([tdrot, tilt, narot])
        return ZXZeuler


    # general case
    else:
        tdrot = np.arctan2(rotation_matrix[2, 0], rotation_matrix[2, 1]) * 180 / np.pi
        tilt = np.arccos(rotation_matrix[2, 2]) * 180 / np.pi
        narot = np.arctan2(rotation_matrix[0, 2], -rotation_matrix[1, 2]) * 180 / np.pi

        ZXZeuler = np.array([tdrot, tilt, narot])
        return ZXZeuler



class EulerAngles:
    """Manage Euler angles for a set of particles"""
    def __init__(self, data=[], convention='not_defined', reference_frame='not_defined'):
        # numpy array [N,3]
        self.euler_angles = data

        # Euler angle convention triplet e.g. 'ZXZ', 'ZYZ'
        self.convention = convention

        # Euler angle reference frame, either 'particle' or 'template'
        # This defines whether the euler angles define rotations of particles onto templates (particle)
        # or templates onto particles (template)
        self.reference_frame = reference_frame

    def calculate_rotation_matrices(self):
        "Write out an [N,3,3] numpy arrays containing a 3x3 rotation matrix for each of N particles"
        nParticles = self.euler_angles.shape[0]
        rotation_matrices = np.empty([nParticles, 3, 3])

        # ZXZ Convention
        if self.convention == 'ZXZ':
            counter = 0
            for triplet in self.euler_angles:
                rotation_matrix = ZXZeuler2matrix(triplet)
                rotation_matrices[counter, :, :] = rotation_matrix
                counter += 1

            self.rotation_matrices = rotation_matrices
            return self.rotation_matrices

        else:
            print("Rotation matrix calculation not yet implemented for euler angles in {} convention".format(
                self.convention))

    def calculate_euler_angles(self):
        "Calculate euler angles from rotation matrices"
        nParticles = self.rotation_matrices.shape[0]
        euler_angles = np.zeros([nParticles, 3])

        # ZXZ convention
        if self.convention == 'ZXZ':

            counter = 0
            for rotation_matrix in self.rotation_matrices:
                euler_angles[counter, 0:3] = matrix2ZXZeuler(rotation_matrix)
                counter += 1

            self.euler_angles = euler_angles
            return self.euler_angles

    def change_reference_frame(self):
        "Changes reference frame for euler angles from particle to template or vice-versa, recalculating the euler angles"

        # ZXZ convention
        if self.convention == 'ZXZ':

            # Calulate rotation matrices
            self.calculate_rotation_matrices()

            # Transpose rotation matrices (changes reference frame)
            counter = 0
            for rotation_matrix in self.rotation_matrices:
                self.rotation_matrices[counter, :, :] = np.transpose(rotation_matrix)
                counter += 1

            # Recalculate euler angles from transposed rotation matrices
            self.calculate_euler_angles()

            # Update reference frame

            if self.reference_frame == 'particle':
                print("Reference frame changed from 'particle' to 'template'")
                self.reference_frame = 'template'
            elif self.reference_frame == 'template':
                self.reference_frame = 'particle'
                print("Reference frame changed from 'template' to 'particle'")


def quiver3d_rotation(positions, rotation_matrices):
    """
    Plots 3D positions and arrows pointing in a direction defined by a rotation matrix
    :param positions: [N,3] numpy array containing N [X, Y, Z] positions.
    :param rotation_matrices: [N,3,3] numpy array containing N [3,3] rotation matrices
    :return:
    """
    # Define a vector that points along the Z axis (like the z-axis (symmetry axis) of our reference)
    # from the origin [0,0,0]
    initial_direction = np.array([[0],[0],[1]])

    # Rotate this vector by each of our N rotation matrices (make sure rotation matrices define rotation of reference
    # onto particle. (transpose of matrix defining rotation of particle onto reference)
    directions_after_rotation = np.matmul(rotation_matrices, initial_direction[np.newaxis, :])
    directions_normalised_for_position = directions_after_rotation[:, :, 0] + positions

    x = positions[:, 0]
    y = positions[:, 1]
    z = positions[:, 2]

    u = np.transpose(directions_normalised_for_position[:, 0])
    v = np.transpose(directions_normalised_for_position[:, 1])
    w = np.transpose(directions_normalised_for_position[:, 2])

    # Plot the positions and directions
    fig = plt.figure()
    ax = fig.gca(projection='3d')

    # Define cubic bounding box to simulate 'axis equal' from matlab plotting
    max_range = np.array([x.max() - x.min(), y.max() - y.min(), z.max() - z.min()]).max() / 2.0

    mid_x = (x.max() + x.min()) * 0.5
    mid_y = (y.max() + y.min()) * 0.5
    mid_z = (z.max() + z.min()) * 0.5
    ax.set_xlim(mid_x - max_range, mid_x + max_range)
    ax.set_ylim(mid_y - max_range, mid_y + max_range)
    ax.set_zlim(mid_z - max_range, mid_z + max_range)

    ax.quiver(x, y, z, u, v, w, length=0.1, normalize=True)
    ax.scatter3D(x,y,z)

    return ax

def quiver3d_emClarity(positions, euler_angles):
    """
    Plotting emClarity Euler angles at particle positions in 3D
    :param positions: [N,3] numpy array of N [x,y,z] positions
    :param EulerAngles: [N,3] numpy array of ZXZ euler angles from emClarity
    :return:
    """
    # Instantiate EulerAngles class
    angles = EulerAngles(data=euler_angles, convention='ZXZ', reference_frame='particle')

    # emClarity uses euler angles in ZXZ convention describing active rotations of particles
    # Need to change reference frame to describe rotation of reference (z-aligned) onto particle
    angles.change_reference_frame()

    # plot using quiver3d_rotation
    ax = quiver3d_rotation(positions, angles.rotation_matrices)

    return ax

import sys
def main():
    file_position = sys.argv[1]
    file_angles = sys.argv[2]
    positions = np.loadtxt(file_position, delimiter=",")
    angles = np.loadtxt(file_angles, delimiter=",")
    #print(positions.shape)
    #print(angles.shape)
    ax = quiver3d_emClarity(positions,angles)
    plt.show()
if __name__ == '__main__':  
    # Calling main() function
    main()
