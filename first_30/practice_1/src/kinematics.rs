// Module: kinematics
// Called from main.rs via kinematics::run()

pub fn run() {
    let velocity = 10.0; // m/s
    let time = 5.0; // s
    let distance = velocity * time;
    println!("v = {} m/s, t = {} s -> d = {} m", velocity, time, distance);
}
