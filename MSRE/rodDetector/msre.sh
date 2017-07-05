#!/bin/bash
#PBS -V
#PBS -q super
#PBS -l nodes=2:ppn=48


#### Executable Line
cd ${PBS_O_WORKDIR}

module load mpi
module load serpent

mpirun -npersocket 1 sss2 -omp 12 msreU.serp | tee serpout.txt
