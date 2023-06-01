#!/bin/csh -f
#
#  Script to correct a MRC stacked tilt series for the CTF
#
#      Usage:
#	   CTFcorrectstack.csh  Input_stack  Output_stack  Tiltfile [Nprocs]
# 
#       where
#           Input_stack:  Input stack from IMOD
#           Output_stack: Output CTF-corrected stack in MRC, MODE 2
#           Tiltfile:     Text File containing tilt angles (as in IMOD).
#           Nprocs:       No. Processors for parallel computing (optional).
#
#       This script uses the script CTFcorrect.csh to correct
#       images extracted from the stack.
#   
#       This script uses IMOD to extract images, to re-stack them
#       and to read the image header.
#
#      
#   Temporary files created by this script:
#       * __image###.mrc     : contains image ### extracted from the stack
#       * __ctfimage###.mrc  : contains the CTF version of the image ###
#       * __ctfimage###.log  : logfile of CTF correction process of image ###
#
#--------------------
if($#argv != 4 && $#argv != 5) then
    echo Usage: CTFcorrectstack.csh  Input_stack  Output_stack  Tiltfile CTFcorrect \[Nprocs\]
    exit
    endif
#--------------------
set stack=$1
set CTFstack=$2
set tiltfile=$3
set CTFcorrect=$4
if($#argv == 5) then
    set Nprocs=$5
else
    set Nprocs=1
endif


# Get Nviews in the tiltseries by invoking IMOD's header program ...
#                                         ... we use full path, just in case. 
set myIMODpath=`which ctfphaseflip`
set myIMODpath=`dirname $myIMODpath`
set Nimgs=`${myIMODpath}/header -size $stack | awk '{printf("%d", $3)}'`
set CSHPATH=`dirname $0`

echo Stacked tilt series $stack containing $Nimgs images

set j=0
set i=1
while ($i <= $Nimgs)

    set i3=`printf "%03d" $i`

    # Extract the tilt angle of the current image
    set tiltangle=`head -n $i $tiltfile | tail -n 1`

    echo Correcting image $i for the CTF, tilt angle = $tiltangle

    # Extract the image i (index = j = i -1) from the stack
    newstack -verbose 0 -secs $j $stack __image$i3.mrc > __ctfimage$i3.log 

    # How many processes are running?. Add 1 to not get higher than Nprocs
    set running=`ps -c | grep CTFcorrect.exe | wc -l | awk '{printf("%d",$1+1)}'`
    
    # Launch the correction. (No more than Nprocs processes run simultaneously)
    if($running < $Nprocs) then   # background, with monitor mode disabled.
       $CSHPATH/$CTFcorrect __image$i3.mrc __ctfimage$i3.mrc $tiltangle >> __ctfimage$i3.log  ; rm -f __image$i3.mrc &
    else                    # foreground
       $CSHPATH/$CTFcorrect __image$i3.mrc __ctfimage$i3.mrc $tiltangle >> __ctfimage$i3.log  ; rm -f __image$i3.mrc 
    endif
    
@ j ++
@ i ++
end

# Wait for all children processes to complete.
wait

# Create CTF-corrected stack
newstack __ctfimage???.mrc $CTFstack

# Concatenate Log files onto $CTFstack.log
cat __ctfimage???.log > $CTFstack.log

# Clean temporary files
rm -f __ctfimage???.mrc*  __image???.mrc* __ctfimage???.log 
