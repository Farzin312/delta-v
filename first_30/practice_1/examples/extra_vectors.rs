// Approach 2: Examples
// Another standalone file, completely independent
// Run with: cargo run --example extra_vectors

fn main() {
    let a = (3.0, 4.0);
    let b = (1.0, 2.0);
    let dot = a.0 * b.0 + a.1 * b.1;
    println!(
        "dot product of ({},{}) and ({},{}) = {}",
        a.0, a.1, b.0, b.1, dot
    );
}
