namespace Year2015.Day4;

public class Day4
{
    public static void run(string Path)
    {
        string secret = File.ReadAllText(Path).Trim();

        int p1 = 0;
        int p2 = 0;
        var hasher = MD5.Create();
        int i = 0;
        byte[] toHash = new byte[20];
        string hashed;

        while (p1 == 0 || p2 == 0)
        {
            toHash = $"{secret}{i}".Select(c => (byte)c).ToArray();
            hashed = BitConverter.ToString(hasher.ComputeHash(toHash)).Replace("-", "");
            if (p1 == 0 && hashed.Substring(0, 5) == "00000")
            {
                Console.WriteLine($"Found p1: {hashed}");
                p1 = i;
            }
            if (p2 == 0 && hashed.Substring(0, 6) == "000000")
            {
                Console.WriteLine($"Found p2: {hashed}");
                p2 = i;
            }
            i++;
        }
        Console.WriteLine($"Part 1: {p1}\nPart 2: {p2}");
    }
}