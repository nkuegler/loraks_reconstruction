#!/usr/bin/env python3

## subject names and session names
## if there are multiple sessions for a subject, the session names should be in a list
sub_ses = [["15484.08", "20241107"],
           ["16690.98", "20241105"], 
           ["28392.ca", "20241119"], 
           ["35080.16", "20241112"],
           ["36623.fd", "20241107"], 
           ["37624.ab", "20241119"], 
           ["38821.00", "20241119"], 
           ["38971.74", "20241112"], 
           ["39101.51", "20241107"], 
           ["40181.e2", "20241112"]
          ]

## directories of subjects and sessions for input and output
input_parent = "/data/pt_03002/data/source"
output_parent = "/data/pt_03002/data/source"
name_storage_dir = "nii_loraks"  # name of the directory in the output_parent where the reconstructed data will be stored


## names of the actual t1w, pdw, and mtw .dat files
t1w_raw = ["meas_MeasUID47_t1w_kp_mtflash3d_v1s_0p6.dat",       # TODO: if only one -> take this
           "meas_MeasUID61_t1w_kp_mtflash3d_v1s_0p6.dat",       # TODO: if multiple -> error/skip
           "meas_MeasUID139_t1w_kp_mtflash3d_v1s_0p6.dat",      # print which skipped
           "meas_MeasUID47_t1w_kp_mtflash3d_v1s_0p6.dat",
           "meas_MeasUID56_t1w_kp_mtflash3d_v1s_0p6.dat",
           "meas_MeasUID93_t1w_kp_mtflash3d_v1s_0p6.dat", 
           "meas_MeasUID48_t1w_kp_mtflash3d_v1s_0p6.dat", 
           "meas_MeasUID79_t1w_kp_mtflash3d_v1s_0p6.dat", 
           "meas_MeasUID24_t1w_kp_mtflash3d_v1s_0p6.dat",
           "meas_MeasUID111_t1w_kp_mtflash3d_v1s_0p6.dat"
]
   
pdw_raw = ["meas_MeasUID49_pdw_kp_mtflash3d_v1s_0p6.dat",
           "meas_MeasUID63_pdw_kp_mtflash3d_v1s_0p6.dat",
           "meas_MeasUID141_pdw_kp_mtflash3d_v1s_0p6.dat",
           "meas_MeasUID49_pdw_kp_mtflash3d_v1s_0p6.dat",
           "meas_MeasUID63_pdw_kp_mtflash3d_v1s_0p6.dat",
           "meas_MeasUID95_pdw_kp_mtflash3d_v1s_0p6.dat",
           "meas_MeasUID50_pdw_kp_mtflash3d_v1s_0p6.dat",
           "meas_MeasUID81_pdw_kp_mtflash3d_v1s_0p6.dat",
           "meas_MeasUID26_pdw_kp_mtflash3d_v1s_0p6.dat",
           "meas_MeasUID113_pdw_kp_mtflash3d_v1s_0p6.dat"
]


mtw_raw = ["meas_MeasUID51_mtw_kp_mtflash3d_v1s_0p6.dat",   # TODO: if two -> take the larger one
           "meas_MeasUID66_mtw_kp_mtflash3d_v1s_0p6.dat",   # if more -> error/skip
           "meas_MeasUID144_mtw_kp_mtflash3d_v1s_0p6.dat",  # print which skipped
           "meas_MeasUID52_mtw_kp_mtflash3d_v1s_0p6.dat",
           "meas_MeasUID61_mtw_kp_mtflash3d_v1s_0p6.dat",
           "meas_MeasUID98_mtw_kp_mtflash3d_v1s_0p6.dat",
           "meas_MeasUID53_mtw_kp_mtflash3d_v1s_0p6.dat", 
           "meas_MeasUID84_mtw_kp_mtflash3d_v1s_0p6.dat", 
           "meas_MeasUID29_mtw_kp_mtflash3d_v1s_0p6.dat",
           "meas_MeasUID116_mtw_kp_mtflash3d_v1s_0p6.dat"
]
