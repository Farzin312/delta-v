// Approach 2: Examples
// Fully independent standalone files
// Each has its own fn main()
// Run with: cargo run --example extra_kinematics

fn main() {
    let g = 9.81; // m/s^2
    let t = 3.0; // s
    let drop_distance = 0.5 * g * t * t;
    println!("Free fall: t = {}s -> d = {:.2} m", t, drop_distance);
}
