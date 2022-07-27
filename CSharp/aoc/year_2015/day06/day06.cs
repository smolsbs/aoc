namespace Year2015.Day6;

public class Day6
{
    private enum States { Off, On, Toggle };
    public static void run(string Path)
    {
        string[] usrIn = File.ReadAllLines(Path).Select(l => l).ToArray();
        var gridP1 = new int[1000, 1000];
        var gridP2 = new int[1000, 1000];
        int p1 = 0;
        int p2 = 0;


        TextParser<(States instruction, (int x1, int y1, int x2, int y2) coords)> parser =
            (from instructs in Character.Letter.Or(Character.WhiteSpace).AtLeastOnce()
             from coordFromX in Character.Digit.AtLeastOnce()
             from _ in Character.EqualTo(',')
             from coordFromY in Character.Digit.AtLeastOnce()
             from __ in Span.EqualTo(" through ")
             from coordToX in Character.Digit.AtLeastOnce()
             from ___ in Character.EqualTo(',')
             from coordToY in Character.Digit.AtLeastOnce()
             select (new string(instructs) switch { "turn on " => States.On, "turn off " => States.Off, _ => States.Toggle },
             (int.Parse(coordFromX), int.Parse(coordFromY), int.Parse(coordToX), int.Parse(coordToY)))
            );



        foreach (string line in usrIn)
        {
            var currInst = parser.Parse(line);

            switch (currInst.instruction)
            {
                case States.On:
                    RegionSetter(currInst.coords, 1);
                    break;
                case States.Off:
                    RegionSetter(currInst.coords, 0);
                    break;
                default:
                    RegionToggle(currInst.coords);
                    break;
            }
        }

        void RegionToggle((int x1, int y1, int x2, int y2) coords)
        {
            for (int i = coords.x1; i <= coords.x2; i++)
            {
                for (int j = coords.y1; j <= coords.y2; j++)
                {
                    gridP1[i, j] = gridP1[i, j] == 0 ? 1 : 0;
                    gridP2[i, j] += 2;
                }
            }
        }

        void RegionSetter((int x1, int y1, int x2, int y2) coords, int state)
        {
            for (int i = coords.x1; i <= coords.x2; i++)
            {
                for (int j = coords.y1; j <= coords.y2; j++)
                {
                    gridP1[i, j] = state;
                    gridP2[i, j] += state == 0 ? -1 : 1;
                }
            }
        }


        p1 = gridP1.Cast<int>().Sum();
        p2 = gridP2.Cast<int>().Sum();

        Console.WriteLine($"Part 1: {p1}\nPart 2: {p2}");

    }
}