namespace Year2015;


public static class Utils
{

    public static int mod(this int a, int n)
    {
        return ((a % n) + n) % n;
    }



    public static IEnumerable<List<T>> Permute<T>(this IEnumerable<T> cities)
    {
        IEnumerable<List<T>> permutate(IEnumerable<T> reminder, IEnumerable<T> prefix)
        {
            return !reminder.Any()
                ? new List<List<T>> { prefix.ToList() }
                : reminder.SelectMany((c, i) => permutate(
                    reminder.Take(i).Concat(reminder.Skip(i + 1)).ToList(),
                    prefix.Append(c)));
        }
        return permutate(cities, Enumerable.Empty<T>());
    }
}