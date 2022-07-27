namespace Year2015.Day3;

public class Day3
{
    private static (int, int) GetMovement(char c, int x, int y)
    {
        return c switch
        {
            '>' => (x + 1, y),
            '<' => (x - 1, y),
            '^' => (x, y + 1),
            'v' => (x, y - 1),
            _ => (x, y)
        };
    }

    public static void run(string Path)
    {
        string usrIn = File.ReadAllText(Path);

        var (x, y) = (0, 0);
        var (sx, sy) = (0, 0);
        var (rx, ry) = (0, 0);
        var (cx, cy) = (0, 0);
        int p1 = 1;
        int p2 = 1;
        bool santaTurn = false;

        var p1Houses = new Dictionary<(int, int), int> { { (x, y), 1 } };
        var p2Houses = new Dictionary<(int, int), int> { { (x, y), 2 } };

        foreach (char c in usrIn)
        {

            // part 1
            (x, y) = GetMovement(c, x, y);
            if (!p1Houses.ContainsKey((x, y)))
            {
                p1Houses.Add((x, y), 1);
                p1++;
            }

            // part 2
            if (santaTurn)
            {
                (sx, sy) = GetMovement(c, sx, sy);
                (cx, cy) = (sx, sy);
            }
            else
            {
                (rx, ry) = GetMovement(c, rx, ry);
                (cx, cy) = (rx, ry);
            }
            santaTurn = !santaTurn;

            if (!p2Houses.ContainsKey((cx, cy)))
            {
                p2Houses.Add((cx, cy), 1);
                p2++;
            }
        }
        Console.WriteLine($"Part 1: {p1}\nPart 2: {p2}");
    }
}