#!/bin/bash

## INPUT VARS

NUM_ITERS=50
HLP_EXE=/opt/intel/mkl/benchmarks/mp_linpack/xhpl_intel64_static
DIM_HLP=80000

## RUNNING TESTS

OUT_DIR=`date +%Y_%m_%d-%Hh_%mm`
mkdir test_$OUT_DIR

COUNTER=0

while [  $COUNTER -lt $NUM_ITERS ]; do
 	  echo 'Doing the test ' $COUNTER
 	  $HLP_EXE -n $DIM_HLP -q 1 -p 1 > $COUNTER.log
 	  cp HPL.out $COUNTER.oup
    mv $COUNTER.* $OUT_DIR/.
    let COUNTER=COUNTER+1
done

echo '... Finish at $(date +%Y_%m_%d-%Hh_%mm)'
