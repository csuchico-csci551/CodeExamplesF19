extern crate mpi;
extern crate rand;

use mpi::datatype::Partition;
use mpi::traits::*;
use mpi::Count;
use std::env;

use rand::distributions::{Distribution, Uniform};

//Useful docs: https://bsteinb.github.io/rsmpi/mpi/point_to_point/trait.Source.html#method.receive
fn main() {
    let args: Vec<String> = env::args().collect();
    let num = &args[1];
    let num_elements: i32 = match num.parse() {
        Ok(n) => {
            n
        },
        Err(_) => {
            eprintln!("error: first argument not an integer");
            return;
        },
    };
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

    let mut x = vec![0; num_elements as usize];
    if rank == root_rank {
        let mut rng = rand::thread_rng();
        let generator = Uniform::from(0..10);
        let mut v: Vec<i32> = Vec::new();
        let v_size = num_elements*size;
        for _n in 0..v_size {
            v.push(generator.sample(&mut rng));
        }
        // println!("{:?}",v);
        let counts: Vec<Count> = vec![num_elements; size as usize];
        let displs: Vec<Count> = counts
            .iter()
            .scan(0, |acc, &x| {
                let tmp = *acc;
                *acc += x;
                Some(tmp)
            })
            .collect();
        let partition = Partition::new(&v[..], counts, &displs[..]);
        println!("Displs: {:?}",displs);
        root_process.scatter_varcount_into_root(&partition, &mut x[..]);
    } else {
        root_process.scatter_varcount_into(&mut x[..]);
    }
    println!(
        "Process {} received number {:?} from process 0",
        rank, x
    );
}