#!/usr/bin/env python3

## subject names and session names
## if there are multiple sessions for a subject, the session names should be in a list
sub_ses = [["42904.6b", ["20250306"]],
           ["38602.43", ["20250306"]], 
           ["42797.b0", ["20250220"]], 
           ["36529.33", ["20250227"]],
           ["41113.bf", ["20250313"]], 
           ["42145.e4", ["20250320"]], 
           ["42608.dc", ["20250306"]], 
           ["40803.29", ["20250327"]]
          ]

## directories of subjects and sessions for input and output
input_parent = "/data/p_03002/data/source/"
output_parent = "/data/p_03002/data/source/"
name_storage_dir = "nii_loraks"  # name of the directory in the output_parent where the reconstructed data will be stored

with_smaps = True # boolean, specifies if sensitivity maps are also reconstructed
                  # each session file MUST have a corresponding sensitivity map file (2x length of t1w_raw, pdw_raw, mtw_raw)
                  # handled so that each specified session in sub_ses is used twice

## specifying names of the actual pdw, t1w, mtw, and ernst .dat files
## Each one has to be a nested list, where the sessions of each subject are specified in a separate list.
t1w_raw =  [[  # 42904.6b
               "meas_MeasUID108_smap_kp_mtflash3d_v1s_4p0.dat",  # 20250306
               "meas_MeasUID109_t1w_kp_mtflash3d_v1s_0p6.dat",  # 20250306
            ],
            [  # 38602.43
               "meas_MeasUID71_smap_kp_mtflash3d_v1s_4p0.dat",  # 20250306
               "meas_MeasUID72_t1w_kp_mtflash3d_v1s_0p6.dat",  # 20250306
            ],
            [  # 42797.b0
               "meas_MeasUID80_smap_kp_mtflash3d_v1s_4p0.dat", # 20250220
               "meas_MeasUID81_t1w_kp_mtflash3d_v1s_0p6.dat", # 20250220
            ], 
            [  # 36529.33
               "meas_MeasUID43_smap_kp_mtflash3d_v1s_4p0.dat",  # 20250227
               "meas_MeasUID44_t1w_kp_mtflash3d_v1s_0p6.dat",  # 20250227
            ],
            [  # 41113.bf
               "meas_MeasUID55_smap_kp_mtflash3d_v1s_4p0.dat",  # 20250313
               "meas_MeasUID56_t1w_kp_mtflash3d_v1s_0p6.dat",  # 20250313
            ],
            [  # 42145.e4
               "meas_MeasUID49_smap_kp_mtflash3d_v1s_4p0.dat",  # 20250320
               "meas_MeasUID50_t1w_kp_mtflash3d_v1s_0p6.dat",  # 20250320
            ],
            [  # 42608.dc
               "meas_MeasUID42_smap_kp_mtflash3d_v1s_4p0.dat",  # 20250306
               "meas_MeasUID43_t1w_kp_mtflash3d_v1s_0p6.dat",  # 20250306
            ],
            [  # 40803.29
               "meas_MeasUID42_smap_kp_mtflash3d_v1s_4p0.dat",  # 20250327
               "meas_MeasUID43_t1w_kp_mtflash3d_v1s_0p6.dat",  # 20250327
            ]
]

# TODO: for automatic pdw and t1w raw data selection:
# if only one -> take this
# if multiple -> error/skip
# print which skipped

pdw_raw =  [[  # 42904.6b
               "meas_MeasUID102_smap_kp_mtflash3d_v1s_4p0.dat",  # 20250306
               "meas_MeasUID103_pdw_kp_mtflash3d_v1s_0p6.dat",  # 20250306
            ],
            [  # 38602.43
               "meas_MeasUID73_smap_kp_mtflash3d_v1s_4p0.dat",  # 20250306
               "meas_MeasUID74_pdw_kp_mtflash3d_v1s_0p6.dat",  # 20250306
            ],
            [  # 42797.b0
               "meas_MeasUID82_smap_kp_mtflash3d_v1s_4p0.dat", # 20250220
               "meas_MeasUID83_pdw_kp_mtflash3d_v1s_0p6.dat", # 20250220
            ], 
            [  # 36529.33
               "meas_MeasUID45_smap_kp_mtflash3d_v1s_4p0.dat",  # 20250227
               "meas_MeasUID46_pdw_kp_mtflash3d_v1s_0p6.dat",  # 20250227
            ],
            [  # 41113.bf
               "meas_MeasUID49_smap_kp_mtflash3d_v1s_4p0.dat",  # 20250313
               "meas_MeasUID50_pdw_kp_mtflash3d_v1s_0p6.dat",  # 20250313
            ],
            [  # 42145.e4
               "meas_MeasUID51_smap_kp_mtflash3d_v1s_4p0.dat",  # 20250320
               "meas_MeasUID52_pdw_kp_mtflash3d_v1s_0p6.dat",  # 20250320
            ],
            [  # 42608.dc
               "meas_MeasUID44_smap_kp_mtflash3d_v1s_4p0.dat",  # 20250306
               "meas_MeasUID45_pdw_kp_mtflash3d_v1s_0p6.dat",  # 20250306
            ],
            [  # 40803.29
               "meas_MeasUID44_smap_kp_mtflash3d_v1s_4p0.dat",  # 20250327
               "meas_MeasUID45_pdw_kp_mtflash3d_v1s_0p6.dat",  # 20250327
            ]
]


# TODO: for automatic MTw raw data selection: 
# if two -> take the larger one
# if more -> error/skip
# print which skipped

mtw_raw =  [[  # 42904.6b
               "meas_MeasUID104_smap_kp_mtflash3d_v1s_4p0.dat",  # 20250306
               "meas_MeasUID106_mtw_kp_mtflash3d_v1s_0p6.dat",  # 20250306
            ],
            [  # 38602.43
               "meas_MeasUID75_smap_kp_mtflash3d_v1s_4p0.dat",  # 20250306
               "meas_MeasUID78_mtw_kp_mtflash3d_v1s_0p6.dat",  # 20250306
            ],
            [  # 42797.b0
               "meas_MeasUID84_smap_kp_mtflash3d_v1s_4p0.dat", # 20250220
               "meas_MeasUID86_mtw_kp_mtflash3d_v1s_0p6.dat", # 20250220
            ], 
            [  # 36529.33
               "meas_MeasUID47_smap_kp_mtflash3d_v1s_4p0.dat",  # 20250227
               "meas_MeasUID49_mtw_kp_mtflash3d_v1s_0p6.dat",  # 20250227
            ],
            [  # 41113.bf
               "meas_MeasUID51_smap_kp_mtflash3d_v1s_4p0.dat",  # 20250313
               "meas_MeasUID53_mtw_kp_mtflash3d_v1s_0p6.dat",  # 20250313
            ],
            [  # 42145.e4
               "meas_MeasUID53_smap_kp_mtflash3d_v1s_4p0.dat",  # 20250320
               "meas_MeasUID55_mtw_kp_mtflash3d_v1s_0p6.dat",  # 20250320
            ],
            [  # 42608.dc
               "meas_MeasUID46_smap_kp_mtflash3d_v1s_4p0.dat",  # 20250306
               "meas_MeasUID49_mtw_kp_mtflash3d_v1s_0p6.dat",  # 20250306
            ],
            [  # 40803.29
               "meas_MeasUID46_smap_kp_mtflash3d_v1s_4p0.dat",  # 20250327
               "meas_MeasUID48_mtw_kp_mtflash3d_v1s_0p6.dat",  # 20250327
            ]
]

ernst_raw = None