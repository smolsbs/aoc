using System;
using System.Linq;

public class Day01{
    public static void Main(){
        int Counter = 0;
        int PrevValue;
        int[] UsrInput = File.ReadLines("/storage/git-repos/aoc/CSharp/aoc/day01.in")
            .Select(r => int.Parse(r))
            .ToArray();

        // Part 1
        PrevValue = UsrInput[0];
        for(int i=1; i < UsrInput.Length; i++){
            if (UsrInput[i] > PrevValue){
                Counter++;
            }
            PrevValue = UsrInput[i];
        }
        Console.WriteLine($"Part 1: {Counter}");

        // Part 2
        Counter = 0;
        PrevValue = UsrInput[0..3].Sum();

        for(int i=1; i < (UsrInput.Length - 2); i++){
            int val = UsrInput[i..(i+3)].Sum();
            if (val > PrevValue){
                Counter++;
            }
            PrevValue = val;
        }
        Console.WriteLine($"Part 2: {Counter}");
    }
}
