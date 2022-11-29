namespace Year2015.Day19;
public class Day19
{

    public static Regex rx = new Regex(@"(\w+) \=\> (\w+)",
            RegexOptions.Compiled | RegexOptions.IgnoreCase);

    public static void Replacements(string molecule)
    {
        Console.WriteLine("no");

    }

    public static void Run(string Path)
    {
        string molecule = "";

        Dictionary<string, List<string>> switches = new Dictionary<string, List<string>>();

        foreach (string l in File.ReadAllLines(Path))
        {
            if (l == "")
                continue;
            Match a = rx.Match(l);
            if (a == Match.Empty)
            {
                molecule = l;
                continue;
            }
            var b = a.Groups;

            if (switches.ContainsKey(b[1].Value))
                switches[b[1].Value].Add(b[2].Value);
            else
                switches.Add(b[1].Value, new List<string> { b[2].Value });

        }

        Replacements(molecule);

    }
}