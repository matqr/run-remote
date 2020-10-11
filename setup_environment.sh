#!/bin/sh

## before running this script copy_env.sh should have been executed

# get name of the curret environment
name=$(grep -A3 'name:' env/environment_ubuntu.yaml | head -n 1 | awk '{print $2}')

# set it up for jupyter
python -m ipykernel install --user --name=name
conda activate name 
conda install ipykernel
ipython kernel install --user --name=name
conda deactivate


