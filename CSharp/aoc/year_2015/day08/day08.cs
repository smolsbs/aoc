namespace Year2015.Day8;

public class Day8
{
    private static int d8P1(string line)
    {   

        // ""
        int stringLit = line.Length;
        int strSize = 0;
        int i = 1;
        char c = line[1];

        while (c != '"')
        {
            switch (c)
            {
                case '\\':
                    if (line[i + 1] == 'x') i += 4;
                    else i += 2;
                    strSize++;
                    break;

                default:
                    i++;
                    strSize++;
                    break;
            }
            c = line[i];
        }
        return stringLit - strSize;
    }

    private static int d8P2(string line)
    {
        int stringLit = line.Length;
        string newString = "\"";

        foreach (char c in line)
        {
            switch (c)
            {
                case '"':
                    newString += "\\\"";
                    break;

                case '\\':
                    newString += "\\\\";
                    break;

                default:
                    newString += c;
                    break;
            }
        }
        newString += "\"";
        return newString.Length - stringLit;
    }

    public static void run(string Path)
    {
        string[] usrIn = File.ReadAllLines(Path).ToArray();


        int p1 = 0;
        int p2 = 0;

        foreach (string line in usrIn)
        {
            p1 += d8P1(line);
            p2 += d8P2(line);
        }
        Console.WriteLine($"Part 1: {p1}\nPart 2: {p2}");
    }
}