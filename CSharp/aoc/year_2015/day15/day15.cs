namespace Year2015.Day15;

public class Day15
{
    public static void Run(string Path)
    {
        int p1;
        int p2;
        string[] usrIn = File.ReadAllLines(Path).ToArray();
        List<Ingredient> ingredients = new();

        foreach (string line in usrIn)
        {
            string[] a = line.Replace(",", "").Replace(":", "").Split(' ').ToArray();
            ingredients.Add(new Ingredient(a));
        }

        (p1, p2) = Maximize(ingredients);
        Console.WriteLine($"Part 1: {p1}\nPart 2: {p2}");


    }

    private static (int, int) Maximize(List<Ingredient> ing)
    {
        int bestCookie = int.MinValue;
        int bestDietCookie = int.MinValue;

        for (int a = 100; a > 0; a--)
        {
            for (int b = 100 - a; b > 0; b--)
            {
                for (int c = 100 - a - b; c > 0; c--)
                {
                    for (int d = 100 - a - b - c; d > 0; d--)
                    {
                        int capSum = Math.Max(ing[0].Cap * a + ing[1].Cap * b + ing[2].Cap * c + ing[3].Cap * d, 0);
                        int durSum = Math.Max(ing[0].Dur * a + ing[1].Dur * b + ing[2].Dur * c + ing[3].Dur * d, 0);
                        int flaSum = Math.Max(ing[0].Fla * a + ing[1].Fla * b + ing[2].Fla * c + ing[3].Fla * d, 0);
                        int texSum = Math.Max(ing[0].Tex * a + ing[1].Tex * b + ing[2].Tex * c + ing[3].Tex * d, 0);
                        int calSum = Math.Max(ing[0].Cal * a + ing[1].Cal * b + ing[2].Cal * c + ing[3].Cal * d, 0);
                        int totalSum = capSum * durSum * flaSum * texSum;

                        if (totalSum > bestCookie)
                            bestCookie = totalSum;

                        if (calSum == 500 && totalSum > bestDietCookie)
                            bestDietCookie = totalSum;

                    }
                }
            }
        }
        return (bestCookie, bestDietCookie);
    }

}


public class Ingredient
{
    public string Name;
    public int Cap;
    public int Dur;
    public int Fla;
    public int Tex;
    public int Cal;

    public Ingredient(string[] splitLine)
    {
        Name = splitLine[0];
        Cap = int.Parse(splitLine[2]);
        Dur = int.Parse(splitLine[4]);
        Fla = int.Parse(splitLine[6]);
        Tex = int.Parse(splitLine[8]);
        Cal = int.Parse(splitLine[10]);
    }

}