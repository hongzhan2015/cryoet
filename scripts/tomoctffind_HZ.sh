#!/bin/sh

# tomopctffind.sh: for a tilt-series in a stack

/usr/local/tomoctf/bin/tomoctffind.exe << foo
124_power.mrc
124_diag.mrc
2.7,300,0.07,19500,5.4
0.5,10000,12
20000,100000,1000
foo

mv CTFPROFILE 124_CTFprof.txt
# mv CTFPROFILE.ps 124_CTFprof.ps
mv tomoctf.param 124.param
#
