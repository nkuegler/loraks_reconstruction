#!/usr/bin/env python3

## subject names and session names
## if there are multiple sessions for a subject, the session names should be in a list
sub_ses = [["15484.08", ["20241107"]],
           ["16690.98", ["20241105"]], 
           ["28392.ca", ["20241119"]], 
           ["35080.16", ["20241112"]],
           ["36623.fd", ["20241107"]], 
           ["37624.ab", ["20241119"]], 
           ["38821.00", ["20241119"]], 
           ["38971.74", ["20241112"]], 
           ["39101.51", ["20241107"]], 
           ["40181.e2", ["20241112"]]
          ]

## directories of subjects and sessions for input and output
input_parent = "/data/p_03002/data/source/"
output_parent = "/data/p_03002/data/source/"
name_storage_dir = "nii_loraks"  # name of the directory in the output_parent where the reconstructed data will be stored

with_smaps = False # boolean, specifies if sensitivity maps are also reconstructed
                   # each session file MUST have a corresponding sensitivity map file (2x length of t1w_raw, pdw_raw, mtw_raw)
                   # handled so that each specified session in sub_ses is used twice

## specifying names of the actual pdw, t1w, mtw, and ernst .dat files
## Each one has to be a nested list, where the sessions of each subject are specified in a separate list.
t1w_raw = [[  # 15484.08
              "meas_MeasUID47_t1w_kp_mtflash3d_v1s_0p6.dat",  # 20241107
           ],
           [  # 16690.98
              "meas_MeasUID61_t1w_kp_mtflash3d_v1s_0p6.dat",  # 20241105
           ],
           [  # 28392.ca 
              "meas_MeasUID139_t1w_kp_mtflash3d_v1s_0p6.dat", # 20241119
           ], 
           [  # 35080.16
              "meas_MeasUID47_t1w_kp_mtflash3d_v1s_0p6.dat",  # 20241112
           ],
           [  # 36623.fd
              "meas_MeasUID56_t1w_kp_mtflash3d_v1s_0p6.dat",  # 20241107
           ],
           [  # 37624.ab
              "meas_MeasUID93_t1w_kp_mtflash3d_v1s_0p6.dat",  # 20241119
           ],
           [  # 38821.00
              "meas_MeasUID48_t1w_kp_mtflash3d_v1s_0p6.dat",  # 20241119
           ],
           [  # 38971.74
              "meas_MeasUID79_t1w_kp_mtflash3d_v1s_0p6.dat",  # 20241112
           ],
           [  # 39101.51
              "meas_MeasUID24_t1w_kp_mtflash3d_v1s_0p6.dat",  # 20241107
           ],
           [  # 40181.e2
              "meas_MeasUID111_t1w_kp_mtflash3d_v1s_0p6.dat",  # 20241112
           ]
]

# TODO: for automatic pdw and t1w raw data selection:
# if only one -> take this
# if multiple -> error/skip
# print which skipped
   
pdw_raw = [[  # 15484.08
              "meas_MeasUID49_pdw_kp_mtflash3d_v1s_0p6.dat",  # 20241107
           ],
           [  # 16690.98
              "meas_MeasUID63_pdw_kp_mtflash3d_v1s_0p6.dat",  # 20241105
           ],
           [  # 28392.ca 
              "meas_MeasUID141_pdw_kp_mtflash3d_v1s_0p6.dat", # 20241119
           ], 
           [  # 35080.16
              "meas_MeasUID49_pdw_kp_mtflash3d_v1s_0p6.dat",  # 20241112
           ],
           [  # 36623.fd
              "meas_MeasUID63_pdw_kp_mtflash3d_v1s_0p6.dat",  # 20241107
           ],
           [  # 37624.ab
              "meas_MeasUID95_pdw_kp_mtflash3d_v1s_0p6.dat",  # 20241119
           ],
           [  # 38821.00
              "meas_MeasUID50_pdw_kp_mtflash3d_v1s_0p6.dat",  # 20241119
           ],
           [  # 38971.74
              "meas_MeasUID81_pdw_kp_mtflash3d_v1s_0p6.dat",  # 20241112
           ],
           [  # 39101.51
              "meas_MeasUID26_pdw_kp_mtflash3d_v1s_0p6.dat",  # 20241107
           ],
           [  # 40181.e2
              "meas_MeasUID113_pdw_kp_mtflash3d_v1s_0p6.dat",  # 20241112
           ]
]


# TODO: for automatic MTw raw data selection: 
# if two -> take the larger one
# if more -> error/skip
# print which skipped

mtw_raw = [[  # 15484.08
              "meas_MeasUID51_mtw_kp_mtflash3d_v1s_0p6.dat",  # 20241107
           ],
           [  # 16690.98
              "meas_MeasUID66_mtw_kp_mtflash3d_v1s_0p6.dat",  # 20241105
           ],
           [  # 28392.ca
              "meas_MeasUID144_mtw_kp_mtflash3d_v1s_0p6.dat", # 20241119
           ],
           [  # 35080.16
              "meas_MeasUID52_mtw_kp_mtflash3d_v1s_0p6.dat",  # 20241112
           ],
           [  # 36623.fd
              "meas_MeasUID61_mtw_kp_mtflash3d_v1s_0p6.dat",  # 20241107
           ],
           [  # 37624.ab
              "meas_MeasUID98_mtw_kp_mtflash3d_v1s_0p6.dat",  # 20241119
           ],
           [  # 38821.00
              "meas_MeasUID53_mtw_kp_mtflash3d_v1s_0p6.dat",  # 20241119
           ],
           [  # 38971.74
              "meas_MeasUID84_mtw_kp_mtflash3d_v1s_0p6.dat",  # 20241112
           ],
           [  # 39101.51
              "meas_MeasUID29_mtw_kp_mtflash3d_v1s_0p6.dat",  # 20241107
           ],
           [  # 40181.e2
              "meas_MeasUID116_mtw_kp_mtflash3d_v1s_0p6.dat",  # 20241112
           ]
]

ernst_raw = None