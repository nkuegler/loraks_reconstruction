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
import json
from datetime import datetime

import config_infantdata as config # import the correct config file


# script defining slurm parameters and reconstruction command
script_dir = os.path.dirname(os.path.abspath(__file__))
recon_script = os.path.join(script_dir, 'recon_infants.sh')

# configuration variables
input_parent = config.input_parent
output_parent = config.output_parent
sub_ses = config.sub_ses
name_storage_dir = config.name_storage_dir
patterns_to_check = config.patterns_to_check

## check if input_parent and output_parent exist
if not os.path.exists(input_parent):
    raise FileNotFoundError(f"Input parent directory {input_parent} does not exist")

if not os.path.exists(output_parent):
    print(f"Output parent directory {output_parent} does not exist. Creating it now.")
    os.makedirs(output_parent, exist_ok=True)


for (_, session_name) in sub_ses:
    if isinstance(session_name, str):
        session_name = [session_name] # convert session element to list for iteration


def sbatch_commands():
    output_paths_raw = {}  # store paths to the raw data for each subject and session -> export as json at the end of the script

    """
    Submit jobs to the cluster
    """
    for i, (subject_name, session_name) in enumerate(sub_ses):

        if not isinstance(subject_name, str):
            raise TypeError("Subject (sub_ses[0]) must be of type string")
        
        if isinstance(session_name, list):
            for j, sess in enumerate(session_name):
                
                # specify output directory (reconstructed data)
                output_dir = os.path.join(output_parent, subject_name, sess, name_storage_dir)
                if not os.path.exists(output_dir):
                    os.makedirs(output_dir, exist_ok=True)
                
                if any(os.path.isfile(os.path.join(output_dir, f)) for f in os.listdir(output_dir)):
                    warnings.warn(f"Output path {output_dir} is not empty. Skipping this session.")
                    continue
                
                # specify input directory (raw data)
                input_path = os.path.join(input_parent, subject_name, sess, "raw")
                session_data = []
                file_reco_counter = 0

                # Step into the input_path and check for files matching patterns
                if os.path.exists(input_path): 
                    for file in os.listdir(input_path):
                        file_path = os.path.join(input_path, file)
                        if os.path.isfile(file_path) and any(pattern in file for pattern in patterns_to_check):
                            os.system(f'sbatch -p long,group_servers,gr_weiskopf {recon_script} {file_path} {output_dir}')
                            session_data.append(file_path)
                            file_reco_counter += 1
                else:
                    warnings.warn(f"Input path {input_path} does not exist. Skipping this session.")

                
                # store paths to the raw data for each subject and session
                if subject_name not in output_paths_raw:
                    output_paths_raw[subject_name] = {}
                output_paths_raw[subject_name][sess] = session_data

                print(f"""
                      ----------------
                      Batch job submitted for {file_reco_counter} files for subject {subject_name} and session {sess}.
                      ----------------
                      """)

        else:
            raise TypeError("Session (sub_ses[1]) must be of type string or list")

    
    # export paths that were used for reconstruction for documentation purposes
    current_time = datetime.now().strftime("%Y%m%d_%H%M")
    output_filename = f'loraks_rawData_{current_time}.json'
    with open(os.path.join(output_parent, output_filename), 'w') as json_file:
        json.dump(output_paths_raw, json_file, indent=4)



if __name__ == "__main__":
    sbatch_commands()
