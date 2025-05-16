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
name_storage_dir = "nii_loraks_smaps"  # name of the directory in the output_parent where the reconstructed data will be stored

with_smaps = False  # boolean, specifies if sensitivity maps are also reconstructed
                   # each session file MUST have a corresponding sensitivity map file (2x length of t1w_raw, pdw_raw, mtw_raw)
                   # handled so that each specified session in sub_ses is used twice

## specifying names of the actual pdw, t1w, mtw, and ernst .dat files
## Each one has to be a nested list, where the sessions of each subject are specified in a separate list.
t1w_raw = [[  # 15484.08
              "meas_MeasUID46_smap_kp_mtflash3d_v1s_4p0.dat", # 20241107
           ],
           [  # 16690.98
              "meas_MeasUID60_smap_kp_mtflash3d_v1s_4p0.dat",  # 20241105
           ],
           [  # 28392.ca 
              "meas_MeasUID138_smap_kp_mtflash3d_v1s_4p0.dat", # 20241119
           ], 
           [  # 35080.16
              "meas_MeasUID46_smap_kp_mtflash3d_v1s_4p0.dat",  # 20241112
           ],
           [  # 36623.fd
              "meas_MeasUID55_smap_kp_mtflash3d_v1s_4p0.dat",  # 20241107
           ],
           [  # 37624.ab
              "meas_MeasUID92_smap_kp_mtflash3d_v1s_4p0.dat",  # 20241119
           ],
           [  # 38821.00
              "meas_MeasUID47_smap_kp_mtflash3d_v1s_4p0.dat", # 20241119
           ],
           [  # 38971.74
              "meas_MeasUID78_smap_kp_mtflash3d_v1s_4p0.dat",  # 20241112
           ],
           [  # 39101.51
              "meas_MeasUID23_smap_kp_mtflash3d_v1s_4p0.dat",  # 20241107
           ],
           [  # 40181.e2
              "meas_MeasUID110_smap_kp_mtflash3d_v1s_4p0.dat",  # 20241112
           ]
]

# TODO: for automatic pdw and t1w raw data selection:
# if only one -> take this
# if multiple -> error/skip
# print which skipped
   
pdw_raw = [[  # 15484.08
              "meas_MeasUID48_smap_kp_mtflash3d_v1s_4p0.dat", # 20241107
           ],
           [  # 16690.98
              "meas_MeasUID62_smap_kp_mtflash3d_v1s_4p0.dat",  # 20241105
           ],
           [  # 28392.ca 
              "meas_MeasUID140_smap_kp_mtflash3d_v1s_4p0.dat", # 20241119
           ], 
           [  # 35080.16
              "meas_MeasUID48_smap_kp_mtflash3d_v1s_4p0.dat",  # 20241112
           ],
           [  # 36623.fd
              "meas_MeasUID62_smap_kp_mtflash3d_v1s_4p0.dat",  # 20241107
           ],
           [  # 37624.ab
              "meas_MeasUID94_smap_kp_mtflash3d_v1s_4p0.dat",  # 20241119
           ],
           [  # 38821.00
              "meas_MeasUID49_smap_kp_mtflash3d_v1s_4p0.dat", # 20241119
           ],
           [  # 38971.74
              "meas_MeasUID80_smap_kp_mtflash3d_v1s_4p0.dat",  # 20241112
           ],
           [  # 39101.51
              "meas_MeasUID25_smap_kp_mtflash3d_v1s_4p0.dat",  # 20241107
           ],
           [  # 40181.e2
              "meas_MeasUID112_smap_kp_mtflash3d_v1s_4p0.dat",  # 20241112
           ]
]


# TODO: for automatic MTw raw data selection: 
# if two -> take the larger one
# if more -> error/skip
# print which skipped

mtw_raw = [[  # 15484.08
              "meas_MeasUID50_smap_kp_mtflash3d_v1s_4p0.dat", # 20241107
           ],
           [  # 16690.98
              "meas_MeasUID64_smap_kp_mtflash3d_v1s_4p0.dat",  # 20241105
           ],
           [  # 28392.ca
              "meas_MeasUID142_smap_kp_mtflash3d_v1s_4p0.dat", # 20241119
           ],
           [  # 35080.16
              "meas_MeasUID50_smap_kp_mtflash3d_v1s_4p0.dat",  # 20241112
           ],
           [  # 36623.fd
              "meas_MeasUID59_smap_kp_mtflash3d_v1s_4p0.dat",  # 20241107
           ],
           [  # 37624.ab
              "meas_MeasUID96_smap_kp_mtflash3d_v1s_4p0.dat",  # 20241119
           ],
           [  # 38821.00
              "meas_MeasUID51_smap_kp_mtflash3d_v1s_4p0.dat", # 20241119
           ],
           [  # 38971.74
              "meas_MeasUID82_smap_kp_mtflash3d_v1s_4p0.dat",  # 20241112
           ],
           [  # 39101.51
              "meas_MeasUID27_smap_kp_mtflash3d_v1s_4p0.dat",  # 20241107
           ],
           [  # 40181.e2
              "meas_MeasUID114_smap_kp_mtflash3d_v1s_4p0.dat",  # 20241112
           ]
]

ernst_raw = None

b1afi_ptx_raw = None

b1afi_stx_raw = None