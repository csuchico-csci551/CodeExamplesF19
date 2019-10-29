extern crate mpi;

use mpi::traits::*;
//Useful docs: https://bsteinb.github.io/rsmpi/mpi/point_to_point/trait.Source.html#method.receive
fn main() {
    let universe = mpi::initialize().unwrap();
    let world = universe.world();
    let size = world.size();
    let rank = world.rank();

    if size < 2 {
        panic!("Size of MPI_COMM_WORLD must be greater than 2, but is {}!", size);
    }
    //adapted from example: https://github.com/bsteinb/rsmpi/blob/master/examples/broadcast.rs
    let root_rank = 0;
    let root_process = world.process_at_rank(root_rank);

    let mut x;
    if world.rank() == root_rank {
        x = 1_u64;
        println!("Root broadcasting value: {}.", x);
    } else {
        x = 0_u64;
    }
    root_process.broadcast_into(&mut x);
    println!(
        "Process {} received number {:?} from process 0\n",
        rank, x
    );
}