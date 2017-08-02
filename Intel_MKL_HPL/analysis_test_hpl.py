#!/usr/bin/env python

import glob as glob
import natsort as natsort
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def load_HPLinpack_test(dirname=None):

    #Execution_Date and Hostname, options o label o comment=["Default",...]

    oup_list_files= natsort.humansorted(glob.glob(dirname+"/*.oup"))
    df_test=pd.DataFrame()
    hostname=''
    execution_date=''

    for oup_file in oup_list_files:
        df_aux=parse_HPLinpack(oup_file)
        df_test=df_test.append(df_aux,ignore_index=True)

    return df_test

def parse_HPLinpack(oupfile=None):
    """Getting N, NB, P, Q, Time, Gflops, Hostname, Execution_Date"""

    with open(oupfile) as fff:
        for line in fff:
            if line.startswith('WC00C2R2'):
                line_cols=line.split()
                df_aux = pd.DataFrame({ 'N' : int(line_cols[1]),
                                        'NB' : int(line_cols[2]),
                                        'P' : int(line_cols[3]),
                                        'Q' : int(line_cols[4]),
                                        'Time' : float(line_cols[5]),
                                        'Gflops' : float(line_cols[6]) },
                                      index=[0])
                break
    return df_aux

    pass


DF=load_HPLinpack_test('2017_08_02-12h_08m')
tpp=2.2*2*16*10
print (DF['Gflops'].mean(),'+/-',DF['Gflops'].std(),'Gflops')
print (DF['Gflops'].mean()/tpp,'+/-',DF['Gflops'].std()/tpp,'% Efficiency with theoretical peak performance')


# Node performance in GFlops = (CPU speed in GHz) x (number of CPU cores) x (CPU instruction per cycle) x (number of CPUs per node)
# 2.2GHz x 2 x (8x2?) x 10


