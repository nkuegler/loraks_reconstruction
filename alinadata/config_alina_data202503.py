#!/usr/bin/env python3

## subject names and session names
## if there are multiple sessions for a subject, the session names should be in a list
sub_ses = [["42298.19", ["20250123"]],
           ["34296.e8", ["20250123"]], 
           ["39984.42", ["20250123"]], 
           ["39963.1e", ["20250130"]],
           ["41745.53", ["20250130"]], 
           ["42750.18", ["20250206"]], 
           ["40562.de", ["20250130"]], 
           ["35516.ae", ["20250206"]], 
           ["40748.9f", ["20250206"]], 
           ["35184.ab", ["20250220"]],
           ["42268.22", ["20250213"]],
           ["42318.d5", ["20250220"]],
           ["40108.fb", ["20250213"]]
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
t1w_raw =  [[  # 42298.19
               "meas_MeasUID42_smap_kp_mtflash3d_v1s_4p0.dat",  # 20250123
               "meas_MeasUID43_t1w_kp_mtflash3d_v1s_0p6.dat",  # 20250123
            ],
            [  # 34296.e8
               "meas_MeasUID76_smap_kp_mtflash3d_v1s_4p0.dat",  # 20250123
               "meas_MeasUID77_t1w_kp_mtflash3d_v1s_0p6.dat",  # 20250123
            ],
            [  # 39984.42 
               "meas_MeasUID106_smap_kp_mtflash3d_v1s_4p0.dat", # 20250123
               "meas_MeasUID107_t1w_kp_mtflash3d_v1s_0p6.dat", # 20250123
            ], 
            [  # 39963.1e
               "",  # 20250130
               "",  # 20250130
            ],
            [  # 41745.53
               "",  # 20250130
               "",  # 20250130
            ],
            [  # 42750.18
               "meas_MeasUID73_smap_kp_mtflash3d_v1s_4p0.dat",  # 20250206
               "meas_MeasUID74_t1w_kp_mtflash3d_v1s_0p6.dat",  # 20250206
            ],
            [  # 40562.de
               "",  # 20250130
               "",  # 20250130
            ],
            [  # 35516.ae
               "meas_MeasUID107_smap_kp_mtflash3d_v1s_4p0.dat",  # 20250206
               "meas_MeasUID108_t1w_kp_mtflash3d_v1s_0p6.dat",  # 20250206
            ],
            [  # 40748.9f
                "meas_MeasUID43_smap_kp_mtflash3d_v1s_4p0.dat",  # 20250206
                "meas_MeasUID44_t1w_kp_mtflash3d_v1s_0p6.dat",  # 20250206
            ],
            [  # 35184.ab
                "",  # 20250220
                "",  # 20250220
            ],
            [  # 42268.22
                "meas_MeasUID44_smap_kp_mtflash3d_v1s_4p0.dat",  # 20250213
                "meas_MeasUID45_t1w_kp_mtflash3d_v1s_0p6.dat",  # 20250213
            ],
            [  # 42318.d5
                "meas_MeasUID51_smap_kp_mtflash3d_v1s_4p0.dat",  # 20250220
                "meas_MeasUID52_t1w_kp_mtflash3d_v1s_0p6.dat",  # 20250220
            ],
            [  # 40108.fb
                "meas_MeasUID82_smap_kp_mtflash3d_v1s_4p0.dat",  # 20250213
                "meas_MeasUID83_t1w_kp_mtflash3d_v1s_0p6.dat",  # 20250213
            ]
]

# TODO: for automatic pdw and t1w raw data selection:
# if only one -> take this
# if multiple -> error/skip
# print which skipped
   
pdw_raw =  [[  # 42298.19
               "meas_MeasUID44_smap_kp_mtflash3d_v1s_4p0.dat",  # 20250123
               "meas_MeasUID45_pdw_kp_mtflash3d_v1s_0p6.dat",  # 20250123
            ],
            [  # 34296.e8
               "meas_MeasUID78_smap_kp_mtflash3d_v1s_4p0.dat", # 20250123
               "meas_MeasUID79_pdw_kp_mtflash3d_v1s_0p6.dat",  # 20250123
            ],
            [  # 39984.42 
               "meas_MeasUID108_smap_kp_mtflash3d_v1s_4p0.dat", # 20250123
               "meas_MeasUID109_pdw_kp_mtflash3d_v1s_0p6.dat", # 20250123
            ], 
            [  # 39963.1e
               "",  # 20250130
               "",  # 20250130
            ],
            [  # 41745.53
               "",  # 20250130
               "",  # 20250130
            ],
            [  # 42750.18
               "meas_MeasUID75_smap_kp_mtflash3d_v1s_4p0.dat",  # 20250206
               "meas_MeasUID76_pdw_kp_mtflash3d_v1s_0p6.dat",  # 20250206
            ],
            [  # 40562.de
               "",  # 20250130
               "",  # 20250130
            ],
            [  # 35516.ae
               "meas_MeasUID109_smap_kp_mtflash3d_v1s_4p0.dat",  # 20250206
               "meas_MeasUID110_pdw_kp_mtflash3d_v1s_0p6.dat",  # 20250206
            ],
            [  # 40748.9f
                "meas_MeasUID45_smap_kp_mtflash3d_v1s_4p0.dat",  # 20250206
                "meas_MeasUID46_pdw_kp_mtflash3d_v1s_0p6.dat",  # 20250206
            ],
            [  # 35184.ab
                "",  # 20250220
                "",  # 20250220
            ],
            [  # 42268.22
                "meas_MeasUID57_smap_kp_mtflash3d_v1s_4p0.dat",  # 20250213
                "meas_MeasUID58_pdw_kp_mtflash3d_v1s_0p6.dat",  # 20250213
            ],
            [  # 42318.d5
                "meas_MeasUID53_smap_kp_mtflash3d_v1s_4p0.dat",  # 20250220
                "meas_MeasUID54_pdw_kp_mtflash3d_v1s_0p6.dat",  # 20250220
            ],
            [  # 40108.fb
                "meas_MeasUID84_smap_kp_mtflash3d_v1s_4p0.dat",  # 20250213
                "meas_MeasUID85_pdw_kp_mtflash3d_v1s_0p6.dat",  # 20250213
            ]
]


# TODO: for automatic MTw raw data selection: 
# if two -> take the larger one
# if more -> error/skip
# print which skipped

mtw_raw =  [[  # 42298.19
               "meas_MeasUID46_smap_kp_mtflash3d_v1s_4p0.dat",  # 20250123
               "meas_MeasUID48_mtw_kp_mtflash3d_v1s_0p6.dat",  # 20250123
            ],
            [  # 34296.e8
               "meas_MeasUID80_smap_kp_mtflash3d_v1s_4p0.dat",  # 20250123
               "meas_MeasUID82_mtw_kp_mtflash3d_v1s_0p6.dat",  # 20250123
            ],
            [  # 39984.42 
               "meas_MeasUID118_smap_kp_mtflash3d_v1s_4p0.dat", # 20250123
               "meas_MeasUID119_mtw_kp_mtflash3d_v1s_0p6.dat", # 20250123
            ], 
            [  # 39963.1e
               "",  # 20250130
               "",  # 20250130
            ],
            [  # 41745.53
               "",  # 20250130
               "",  # 20250130
            ],
            [  # 42750.18
               "meas_MeasUID77_smap_kp_mtflash3d_v1s_4p0.dat",  # 20250206
               "meas_MeasUID81_mtw_kp_mtflash3d_v1s_0p6.dat",  # 20250206
            ],
            [  # 40562.de
               "",  # 20250130
               "",  # 20250130
            ],
            [  # 35516.ae
               "meas_MeasUID111_smap_kp_mtflash3d_v1s_4p0.dat",  # 20250206
               "meas_MeasUID113_mtw_kp_mtflash3d_v1s_0p6.dat",  # 20250206
            ],
            [  # 40748.9f
                "meas_MeasUID47_smap_kp_mtflash3d_v1s_4p0.dat",  # 20250206
                "meas_MeasUID49_mtw_kp_mtflash3d_v1s_0p6.dat", # 20250206
            ],
            [  # 35184.ab
                "",  # 20250220
                "",  # 20250220
            ],
            [  # 42268.22
                "meas_MeasUID48_smap_kp_mtflash3d_v1s_4p0.dat",  # 20250213
                "meas_MeasUID56_mtw_kp_mtflash3d_v1s_0p6.dat",  # 20250213
            ],
            [  # 42318.d5
                "meas_MeasUID55_smap_kp_mtflash3d_v1s_4p0.dat",  # 20250220
                "meas_MeasUID57_mtw_kp_mtflash3d_v1s_0p6.dat",  # 20250220
            ],
            [  # 40108.fb
                "meas_MeasUID86_smap_kp_mtflash3d_v1s_4p0.dat",  # 20250213
                "meas_MeasUID89_mtw_kp_mtflash3d_v1s_0p6.dat",  # 20250213
            ]
]

ernst_raw = None