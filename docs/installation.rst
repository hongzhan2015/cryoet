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

4. Configuration of multiple GCC and G++
"""""""""""""""""""""""""""""""""
Because some software, like Scripion's plugins, needs specific version of gcc and g++, it is necessary to install multiple version of gcc and g++. 

For example, to install gcc-7,8,9 and g++-7,8,9:
.. code-block:: console

    sudo apt install build-essential
    sudo apt -y install gcc-7 g++-7 gcc-8 g++-8 gcc-9 g++-9

Use the update-alternatives tool to create list of multiple GCC and G++ compiler alternatives: 
.. code-block:: console

    sudo update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-7 7
    sudo update-alternatives --install /usr/bin/g++ g++ /usr/bin/g++-7 7
    sudo update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-8 8
    sudo update-alternatives --install /usr/bin/g++ g++ /usr/bin/g++-8 8
    sudo update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-9 9
    sudo update-alternatives --install /usr/bin/g++ g++ /usr/bin/g++-9 9

Check the available C and C++ compilers list on your Ubuntu 22.04 system and select desired version by entering relevant selection number:  
.. code-block:: console
    
    sudo update-alternatives --config gcc

There are 3 choices for the alternative gcc (providing /usr/bin/gcc).
