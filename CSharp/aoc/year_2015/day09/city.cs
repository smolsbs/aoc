namespace Year2015.Day9;

class City : IEquatable<City>
{
    public string name;
    public record Connection(City City, int Distance);
    public List<Connection> connections;


    public City(string name)
    {
        this.name = name;
        connections = new();
    }

    public City addCity(City inCity, int distance)
    {
        connections.Add(new(inCity, distance));
        inCity.connections.Add(new(this, distance));
        return inCity;
    }

    public Connection GetConnection(City city)
    {
        return connections.First(c => c.City == city);
    }

    public static (int min, int max) FindMinMax(List<City> cities)
    {
        var min = int.MaxValue;
        var max = int.MinValue;
        var result = GeneratePermutations(cities);

        for (int i = 0; i < result.Count; i++)
        {
            var route = result[i];
            var cost = 0;
            for (int j = 0; j < route.Count - 1; j++)
            {
                var city = route[j];
                var next = route[j + 1];
                cost += city.GetConnection(next).Distance;
            }
            if (min > cost)
                min = cost;
            if (max < cost)
                max = cost;
        }
        return (min, max);

    }


    private static List<List<T>> GeneratePermutations<T>(List<T> cities)
    {
        List<List<T>> permutate(IEnumerable<T> reminder, IEnumerable<T> prefix)
        {
            return !reminder.Any()
                ? new List<List<T>> { prefix.ToList() }
                : reminder.SelectMany((c, i) => permutate(
                    reminder.Take(i).Concat(reminder.Skip(i + 1)).ToList(),
                    prefix.Append(c))).ToList();
        }
        return permutate(cities, Enumerable.Empty<T>());
    }

    public bool Equals(City? other)
    {
        if (other == null) return false;
        return name == other.name;
    }

    public override string ToString()
    {
        return name;
    }
}
