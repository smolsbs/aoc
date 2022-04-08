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

            switch (Aux[0]){
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

    public static void Day_3(string Path){
        string[] usrIn = File.ReadLines(Path).Select(r => r).ToArray();
        var mid = usrIn.Length / 2;
        var max_len = usrIn[0].Length;
        string gamma = "", epsilon = "";

        var oxi = new string[usrIn.Length];
        var co2 = new string[usrIn.Length];
        usrIn.CopyTo(oxi, 0);
        usrIn.CopyTo(co2, 0);



        // part 1
        for (var i = 0; i < max_len; i++){
            var aux = usrIn.Select(v => v[i]).ToArray();
            var g = aux.Count(v => v == '1') > mid ? "1": "0";
            var e = g == "1" ? "0": "1";
            gamma += g;
            epsilon += e;

        }

        // part 2

        var (oxi_i, oxi_mid, co2_i, co2_mid) = (0, oxi.Length / 2f, 0, co2.Length / 2f );
        while (oxi.Length != 1){
            var aux = oxi.Select(v => v[oxi_i]).ToArray();
            var g = aux.Count(v => v == '1') >= oxi_mid ? '1': '0';
            oxi = oxi.Where(r => r[oxi_i] == g).ToArray();
            oxi_mid = oxi.Length / 2f;
            oxi_i++;
        }

        while (co2.Length != 1){
            var aux = co2.Select(v => v[co2_i]).ToArray();
            var e = aux.Count(v => v == '1') >= co2_mid ? '0': '1';
            co2 = co2.Where(r => r[co2_i] == e).ToArray();
            co2_mid = co2.Length / 2f;
            co2_i++;
        }

        var p1 = Convert.ToInt32(gamma, 2) * Convert.ToInt32(epsilon, 2);
        var p2 = Convert.ToInt32(oxi[0], 2) * Convert.ToInt32(co2[0], 2);
        Console.WriteLine($"Part 1: {p1}\nPart 2: {p2}");

    }

    public static void Day_4(string Path){
    
    
        Console.WriteLine("HAHAHAHA no.");
    }



}

