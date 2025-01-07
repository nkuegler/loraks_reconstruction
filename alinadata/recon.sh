#!/bin/bash

#
#SBATCH -c 16					# 16 cores for fast reco
#SBATCH --mem 500G				# 0.5 mm fully sampled is around 220G, need maybe double
#SBATCH --time 1800				# 10 echoes at 2 hours per echo but some nodes take 3 hours per echo
#SBATCH -o /data/u_kuegler_software/git/loraks_reconstruction/logs/alinadata/%j.out	# redirect the output
#
# Real values for (16 cores, 500G request) are 213G RAM 8.5hrs time 27G file (PDw/T1w), 121G 6.5hrs 10G (MTw)

rawdata=$1
outdir=$2

MATLAB matlab -nodisplay -nodesktop -r "reconstruction('$rawdata','$outdir','/data/u_kuegler_software/git/loraks_reconstruction/alinadata/loraksConfig.json');exit" -sd /data/u_kuegler_software/git/image-reconstruction
