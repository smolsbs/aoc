namespace Year2015.Day14;

public class Day14
{
    static TextParser<Reindeer> parser =
        (from name in Character.Letter.AtLeastOnce()
         from _ in Span.EqualTo(" can fly ")
         from speed in Character.Digit.AtLeastOnce()
         from __ in Span.EqualTo(" km/s for ")
         from dur in Character.Digit.AtLeastOnce()
         from ___ in Span.EqualTo(" seconds, but then must rest for ")
         from rest in Character.Digit.AtLeastOnce()
         select (new Reindeer(new string(name), int.Parse(speed), int.Parse(dur), int.Parse(rest)))
        );

    private static List<Reindeer> ParseInput(string Path)
    {
        List<Reindeer> reindeers = new();
        foreach (string line in File.ReadAllLines(Path).ToArray())
            reindeers.Add(parser.Parse(line));

        return reindeers;
    }

    public static void Run(string Path, int time = 2503)
    {

        var reindeers = ParseInput(Path);
        var names = reindeers.Select(c => c.Name).ToArray();

        for (int _ = 0; _ < time; _++)
        {
            foreach (string name in names)
                reindeers.First(c => c.Name == name).Tick();

            reindeers
                .Where(v => v.Distance == reindeers.Max(x => x.Distance))
                .First()
                .Points++;
        }

        int p1 = reindeers.Max(v => v.Distance);
        int p2 = reindeers.Max(v => v.Points);

        Console.WriteLine($"Part 1: {p1}\nPart 2: {p2}");
    }
}


public class Reindeer
{
    public string Name;
    public int Speed;
    public int Duration;
    public int Rest;
    public int Distance = 0;
    public int Points = 0;

    bool resting = false;
    int timeToNextState;

    public Reindeer(string name, int speed, int dur, int rest)
    {
        Name = name;
        Speed = speed;
        Duration = dur;
        Rest = rest;
        timeToNextState = Duration;
    }


    public void Tick()
    {
        if (resting)
        {
            timeToNextState--;
            if (timeToNextState == 0)
            {
                resting = !resting;
                timeToNextState = Duration;
            }
        }
        else
        {
            Distance += Speed;
            timeToNextState--;

            if (timeToNextState == 0)
            {
                resting = !resting;
                timeToNextState = Rest;
            }
        }

    }

}