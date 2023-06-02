Installation IMOD software
==========================

Linux system - Ubuntu 22.04LTS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To download latest IMOD software, please visit `IMOD <https://bio3d.colorado.edu/imod/>`_ for installation. 

Require Java:

.. code-block:: console
    
    java -version

To install java:

.. code-block:: console

    sudo apt install default-jre

1. Download & Install miniconda3
""""""""""""""""""""""""""""""""

To install IMOD with default settings:

.. code-block:: console

    sh imod_4.11.24_RHEL7-64_CUDA8.0.sh

To activate IMOD, source IMOD-Linux.sh or IMOD-linux.csh:

.. code-block:: console

    source /usr/local/IMOD/IMOD-linux.sh


If you want to run IMOD temporarily:

.. code-block:: console

    mkdir imod_install
    wget https://bio3d.colorado.edu/imod/AMD64-RHEL5/imod_4.11.24_RHEL7-64_CUDA8.0.sh
    sh imod_4.11.24_RHEL7-64_CUDA8.0 -dir ./imod_install -skip

You can substitute testIMOD to any directory you want. It is good to install on a server. 

2. Install PEET
""""""""""""""""

PEET is a program developed by Dr. John Heumann. check website: `PEET <https://bio3d.colorado.edu/PEET/>`_ for more information

Useful programs used by PEET: 

To install PEET:

.. code-block:: console

    wget https://bio3d.colorado.edu/ftp/PEET/linux/Particle_1.16.0a_linux.sh
    wget https://bio3d.colorado.edu/ftp/PEET/linux/ParticleRuntimeV99_linux.tgz
    sh Particle_1.16.0a_linux.sh
    tar -xfzf ParticleRuntimeV99_linux.tgz -C /path/where/to/extract/

Add PEET onto the $PATH and reboot the system. 

Check useful webpage for programs inside PEET: `Program Description <https://bio3d.colorado.edu/ftp/PEET/man/html/index.html>`_

I am running all programs on Ubuntu 22.04 for workstation, Centos 7 on GPU server, and the following GPUs:
    - NVIDIA RTX 2080
    - NVIDIA A100
