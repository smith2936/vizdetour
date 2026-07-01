#!/bin/bash
conda create -n vizdetour python=3.13 -y
conda activate vizdetour
pip install -r requirements.txt
conda install -c conda-forge firefox geckodriver -y
playwright install