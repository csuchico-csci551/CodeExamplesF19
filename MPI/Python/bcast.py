"""
Parallel Hello World
https://github.com/erdc/mpi4py/blob/master/demo/helloworld.py
"""

from mpi4py import MPI
import sys

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

if rank == 0:
    data = 1
else:
    data = None
data = comm.bcast(data, root=0)

sys.stdout.write(
    "Process %d received number %d from process 0\n"
    % (rank, data))