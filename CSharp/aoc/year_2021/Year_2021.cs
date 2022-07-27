using System;
using System.IO;
using System.Linq;
using System.Text.RegularExpressions;
using System.Collections.Generic;

namespace Year2021;

public static class y_2021
{

    public static void Day1(string Path)
    {
        int Counter = 0;
        int PrevValue;
        int[] UsrInput = File.ReadLines(Path)
            .Select(r => int.Parse(r))
            .ToArray();

        // Part 1
        for (int i = 1; i < UsrInput.Length; i++)
        {
            if (UsrInput[i] > UsrInput[i - 1])
            {
                Counter++;
            }
            PrevValue = UsrInput[i];
        }
        Console.WriteLine($"Part 1: {Counter}");

        // Part 2
        Counter = 0;
        PrevValue = UsrInput[0..3].Sum();

        for (int i = 1; i < (UsrInput.Length - 2); i++)
        {
            int val = UsrInput[i..(i + 3)].Sum();
            if (val > PrevValue)
            {
                Counter++;
            }
            PrevValue = val;
        }
        Console.WriteLine($"Part 2: {Counter}");
    }

    public static void Day2(string Path)
    {
        Dictionary<string, int> Values = new Dictionary<string, int>();
        Values.Add("depth", 0);
        Values.Add("depth2", 0);
        Values.Add("horizpos", 0);
        Values.Add("aim", 0);

        IEnumerable<string> UsrInput = File.ReadLines(Path);

        foreach (var line in UsrInput)
        {
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

        int Part1 = Values["depth"] * Values["horizpos"];
        int Part2 = Values["depth2"] * Values["horizpos"];

        Console.WriteLine($"Part 1: {Part1}\nPart 2: {Part2}");
    }

    public static void Day3(string Path)
    {
        string[] usrIn = File.ReadLines(Path).Select(r => r).ToArray();
        var mid = usrIn.Length / 2;
        var max_len = usrIn[0].Length;
        string gamma = "", epsilon = "";

        var oxi = new string[usrIn.Length];
        var co2 = new string[usrIn.Length];
        usrIn.CopyTo(oxi, 0);
        usrIn.CopyTo(co2, 0);



        // part 1
        for (var i = 0; i < max_len; i++)
        {
            var aux = usrIn.Select(v => v[i]).ToArray();
            var g = aux.Count(v => v == '1') > mid ? "1" : "0";
            var e = g == "1" ? "0" : "1";
            gamma += g;
            epsilon += e;

        }

        // part 2

        var (oxi_i, oxi_mid, co2_i, co2_mid) = (0, oxi.Length / 2f, 0, co2.Length / 2f);
        while (oxi.Length != 1)
        {
            var aux = oxi.Select(v => v[oxi_i]).ToArray();
            var g = aux.Count(v => v == '1') >= oxi_mid ? '1' : '0';
            oxi = oxi.Where(r => r[oxi_i] == g).ToArray();
            oxi_mid = oxi.Length / 2f;
            oxi_i++;
        }

        while (co2.Length != 1)
        {
            var aux = co2.Select(v => v[co2_i]).ToArray();
            var e = aux.Count(v => v == '1') >= co2_mid ? '0' : '1';
            co2 = co2.Where(r => r[co2_i] == e).ToArray();
            co2_mid = co2.Length / 2f;
            co2_i++;
        }

        var p1 = Convert.ToInt32(gamma, 2) * Convert.ToInt32(epsilon, 2);
        var p2 = Convert.ToInt32(oxi[0], 2) * Convert.ToInt32(co2[0], 2);
        Console.WriteLine($"Part 1: {p1}\nPart 2: {p2}");

    }

    private static long SimulateDay6(int[] usrIn, int days)
    {
        long[] lifetimes = new long[9];
        foreach (var p in usrIn)
        {
            lifetimes[p]++;
        }
        for (var d = 0; d < days; d++)
        {
            var heaven = lifetimes[0];
            for (var i = 1; i < 9; i++)
                lifetimes[i - 1] = lifetimes[i];
            lifetimes[6] += heaven;
            lifetimes[8] = heaven;
        }
        return lifetimes.Sum();
    }

    public static void Day6(string Path)
    {
        var usrIn = File.ReadLines(Path).First().Split(',').Select(r => int.Parse(r)).ToArray();

        long p1 = SimulateDay6(usrIn, 80);
        long p2 = SimulateDay6(usrIn, 256);

        Console.WriteLine($"Part 1: {p1}\nPart 2: {p2}");

    }

    private static int DecodeDay8(string inputs, string outputs)
    {
        string[] trueSig = new string[10];

        string[] inp = inputs.Split(new char[] { ' ' }, StringSplitOptions.RemoveEmptyEntries);
        var inptLookup = inp.ToLookup(w => w.Length);
        var outpt = outputs.Split(new char[] { ' ' }, StringSplitOptions.RemoveEmptyEntries);

        var segs5 = inptLookup[5].ToList();
        var segs6 = inptLookup[6].ToList();

        // setting up unique numbers
        trueSig[1] = inptLookup[2].First();
        trueSig[4] = inptLookup[4].First();
        trueSig[7] = inptLookup[3].First();
        trueSig[8] = inptLookup[7].First();


        // segments of length 6
        trueSig[9] = segs6.First(w => trueSig[4].IsSubsetOf(w));
        segs6.Remove(trueSig[9]);
        trueSig[0] = segs6.First(w => trueSig[1].IsSubsetOf(w));
        segs6.Remove(trueSig[0]);
        trueSig[6] = segs6.First();

        // segments of length 5
        trueSig[3] = segs5.First(w => trueSig[1].IsSubsetOf(w));
        segs5.Remove(trueSig[3]);
        trueSig[5] = segs5.First(w => w.IsSubsetOf(trueSig[6]));
        segs5.Remove(trueSig[5]);
        trueSig[2] = segs5.First();

        // find from the decoded inputs the four integer output

        var newTrueSig = trueSig.Select((sig, idx) => (sig, idx));
        var decodedOutput = outpt.Select(w => newTrueSig.First(sig => w.Match(sig.sig)).idx);

        return decodedOutput.Aggregate((a, b) => a * 10 + b);
    }

    public static void Day8(string Path)
    {
        var usrIn = File.ReadLines(Path).Select(r => r).ToArray();
        var uniques = new HashSet<int> { 2, 3, 4, 7 };
        int p1 = 0;
        int p2 = 0;

        foreach (string line in usrIn)
        {
            string[] outIn = line.Split(" | ");
            p1 += outIn[1].Split(' ').Count(w => uniques.Contains(w.Length));
            p2 += DecodeDay8(outIn[0], outIn[1]);
        }

        Console.WriteLine($"Part 1: {p1}\nPart 2: {p2}");

    }

}

public static class Utils
{
    public static bool IsSubsetOf<T>(this IEnumerable<T> value, IEnumerable<T> source)
    {
        return value.All(m => source.Contains(m));
    }

    public static bool Match(this string value1, string value2)
    {
        if (value1.Length != value2.Length)
        {
            return false;
        }

        return value1.All(c => value2.Contains(c));
    }
}

