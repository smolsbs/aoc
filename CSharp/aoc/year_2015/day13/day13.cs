using Year2015;

namespace Year2015.Day13;
public class Day13
{

    private static TextParser<(string name1, string status, int value, string name2)> parser =
        (from name1 in Character.Letter.AtLeastOnce()
         from _ in Span.EqualTo(" would ")
         from status in Character.Letter.AtLeastOnce()
         from __ in Character.WhiteSpace
         from value in Character.Digit.AtLeastOnce()
         from ___ in Span.EqualTo(" happiness units by sitting next to ")
         from name2 in Character.Letter.AtLeastOnce()
         select (new string(name1), new string(status), int.Parse(value), new string(name2))
        );

    private static int GetBestSeats(List<string> peopleList, List<Person> people)
    {
        var permutations = peopleList.Permute();
        int happiest = int.MinValue;

        foreach (var instance in permutations)
        {
            var happy = 0;
            for (int i = 0; i < instance.Count; i++)
            {
                var currPerson = people.First(c => c.name == instance[i]);
                var nP = (i + 1) % instance.Count;
                var pP = (i - 1).mod(instance.Count);

                happy += currPerson.buddies[instance[nP]];
                happy += currPerson.buddies[instance[pP]];
            }

            if (happy > happiest)
                happiest = happy;
        }

        return happiest;
    }


    public static void Run(string Path)
    {
        string[] usrIn = File.ReadAllLines(Path).ToArray();

        List<Person> people = new();

        Person me = "Me";

        foreach (string line in usrIn)
        {
            (string name1, string status, int val, string name2) = parser.Parse(line);

            if (status == "lose") val *= -1;

            Person? person = people.FirstOrDefault(c => c.name == name1);

            if (person == null)
            {
                var newPerson = new Person(name1).addPerson(name2, val);
                newPerson.addPerson("Me", 0);
                me.addPerson(name1, 0);
                people.Add(newPerson);
            }
            else
                person.addPerson(name2, val);

        }

        var p1List = people.Select(c => c.name).ToList();

        people.Add(me);
        var p2List = people.Select(c => c.name).ToList();

        int p1 = GetBestSeats(p1List, people);
        int p2 = GetBestSeats(p2List, people);

        Console.WriteLine($"Part 1: {p1}\nPart 2: {p2}");
    }
}




public class Person
{
    public string name;

    public Person(string name) => this.name = name;

    public Dictionary<string, int> buddies = new();

    public Person addPerson(string personName, int happiness)
    {
        if (!buddies.ContainsKey(personName))
        {
            buddies.Add(personName, happiness);
        }
        return this;
    }

    public static implicit operator Person(string name) => new Person(name);


    public override string ToString()
    {
        return $"{name} => {string.Join(" | ", buddies.Select(v => $"{v.Key}:{v.Value}"))}";
    }

}