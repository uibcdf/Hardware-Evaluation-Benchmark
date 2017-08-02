

### Input Data

Threshold: -16    (In this case we don't check if the tests pass)

P and Q - the number of rows and columns in the process grid, respectively.
P*Q must be the number of MPI processes that HPL is using.
Choose P≤Q.

NB - the block size of the data distribution.
Intel Xeon Processor E26* v3/E26* v4 (codenamed Haswell or Broadwell): 192
*This is the case since Ixtlilton has Intel Xeon E5-2630 v4*

It is suggested setting Ns to use the 80% of memory 
For 64 GB: 83000 Ns
However, I get the warning: 'Page swap happend. N or NB maybe too big'.
Thereby N=80000

### Source and Additional Info:

http://www.netlib.org/benchmark/hpl/tuning.html
https://software.intel.com/en-us/mkl-linux-developer-guide-contents-of-the-intel-distribution-for-linpack-benchmark
https://software.intel.com/en-us/mkl-linux-developer-guide-configuring-parameters
https://software.intel.com/en-us/mkl-linux-developer-guide-running-the-intel-distribution-for-linpack-benchmark

