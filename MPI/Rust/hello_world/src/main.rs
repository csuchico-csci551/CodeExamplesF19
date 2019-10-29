extern crate mpi;

use mpi::traits::*;

fn main() {
    let universe = mpi::initialize().unwrap();
    let world = universe.world();
    let size = world.size();
    let rank = world.rank();
    let processor = mpi::environment::processor_name().unwrap();

    println!(
        "Hello world from processor {}, rank {} out of {} processors\n",
        processor, rank, size
    );
}