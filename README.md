# cryoet
Script for Cryo-tomography workflow

## Plot average back to the tomograms using emClarity
1) extract variable in matlab: 
$a.$ running csvwrite('filename.csv',variable.cycle#.Avg_geometry.tilt#)
$b.$ column 14-16 are Euler angle, with convention: Z1-X-Z2; From emClarity website: 'The angles input to emClarity describe ZXZ active intrinsic rotations of the particles coordinate system. That is to say, the basis vectors describing the average particle in the microscope reference frame are rotated (positive anti-clockwise) around Z, the new X, and the new Z axis. The final transformation describes the coordinate system attached to any given particle in your data set.'
'Given the above description of the Euler angles, the gridvectors calculated in matlab (micrscope basis) are transformed by Z1,X,Z2 and used to ask what is the density there, rotate it back into the microscope reference frame. To rotate an average from the microscope frame to the particle, the gridvectors are multiplied by -Z2,-X,-Z1.'
$c.$ copy out the 14-16 Euler angle in a csv table, then change Z1-X-Z2 to Z2-X-Z1 then multiple by (-1)
$d.$ run MOTL2Slicer INPUT OUTPUT, output file will be written in X, Y, Z convention
$e.$ copy output into summary.csv, first column is #coutour, #X, #y, #z, x_angle, y_angle, z_angle
$f.$ run clonemodel -at summary.csv INPUT.mod OUTPUT.mod

