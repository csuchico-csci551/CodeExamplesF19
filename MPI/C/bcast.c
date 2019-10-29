// Initially built on example from www.mpitutorial.com
// https://github.com/wesleykendall/mpitutorial/blob/gh-pages/tutorials/mpi-send-and-receive/code/send_recv.c
#include <mpi.h>
#include <stdio.h>

int main(int argc, char** argv) {
  // Initialize the MPI environment. The two arguments to MPI Init are not
  // currently used by MPI implementations, but are there in case future
  // implementations might need the arguments.
  MPI_Init(NULL, NULL);

  // Get the number of processes
  int world_size;
  MPI_Comm_size(MPI_COMM_WORLD, &world_size);

  // Get the rank of the process
  int world_rank;
  MPI_Comm_rank(MPI_COMM_WORLD, &world_rank);

  // We are assuming at least 2 processes for this task
  if (world_size < 2) {
    fprintf(stderr, "World size must be greater than 1 for %s\n", argv[0]);
    MPI_Abort(MPI_COMM_WORLD, 1);
  }

  int number=-1;
  if (world_rank == 0) {
    //Set 1 in rank 0
    number = 1;
    
  } 
  MPI_Bcast(
    /*void* data */ &number,
    /*int count */ 1,
    /*MPI_Datatype datatype*/ MPI_INT,
    /*int root*/ 0, //Who's value/data is broadcast out
    /*MPI_Comm communicator*/MPI_COMM_WORLD);
  printf("Process %d received number %d from process 0\n", world_rank, number);

  



  // Finalize the MPI environment. No more MPI calls can be made after this
  MPI_Finalize();
}