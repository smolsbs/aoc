namespace Year2015.Day16;



public class Day16
{

    private static Dictionary<string, int> realSue = new Dictionary<string, int> { { "children", 3 }, { "cats", 7 }, { "samoyeds", 2 }, { "pomeranians", 3 }, { "akitas", 0 }, { "vizslas", 0 }, { "goldfish", 5 }, { "trees", 3 }, { "cars", 2 }, { "perfumes", 1 } };

    public static void Run(string Path)
    {
        string[] asf = File.ReadAllLines(Path).ToArray();
        int p1 = 0;
        int p2 = 0;

        foreach (string l in asf)
        {
            // Sue 88 trees 1 samoyeds 1 goldfish 0
            var aux = l.Replace(":", "").Replace(",", "").Split(" ");
            int sueNum = int.Parse(aux[1]);

            bool realP1 = true;
            bool realP2 = true;

            for (int i = 2; i < aux.Length; i += 2)
            {
                if (!realP1 && !realP2)
                    break;

                string compound = aux[i];
                int compoundVal = int.Parse(aux[(i + 1)]);

                if (compoundVal != realSue[compound])
                {
                    realP1 = false;
                    realP2 = false;
                }

                // p2 specific checks
                if (compound == "cats" || compound == "trees")
                    realP2 = compoundVal > realSue[compound] ? true : false;
                if (compound == "pomeranians" || compound == "goldfish")
                    realP2 = compoundVal < realSue[compound] ? true : false;

            }
            if (realP1 == true)
                p1 = sueNum;

            if (realP2 == true)
                p2 = sueNum;
        }
        Console.WriteLine($"Part 1: {p1}\nPart 2: {p2}");
    }

}