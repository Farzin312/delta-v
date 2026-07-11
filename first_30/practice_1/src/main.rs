// Approach 1: Modules
// main.rs is the single entry point
// other files are modules that get wired in here

mod kinematics;
mod vectors;

fn main() {
    println!("=== Practice 1: Physics Basics ===\n");

    println!("[Kinematics]");
    kinematics::run();

    println!("\n[Vectors]");
    vectors::run();
}
