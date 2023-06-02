Installation emClarity for subtomogram averaging
================================================

Linux system - Ubuntu 22.04LTS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To get the latest emClarity github, please visit `emClarity <https://github.com/StochasticAnalytics/emClarity/wiki>`_ for more information. 

.. note::

    It is possible to rebuild emClarity from its source code. But it is pretty difficult to do.

    emClarity runs on GPUs, and both workstation with Titan RTX and GPU server equipped with A100 will do the job. 
    Attention for matlab runtime version.

    You also need to make sure IMOD and Chimera on the PATH so that emClarity can find them. 
    
    Make sure CUDA is in the PATH also. 

1. Download & Install matlab runtime
""""""""""""""""""""""""""""""""""""
Require matlab runtime v2021a.

To install matlab runtime:


.. code-block:: console
    
    wget https://ssd.mathworks.com/supportfiles/downloads/R2021a/Release/8/deployment_files/installer/complete/glnxa64/MATLAB_Runtime_R2021a_Update_8_glnxa64.zip
    mkdir matlab_runtime_install
    unzip glnxa64/MATLAB_Runtime_R2021a_Update_8_glnxa64.zip -d ./matlab_runtime_install
    sudo ./install -agreeToLicense yes

To configure matlab runtime path:
---------------------------------- 

+------------------------+------------------+----------------------------------------------------+
| OS system              |      Env Var     |        Dir                                         |
+========================+==================+====================================================+
| Windows OS             |       PATH       | 	<MATLAB_RUNTIME_INSTALL_DIR>\runtime\<arch>      |
+------------------------+------------------+----------------------------------------------------+
| Linux OS               | LD_LIBRARY_PATH  |   <MATLAB_RUNTIME_INSTALL_DIR>/runtime/glnxa64     |
|                        |                  |   <MATLAB_RUNTIME_INSTALL_DIR>/bin/glnxa64         |
|                        |                  |   <MATLAB_RUNTIME_INSTALL_DIR>/sys/os/glnxa64      |
|                        |                  |   <MATLAB_RUNTIME_INSTALL_DIR>/extern/bin/glnxa64  |
+------------------------+------------------+----------------------------------------------------+
| Mac OS                 | DLD_LIBRARY_PATH |   <MATLAB_RUNTIME_INSTALL_DIR>/runtime/maci64      |
|                        |                  |   <MATLAB_RUNTIME_INSTALL_DIR>/bin/maci64          |
|                        |                  |   <MATLAB_RUNTIME_INSTALL_DIR>/sys/os/maci64       |
|                        |                  |   <MATLAB_RUNTIME_INSTALL_DIR>/extern/bin/maci64   |
+------------------------+------------------+----------------------------------------------------+

2. Download latest emclarity version
""""""""""""""""""""""""""""""""""""

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

