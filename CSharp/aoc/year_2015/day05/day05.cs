namespace Year2015.Day5;

public class Day5
{
    [Flags]
    private enum Niceness { Def = 0, Vowel = 2, Double = 4, Bad = 8, Repeats = 16, Pair = 32 };
    private static bool d5P1(string line)
    {
        var badStrings = new List<string> { "ab", "cd", "pq", "xy" };
        var allVowels = new List<char> { 'a', 'e', 'i', 'o', 'u' };
        Niceness flags = default;
        int vowels = 0;

        for (int i = 0; i < line.Length; i++)
        {

            char c = line[i];

            if (allVowels.Contains(c)) vowels++;

            if (i < 1) continue;
            char lc = line[i - 1];
            if (badStrings.Contains($"{lc}{c}"))
            {
                flags |= Niceness.Bad;
                break;
            }
            if (lc == c) flags |= Niceness.Double;
        }
        if (flags.HasFlag(Niceness.Bad)) return false;

        if (vowels > 2) flags |= Niceness.Vowel;

        return flags.HasFlag(Niceness.Vowel | Niceness.Double);
    }

    private static bool d5P2(string line)
    {
        Niceness flags = default;
        for (int i = 0; i < line.Length; i++)
        {
            if (i < line.Length - 2)
            {
                string asdf = line[i..(i + 2)];
                if (line[(i + 2)..].Contains(asdf)) flags |= Niceness.Pair;
            }

            if (i < 2) continue;
            char llc = line[i - 2];
            char lc = line[i - 1];
            char c = line[i];

            if (llc == c) flags |= Niceness.Repeats;
        }

        return flags.HasFlag(Niceness.Repeats | Niceness.Pair);
    }

    public static void run(string Path)
    {
        string[] usrIn = File.ReadAllLines(Path).ToArray();
        int p1 = 0;
        int p2 = 0;

        foreach (string line in usrIn)
        {
            p1 += d5P1(line) == true ? 1 : 0;
            p2 += d5P2(line) == true ? 1 : 0;
        }
        Console.WriteLine($"Part 1: {p1}\nPart 2: {p2}");

    }
}