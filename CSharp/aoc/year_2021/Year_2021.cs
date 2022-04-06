using System;
using System.Linq;
using System.Collections.Generic;

namespace Year2021;
public class y_2021{
    
    public static void Day_1(string Path){
        int Counter = 0;
        int PrevValue;
        int[] UsrInput = File.ReadLines(Path)
            .Select(r => int.Parse(r))
            .ToArray();

        // Part 1
        for(int i=1; i < UsrInput.Length; i++){
            if (UsrInput[i] > UsrInput[i-1]){
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

    public static void Day_2(String Path){
        Dictionary<string,int> Values = new Dictionary<string, int>();
        Values.Add("depth", 0);
        Values.Add("depth2", 0);
        Values.Add("horizpos",0);
        Values.Add("aim", 0);

        IEnumerable<string> UsrInput = File.ReadLines(Path);

        foreach (var line in UsrInput){
            string[] Aux = line.Split(' ');
            int val = int.Parse(Aux[1]);

            switch (Aux[0])
            {
                case "down":
                    Values["depth"] += val;
                    Values["aim"] += val;
                    break;
                
                case "up":
                    Values["depth"] -= val;
                    Values["aim"] -= val;
                    break;

                case "forward":
                    Values["horizpos"] += val;
                    Values["depth2"] += (Values["aim"] * val);
                    break;

                default:
                    break;
            }
            
        }
        
        int Part1 = Values["depth"]*Values["horizpos"];
        int Part2 = Values["depth2"]*Values["horizpos"];

        Console.WriteLine($"Part 1: {Part1}\nPart 2: {Part2}");

    }

}

