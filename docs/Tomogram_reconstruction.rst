Tomogram Reconstruction using eTomo
====================================

IMOD version:  4.12.30 & Ubuntu 22.04 LTS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. note::

    Prepare tilt series into individual directory, which can be helpful for afterwards processing.

    In SerialEM, saving .mdoc file for each tilt is very helpful, if not, using script to reorder tilt series from -54 to 54.

    The following note using .mrc file withouth .mdoc.

    Name tilt-series as TS_XX.st 
    

1. Prepare tilt-series for emClarity workflow
""""""""""""""""""""""""""""""""""""""""""""""

Making image stacks:

.. code-block:: console
    
    newstack ??*.mrc TS_27/TS_27.st


2. Initiate eTomo
"""""""""""""""""

Start eTomo: 

.. code-block:: console
    
    etomo

.. image:: images/etomo_01.png
  :width: 400




Go to emClarity GitHub and in the Wiki page, download by clicking the latest version v1.6.1: `<https://github.com/StochasticAnalytics/emClarity/wiki>`_

After download, editing the emclarity_1.6.0_v21a file to point out the matlab runtime path: 

.. code-block:: console

    MCR_BASH=/usr/local/MATLAB/MATLAB_Runtime/v910/runtime/glnxa64:/usr/local/MATLAB/MATLAB_Runtime/v910/bin/glnxa64:/usr/local/MATLAB/MATLAB_Runtime/v910/sys/os/glnxa64:/usr/local/MATLAB/MATLAB_Runtime/v910/extern/bin/glnxa64

    export emClarity_ROOT=/home/hzhan/emClarity_1.6.0/emClarity_1.6.1.0
    export LD_LIBRARY_PATH=${emClarity_ROOT}/lib:${MCR_BASH}:${LD_LIBRARY_PATH}


Creating a emClarity alias so that you can call emClarity easily:

.. code-block:: console

    #!/bin/bash
    export PATH="/home/hzhan/emClarity_1.6.0/emClarity_1.6.1.0/bin:$PATH"
    alias emClarity='/home/hzhan/emClarity_1.6.0/emClarity_1.6.1.0/bin/emClarity_1_6_1_0_v21a'


3. Make test run to check installation
""""""""""""""""""""""""""""""""""""""

.. code-block:: console

    emClarity check


If you want to check detailed manual created by Thomas Frosio, here is the link to his github: `<https://github.com/ffyr2w/emClarity-tutorial>`_

