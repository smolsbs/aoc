namespace Year2015.Day2;

public class Day2
{
    public static void run(string Path)
    {
        string[] usrIn = File.ReadLines(Path).Select(l => l).ToArray();
        int p1 = 0;
        int p2 = 0;
        int[] vals = new int[3];
        int[] areas = new int[3];

        foreach (string line in usrIn)
        {
            // l w h
            vals = line.Split('x').Select(c => int.Parse(c)).ToArray();

            areas[0] = vals[0] * vals[1];
            areas[1] = vals[1] * vals[2];
            areas[2] = vals[2] * vals[0];

            p1 += areas.Min();
            p1 += areas.Select(v => v * 2).Sum();

            p2 += (vals.Aggregate((a, b) => a * b));
            p2 += (vals.OrderBy(v => v).Take(2).Select(v => v).Sum() * 2);

        }

        Console.WriteLine($"Part 1: {p1}\nPart 2: {p2}");
    }
}