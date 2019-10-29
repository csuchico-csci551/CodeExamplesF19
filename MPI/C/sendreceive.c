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
    //Send i to all processes
    for(int i=0;i<world_size;i++){
        number = i;
        MPI_Send(
        /* data         = */ &number, 
        /* count        = */ 1, 
        /* datatype     = */ MPI_INT, //Types described here: https://mpitutorial.com/tutorials/mpi-send-and-receive/
        /* destination  = */ i, 
        /* tag          = */ 0, 
        /* communicator = */ MPI_COMM_WORLD);
    }
  } 
  MPI_Recv(
    /* data         = */ &number, 
    /* count        = */ 1, 
    /* datatype     = */ MPI_INT, 
    /* source       = */ 0, 
    /* tag          = */ 0, 
    /* communicator = */ MPI_COMM_WORLD, 
    /* status       = */ MPI_STATUS_IGNORE);
  printf("Process %d received number %d from process 0\n", world_rank, number);

  



  // Finalize the MPI environment. No more MPI calls can be made after this
  MPI_Finalize();
}