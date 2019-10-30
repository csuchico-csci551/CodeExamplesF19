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

    if rank == 0{
        for i in 0..size{
            world.process_at_rank(i).send(&i);
        }
    }
    let x = world.process_at_rank(0).receive::<i32>();
    println!(
        "Process {} received number {:?} from process 0",
        rank, x.0
    );
}