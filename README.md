# Notebook for Cryo-electron tomography data preprocessing
## _Hong Zhan, ver 2023-03-07_

Welcome to check online documents:https://cryoet.readthedocs.io/en/latest/index.html

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

Customized scripts for organizing cryo-electron tomography data pre-processing for the subtomogram pipeline

- Python script
- Docker images
- Bash scripts

### For examples
- Tilt-series are collected using dose-symmetry scheme, and each tilt-series are collected from -{max} to {max} format. You can also use .mdoc file in imod function alignframe, however, it is much better to use unblur and motioncor.

## Frame alignments using unblur on a SLURM cluster
- create a list containing all tiff files
```
ls *.tif >> list.txt
```
- create a submission file
```
#!/bin/bash

#SBATCH -A XXXXXX
#SBATCH -t 1:00:00
#SBATCH -N 1
#SBATCH -n 16
#SBATCH -J unblur
#SBATCH -e unblur-%j-%a.err
#SBATCH -o unblur-%j-%a.out
#SBATCH --array=1-41

LINE=$(sed -n "$SLURM_ARRAY_TASK_ID"p list.txt)

unblur <<foo
${LINE}
${LINE}_aligned.mrc
0.8265
2
yes
300
0.37
0.0
yes
2.0
80.0
1500
1
1
1
20
yes
no
[Gain Reference]
1
0
no
foo
```
Important information check on dockerhub
https://hub.docker.com/r/hzhan3/unblur

## Put aligned tilt-series into corresponding subdirectories
```
python mvsubdir2.py
```
- In the tilt-series subdirectory, rename tilt series according from -{max} to {max}, example here increament degree is 3. 
```
python namechange_3degrees_HZ.py
```

- emClarity and Relion requested an order file that contains tile angle collected in real-time order and is used for dose-weighted analysis. running following script can generate an order file, but need to change corresponding colums:
```
python order_generate.py 
```

This is a simplified manual for using scripts for tomographic data analysis and subtomogram averaging processing using different software packages.
