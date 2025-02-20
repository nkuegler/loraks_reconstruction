#!/usr/bin/env python3

"""
This script is used to submit reconstruction jobs to a computing cluster using SLURM. 
It reads configuration variables from config.py, constructs input and output paths, and submits jobs 
for each subject and session specified in the configuration.
Functions:
    sbatch_commands: Submits jobs to the cluster for each subject and session.
    This function iterates over the subjects and sessions specified in the configuration,
    constructs the necessary input and output paths, and submits SLURM jobs for T1-weighted,
    PD-weighted, and MT-weighted raw data reconstruction.
    Raises:
        TypeError: If the subject name is not a string or if the session name is not a string or list.
"""


import os
import warnings

import config_alina as config

# script defining slurm parameters and reconstruction command
script_dir = os.path.dirname(os.path.abspath(__file__))
recon_script = os.path.join(script_dir, 'recon.sh')

# configuration variables
input_parent = config.input_parent
output_parent = config.output_parent
t1w_raw = config.t1w_raw
pdw_raw = config.pdw_raw
mtw_raw = config.mtw_raw
sub_ses = config.sub_ses
name_storage_dir = config.name_storage_dir


## check if sub_ses, t1w, pdw, and mtw are of the same length
if len(sub_ses) != len(t1w_raw) or \
        len(sub_ses) != len(pdw_raw) or \
        len(sub_ses) != len(mtw_raw):
    raise ValueError("Length of sub_ses, t1w_raw, pdw_raw, and mtw_raw must be the same")


def sbatch_commands():
    """
    Submit jobs to the cluster
    """
    for i, (subject_name, session_name) in enumerate(sub_ses):

        if not isinstance(subject_name, str):
            raise TypeError("Subject (sub_ses[0]) must be of type string")
        
        if isinstance(session_name, str):
            session_name = [session_name] # convert session element to list for iteration
        
        if isinstance(session_name, list):
            for sess in session_name:
                
                # specify output directory (reconstructed data)
                output_dir = os.path.join(output_parent, subject_name, sess, name_storage_dir)
                if not os.path.exists(output_dir):
                    os.makedirs(output_dir, exist_ok=True)
                
                if os.listdir(output_dir):
                    warnings.warn(f"Output path {output_dir} is not empty. Skipping this session.")
                    continue
                
                # specify input directory (raw data)
                input_path = os.path.join(input_parent, subject_name, sess, "dcm/rawdata")

                t1w_input_path = os.path.join(input_path, t1w_raw[i])
                os.system(f'sbatch -p all,group_servers,gr_weiskopf {recon_script} {t1w_input_path} {output_dir}')
                
                pdw_input_path = os.path.join(input_path, pdw_raw[i])
                os.system(f'sbatch -p all,group_servers,gr_weiskopf {recon_script} {pdw_input_path} {output_dir}')
                
                mtw_input_path = os.path.join(input_path, mtw_raw[i])
                os.system(f'sbatch -p all,group_servers,gr_weiskopf {recon_script} {mtw_input_path} {output_dir}')
        
        else:
            raise TypeError("Session (sub_ses[1]) must be of type string or list")


if __name__ == "__main__":
    sbatch_commands()



