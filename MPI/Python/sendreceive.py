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
    for i in range(size):
        comm.send(i, dest=i, tag=0)

data = comm.recv(source=0, tag=0)
sys.stdout.write(
    "Process %d received number %d from process 0\n"
    % (rank, data))