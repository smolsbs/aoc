namespace Year2015.Day17;
using Combinatorics.Collections;

public class Day17
{
    public static void Run(string Path)
    {
        int p1 = 0;
        int p2 = 0;

        int[] containers = File.ReadAllLines(Path).Select(v => int.Parse(v)).ToArray();

        for (int i = 2; i < containers.Length + 1; i++)
        {

            var a = new Combinations<int>(containers, i);
            int b = a.Count(v => v.Sum() == 150);
            if (p2 == 0 && b != 0)
                p2 = i;
            p1 += b;

        }

        // total = 150

        Console.WriteLine($"Part 1: {p1}\nPart 2: {p2}");
    }
}