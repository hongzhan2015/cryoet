Installation miniconda
======================

Configuration conda environment
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

I am using miniconda3 for configuration of python envirnment `miniconda3 <https://docs.conda.io/en/latest/miniconda.html/>`_ for installation. 

There are couple of main steps to install and configure miniconda3:

1. Download & Install miniconda3
""""""""""""""""""""""""""""""""

.. code-block:: console

    wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
    bash Miniconda3-latest-Linux-x86_64.sh

I recommend not to initate conda at beginning, you can activate conda when you want to by creating line in ./bashrc. 

2. Create environment with name and specific python version:
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

Here is an example for installing IsoNet using Python 3.8

.. code-block:: console

    conda create --name IsoNet python=3.8
    conda activate IsoNet

Install the required plugins via pip:

.. code-block:: console

    pip install -r requirement.txt
    
Install cudnn via conda-forge:

.. code-block:: console

    conda install -c conda-forge cudnn


3. Add program into PATH variable
"""""""""""""""""""""""""""""""""

.. code-block:: console
  #!/bin/bash
  conda activate isonet
  export PATH="/home/hzhan/IsoNet/IsoNet/bin:$PATH"
  export PYTHONPATH="/home/hzhan/IsoNet:$PYTHONPATH"

I am running all programs on Ubuntu 22.04 for workstation, Centos 7 on GPU server, and the following GPUs:
    - NVIDIA RTX 2080
    - NVIDIA A100
