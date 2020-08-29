!/bin/bash

#SBATCH -A emslp50505
#SBATCH -t 1:00:00
#SBATCH --gres=gpu:volta:2
#SBATCH -N 1
#SBATCH -n 16
#SBATCH -J MotionCor
#SBATCH -e MotionCor-%j.err
#SBATCH -o MotionCor-%j.out
#SBATCH --array=1-41

LINE=$(sed -n "$SLURM_ARRAY_TASK_ID"p list.txt)

/home/scicons/cascade/apps/relion/MotionCorr2-1.2.1/MotionCor2 -InTiff ${LINE} \
-OutMrc ${LINE}_sumavg.mrc \
-Iter 10 \
-Tol 0.5 \
-FtBin 2 \
-Kv 300 \
-PixSize 0.8652 \
-Patch 5 5 \
-Gpu 0 1 >> ${LINE}_motioncor2log.txt