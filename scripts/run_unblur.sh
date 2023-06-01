#!/bin/bash

# copy tar file from /mnt/gluster into the working directory
cp /mnt/gluster/hzhan3/janelia_mar19/n58/$1 ./ 

# untar unblur from cistem
tar -xzf cistem.tar.gz

# add path to the environment
mkdir home
export HOME=$(pwd)/home
export PATH=$(pwd)/cistem:$PATH

# unblur 
unblur << foo
$1
$1_aligned.mrc
1.77
2
yes
300
1.0
0.0
yes
2.0
80.0
150
1
1
1
20
yes
yes
1
0
no
foo

# to transfer big outout to proper file system
tar -czvf $1_aligned.tar.gz $1_aligned.mrc
mv $1_aligned.tar.gz /mnt/gluster/hzhan3/janelia_mar19/n58
rm $1_aligned.tar.gz $1 $1_aligned.mrc

## END

