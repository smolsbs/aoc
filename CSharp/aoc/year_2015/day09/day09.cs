namespace Year2015.Day9;

public class Day9
{
    public static void run(string Path)
    {
        string[] usrIn = File.ReadAllLines(Path).ToArray();
        int p1 = 0;
        int p2 = 0;

        List<City> citiesList = new();

        TextParser<(string inCity, string outCity, int dist)> parser =
            (from City1 in Character.Letter.AtLeastOnce()
             from _ in Span.EqualTo(" to ")
             from City2 in Character.Letter.AtLeastOnce()
             from __ in Span.EqualTo(" = ")
             from distance in Character.Digit.AtLeastOnce()
             select (new string(City1), new String(City2), int.Parse(distance))
            );

        foreach (string line in usrIn)
        {
            var (inCity, outCity, dist) = parser.Parse(line);
            var curCity = citiesList.FirstOrDefault(c => c.name == inCity);

            if (curCity == null)
            {
                curCity = new City(inCity);
                citiesList.Add(curCity);
            }
            var newCity = citiesList.FirstOrDefault(c => c.name == outCity);
            if (newCity == null)
            {
                newCity = new City(outCity);
                citiesList.Add(newCity);
            }
            curCity.addCity(newCity, dist);

        }

        (p1, p2) = City.FindMinMax(citiesList);


        Console.WriteLine($"Part 1: {p1}\nPart 2: {p2}");
    }
}


