#!/bin/sh

# set it up for jupyter
python -m ipykernel install --user --name=$CONDA_DEFAULT_ENV
conda install ipykernel
ipython kernel install --user --name=$CONDA_DEFAULT_ENV
