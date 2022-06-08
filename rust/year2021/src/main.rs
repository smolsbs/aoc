use std::fs;
use std::io::prelude::*;
use std::io::BufReader;


fn day01(path: &str){
    let fp = fs::File::open(path).expect("Not a valid file.");
    let buf = BufReader::new(fp);
    let mut usr_in: Vec<i32> = buf.lines()
                                .map(|x| x.unwrap().parse::<i32>().unwrap())
                                .collect();

    
}



fn main(){
    println!("Hello world!");
}