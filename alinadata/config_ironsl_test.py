#!/usr/bin/env python3

## subject names and session names
## if there are multiple sessions for a subject, the session names should be in a list
sub_ses = [["41006.a1", "20231123"],
]
            # ["35080.16", "20241112"],
            # ["36623.fd", "20241107"], 
            # ["37624.ab", "20241119"], 
            # ["38821.00", "20241119"], 
            # ["38971.74", "20241112"], 
            # ["39101.51", "20241107"], 
            # ["40181.e2", "20241112"]
            # ]

## directories of subjects and sessions for input and output
input_parent = "/data/pt_02262/bids_test/bids_folders_autom/source/"
output_parent = "/data/pt_02262/bids_test/bids_folders_autom/source/"


## names of the actual t1w, pdw, and mtw .dat files
t1w_raw = ["meas_MeasUID24_t1w_kp_mtflash3d_v1sx_0p6.dat",
]
   
pdw_raw = ["meas_MeasUID25_pdw_kp_mtflash3d_v1sx_0p6.dat",
]

mtw_raw = ["meas_MeasUID31_mtw_kp_mtflash3d_v1sx_0p6.dat"
]
