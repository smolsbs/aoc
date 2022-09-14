namespace Year2015.Day18;

public class Day18
{
    private static int MSIZE = 100;

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
        Console.WriteLine(line);
    }

    private static int GetOnValues(int[] grid)
    {
        return grid.Count(v => v == 1);
    }

    private static int DoWhat(int[] grid, (int, int) idx)
    {
        (int r, int c) = idx;
        int val = GetNeighbours(grid, idx);
        int state = grid[r * MSIZE + c];
        switch (state)
        {
            case 1:
                if (val == 2 || val == 3)
                    return 1;
                else
                    return 0;
            default:
                if (val == 3)
                    return 1;
                else
                    return 0;
        }
    }

    private static (int[], int[]) Step(int[] grid, int[] grid2)
    {
        int[] statesP1 = new int[(MSIZE * MSIZE)];
        int[] statesP2 = new int[(MSIZE * MSIZE)];
        for (int i = 0; i < MSIZE; i++)
        {
            for (int j = 0; j < MSIZE; j++)
            {
                statesP1[i * MSIZE + j] = DoWhat(grid, (i, j));
                statesP2[i * MSIZE + j] = DoWhat(grid2, (i, j));

            }
        }

        statesP2[0] = 1;
        statesP2[MSIZE - 1] = 1;
        statesP2[(MSIZE - 1) * MSIZE] = 1;
        statesP2[(MSIZE - 1) * MSIZE + MSIZE - 1] = 1;

        return (statesP1, statesP2);
    }

    private static int GetNeighbours(int[] grid, (int, int) idx)
    {
        (int r, int c) = idx;
        int sum = 0;
        for (int i = Math.Max(0, r - 1); i <= Math.Min(MSIZE - 1, r + 1); i++)
        {
            for (int j = Math.Max(0, c - 1); j <= Math.Min(MSIZE - 1, c + 1); j++)
            {
                if ((i, j) == (r, c))
                    continue;
                sum += grid[i * MSIZE + j];
            }
        }
        return sum;
    }

    public static void Run(string Path)
    {
        int[] usrIn = new int[(MSIZE * MSIZE)];
        int[] usrIn2 = new int[(MSIZE * MSIZE)];

        int i = 0;
        foreach (string line in File.ReadAllLines(Path))
            foreach (char c in line)
            {
                usrIn[i] = c == '#' ? 1 : 0;
                i++;
            }

        usrIn.CopyTo(usrIn2, 0);
        usrIn2[0] = 1;
        usrIn2[MSIZE - 1] = 1;
        usrIn2[(MSIZE - 1) * MSIZE] = 1;
        usrIn2[(MSIZE - 1) * MSIZE + MSIZE - 1] = 1;

        for (int step = 0; step < 100; step++)
        {
            (usrIn, usrIn2) = Step(usrIn, usrIn2);

        }

        int p1 = GetOnValues(usrIn);
        int p2 = GetOnValues(usrIn2);

        Console.WriteLine($"Part 1: {p1}\nPart 2: {p2}");

    }


}