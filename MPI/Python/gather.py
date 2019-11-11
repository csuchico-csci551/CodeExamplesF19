"""
Parallel Hello World
https://github.com/erdc/mpi4py/blob/master/demo/helloworld.py
"""

from mpi4py import MPI
from random import seed, randint
import sys

if len(sys.argv) < 2:
    print("Usage: scatter.py num_elements_per_proc ")
    quit()
num_elements_per_proc= int(sys.argv[1])

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

if size<2:
    print("Need more than 1 process")
    quit()

if rank == 0:
    data = [randint(0,10) for i in range(num_elements_per_proc*size)]
# dividing data into chunks
    chunks = [[] for _ in range(size)]
    for i, chunk in enumerate(data):
        chunks[i % size].append(chunk)
    print(chunks)
else:
    data = None
    chunks = None
data = comm.scatter(chunks, root=0)
print("Process " + str(rank) + ' received list ' + str(data) + " from process 0")

# gather results
result = comm.gather(data, root=0)
# do something with result

if comm.rank == 0:
    print("Process 0 gathered " + str(result))
else:
    result = None