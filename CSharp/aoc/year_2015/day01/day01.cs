namespace Year2015.Day1;
public class Day1{
    public static void run(string Path)
    {
        string usrIn = File.ReadAllText(Path);
        int p1 = 0;
        int p2 = 0;
        bool basement = false;

        for (int i = 0; i < usrIn.Length; i++)
        {
            p1 += usrIn[i] == '(' ? 1 : -1;
            if (!basement && p1 == -1)
            {
                p2 = i + 1;
                basement = !basement;
            }
        }
        Console.WriteLine($"Part 1: {p1}\nPart 2: {p2}");

    }
}

