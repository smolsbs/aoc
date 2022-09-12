namespace Year2015.Day18;

public class Day18
{
    private static int MAX_COL = 100;
    private static int MAX_ROW = 100;

    private static void PrintGrid(int[] grid)
    {
        int i = 0;
        string line = "";
        while (i < grid.Length)
        {
            if (i != 0 && i % 6 == 0)
            {
                Console.WriteLine(line);
                line = "";
            }
            line += $"{grid[i]} ";
            i++;
        }
    }

    private static int GetOnValues(int[] grid)
    {
        return grid.Count(v => v == 1);
    }

    private static int[] Step(int[] grid, bool p2 = false)
    {
        int[] newStates = new int[(MAX_COL * MAX_ROW)];
        for (int i = 0; i < MAX_ROW; i++)
        {
            for (int j = 0; j < MAX_COL; j++)
            {
                int val = GetNeighbours(grid, (i, j));
                switch (grid[i * MAX_ROW + j])
                {
                    case 1:
                        if (val == 2 || val == 3)
                            newStates[i * MAX_ROW + j] = 1;
                        else
                            newStates[i * MAX_ROW + j] = 0;
                        break;
                    case 0:
                        if (val == 3)
                            newStates[i * MAX_ROW + j] = 1;
                        else
                            newStates[i * MAX_ROW + j] = 0;
                        break;
                }
            }
        }

        if (p2)
        {
            newStates[0] = 1;
            newStates[MAX_COL - 1] = 1;
            newStates[(MAX_ROW - 2) * MAX_ROW] = 1;
            newStates[(MAX_ROW - 1) * MAX_ROW - 1] = 1;
        }

        return newStates;
    }

    private static int GetNeighbours(int[] grid, (int, int) idx)
    {
        (int r, int c) = idx;
        int sum = 0;
        for (int i = Math.Max(0, r - 1); i <= Math.Min(MAX_ROW - 1, r + 1); i++)
        {
            for (int j = Math.Max(0, c - 1); j <= Math.Min(MAX_COL - 1, c + 1); j++)
            {
                if ((i, j) == (r, c))
                    continue;
                sum += grid[i * MAX_ROW + j];
            }
        }
        return sum;
    }

    public static void Run(string Path)
    {
        int[] usrIn = new int[(MAX_COL * MAX_ROW)];
        int[] usrIn2 = new int[(MAX_COL * MAX_ROW)];

        int i = 0;
        foreach (string line in File.ReadAllLines(Path))
            foreach (char c in line)
            {
                usrIn[i] = c == '#' ? 1 : 0;
                i++;
            }

        usrIn.CopyTo(usrIn2, 0);
        usrIn2[0] = 1;
        usrIn2[MAX_COL - 1] = 1;
        usrIn2[(MAX_ROW - 2) * MAX_ROW] = 1;
        usrIn2[(MAX_ROW - 1) * MAX_ROW - 1] = 1;

        for (int step = 0; step < 100; step++)
        {
            Step(usrIn).CopyTo(usrIn, 0);
            Step(usrIn2, true).CopyTo(usrIn2, 0);
        }

        int p1 = GetOnValues(usrIn);
        int p2 = GetOnValues(usrIn2);

        Console.WriteLine($"Part 1: {p1}\nPart 2: {p2}");

    }


}