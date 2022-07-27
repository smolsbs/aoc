namespace Year2015.Day10;


public class Day10
{

    private static string makeNextIter(string currRun)
    {
        StringBuilder nextRun = new();
        int v = 1;
        char currChar = currRun[0];
        char lastChar = currRun[0];
        for (int j = 1; j < currRun.Length; j++)
        {
            currChar = currRun[j];
            if (currChar == lastChar) v++;
            else
            {
                nextRun.Append($"{v}{lastChar}");
                v = 1;
            }
            lastChar = currChar;
        }
        nextRun.Append($"{v}{currChar}");
        return nextRun.ToString();
    }

    public static void Run(string value, int runs = 50)
    {
        int p1 = 0;
        int p2 = 0;
        string run = value;

        for (int i = 0; i < runs; i++)
        {
            run = makeNextIter(run);

            if (i == 39) p1 = run.Length;
            if (i == 49) p2 = run.Length;
        }
        Console.WriteLine($"Part 1: {p1}\nPart 2: {p2}");
    }

}