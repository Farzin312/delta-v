// Module: vectors
// Called from main.rs via vectors::run()

pub fn run() {
    let ax: f64 = 3.0;
    let ay: f64 = 4.0;
    let magnitude = (ax * ax + ay * ay).sqrt();
    println!("({}, {}) -> magnitude = {}", ax, ay, magnitude);
}
