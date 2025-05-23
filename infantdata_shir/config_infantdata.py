#!/usr/bin/env python3

## subject names and session names
## if there are multiple sessions for a subject, the session names should be in a list
sub_ses = [["sub-006", ["20240218"]],
           ["sub-017", ["20240304"]],
           ["sub-021", ["20240309"]],
           ["sub-027", ["20240312"]],
           ["sub-031", ["20240318"]],
           ["sub-042", ["20240429"]],
           ["sub-048", ["20240512"]],
           ["sub-051", ["20240503"]],
           ["sub-057", ["20240513"]],
           ["sub-061", ["20240515"]],
           ["sub-062", ["20240508"]],
           ["sub-109", ["20240824"]],  
]


## directories of subjects and sessions for input and output
input_parent = "/data/p_03037/LORAKS/source/"
output_parent = "/data/p_03037/LORAKS/source/"
name_storage_dir = "nii_loraks_recon"   # name of the directory in the output_parent where the reconstructed data will be stored



##### different approach than specified below:
# # reconstruct everything in the input_directory, that contains one of the following patterns:
patterns_to_check = ["t1w", "pdw", "mtw", "smaps"]



## specifying names of the files to reconstruct (.dat)
## Each session has to be a nested list.
## The files are just dumped into the list, and the script will loop over the whole list.
# raw_file_list = [[  # sub-006, 20240218
#                      "meas_MID00046_smaps_kp_mtflash3d_v1s_20ch_20240218-132433.dat",
#                      "meas_MID00051_smaps_kp_mtflash3d_v1s_BC_20240218-132550.dat",
#                      "meas_MID00052_t1w_kp_mtflash3d_v1s_1p0_20240218-132619.dat",
#                      "meas_MID00053_smaps_kp_mtflash3d_v1s_20ch_20240218-132948.dat",
#                      "meas_MID00054_smaps_kp_mtflash3d_v1s_BC_20240218-133014.dat",
#                      "meas_MID00055_pdw_kp_mtflash3d_v1s_1p0_20240218-133041.dat",
#                      "meas_MID00056_smaps_kp_mtflash3d_v1s_20ch_20240218-133409.dat",
#                      "meas_MID00057_smaps_kp_mtflash3d_v1s_BC_20240218-133430.dat",
#                      "meas_MID00058_mtw_kp_mtflash3d_v1s_1p0_20240218-133457.dat",
#                      "meas_MID00060_smaps_kp_mtflash3d_v1s_20ch_20240218-134105.dat",
#                      "meas_MID00061_smaps_kp_mtflash3d_v1s_BC_20240218-134145.dat",
#                      "meas_MID00062_t1w_kp_mtflash3d_v1s_1p0_20240218-134212.dat",
#                  ],
#                  [  # sub-017, 20240304
#                      "meas_MID00099_smaps_kp_mtflash3d_v1s_20ch_20240304-205353.dat",
#                      "meas_MID00100_t1w_kp_mtflash3d_v1s_1p0_20240304-205412.dat",
#                      "meas_MID00101_smaps_kp_mtflash3d_v1s_20ch_20240304-205741.dat",
#                      "meas_MID00102_pdw_kp_mtflash3d_v1s_1p0_20240304-205743.dat",
#                      "meas_MID00103_smaps_kp_mtflash3d_v1s_20ch_20240304-210108.dat",
#                      "meas_MID00104_mtw_kp_mtflash3d_v1s_1p0_20240304-210109.dat",
#                  ],
#                  [  # sub-021, 20240309
#                      "meas_MID00042_smaps_kp_mtflash3d_v1s_20ch_20240309-124855.dat",
#                      "meas_MID00043_t1w_kp_mtflash3d_v1s_1p0_20240309-124914.dat",
#                      "meas_MID00044_smaps_kp_mtflash3d_v1s_20ch_20240309-125242.dat",
#                      "meas_MID00045_pdw_kp_mtflash3d_v1s_1p0_20240309-125244.dat",
#                      "meas_MID00046_smaps_kp_mtflash3d_v1s_20ch_20240309-125610.dat",
#                      "meas_MID00047_mtw_kp_mtflash3d_v1s_1p0_20240309-125611.dat",
#                  ],
#                  [  # sub-027, 20240312
#                      "meas_MID00125_smaps_kp_mtflash3d_v1s_20ch_20240312-212437.dat",
#                      "meas_MID00126_t1w_kp_mtflash3d_v1s_1p0_20240312-212457.dat",
#                      "meas_MID00127_smaps_kp_mtflash3d_v1s_20ch_20240312-212826.dat",
#                      "meas_MID00128_pdw_kp_mtflash3d_v1s_1p0_20240312-212827.dat",
#                      "meas_MID00129_smaps_kp_mtflash3d_v1s_20ch_20240312-213153.dat",
#                      "meas_MID00130_mtw_kp_mtflash3d_v1s_1p0_20240312-213155.dat",
#                  ],
#                  [  # sub-031, 20240318
#                      "meas_MID00140_smaps_kp_mtflash3d_v1s_20ch_20240318-132301.dat",
#                      "meas_MID00141_t1w_kp_mtflash3d_v1s_1p0_20240318-132320.dat",
#                      "meas_MID00142_smaps_kp_mtflash3d_v1s_20ch_20240318-132650.dat",
#                      "meas_MID00143_pdw_kp_mtflash3d_v1s_1p0_20240318-132651.dat",
#                      "meas_MID00144_smaps_kp_mtflash3d_v1s_20ch_20240318-133018.dat",
#                      "meas_MID00145_mtw_kp_mtflash3d_v1s_1p0_20240318-133020.dat",
#                  ],
# ]