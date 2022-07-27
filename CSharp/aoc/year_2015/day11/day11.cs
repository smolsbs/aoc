namespace Year2015.Day11;

public class Day11
{

    readonly static char[] badChars = new char[] { 'i', 'o', 'l' };


    private static string makePw(string initialPw)
    {
        var pw = initialPw.ToCharArray();
        while (true)
        {
            int i = pw.Length - 1;

            while (i > 0)
            {
                pw[i] = (char)((pw[i] - 96) % 26 + 97);
                if (pw[i] != 'a') break;
                i--;
            }

            string aux = new string(pw);
            if (rules(aux)) return aux;
        }
    }

    private static bool rules(string password)
    {
        var pw = password;
        if (pw.Any(c => badChars.Contains(c))) return false;

        bool conseq = false;
        var pairs = new List<string>();
        for (int i = 1; i < pw.Length; i++)
        {
            var p = pw[(i - 1)..(i + 1)];
            if (p[0] == p[1] && !pairs.Contains(p))
            {
                pairs.Add(p);
            }

            if (i < 3) continue;
            if ((pw[i - 2] + 2) == pw[i] && (pw[i - 1] + 1) == pw[i]) conseq = true;
        }

        return (conseq == true && pairs.Count >= 2);
    }


    public static void Run(string password)
    {
        string p1 = "";
        string p2 = "";

        p1 = makePw(password);
        p2 = makePw(p1);

        Console.WriteLine($"Part 1: {p1}\nPart 2: {p2}");
    }
}