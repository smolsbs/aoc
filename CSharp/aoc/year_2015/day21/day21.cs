namespace Year2015.Day21;
using Combinatorics.Collections;
public class Day21
{
    private static Dictionary<string, Item> weapons = new Dictionary<string, Item>()
    {
        {"Dagger", new Item {Name="Dagger", Price=8, Damage=4, Armour=0}},
        {"Shortsword", new Item {Name="Shortsword", Price=10, Damage=5, Armour=0}},
        {"Warhammer", new Item {Name="Warhammer", Price=25, Damage=6, Armour=0}},
        {"Longsword", new Item {Name="Longsword", Price=40, Damage=7, Armour=0}},
        {"Greataxe", new Item {Name="Greataxe", Price=74, Damage=8, Armour=0}},
    };
    private static Dictionary<string, Item> armor = new Dictionary<string, Item>()
    {
        {"Nothing", new Item {Name="Nothing", Price=0, Damage=0, Armour=0}},
        {"Leather", new Item {Name="Leather", Price=13, Armour=1, Damage=0}},
        {"Chainmail", new Item {Name="Chainmail", Price=31, Armour=2, Damage=0}},
        {"Splintmail", new Item {Name="Splintmail", Price=53, Armour=3, Damage=0}},
        {"Bandedmail", new Item {Name="Bandedmail", Price=75, Armour=4, Damage=0}},
        {"Platemail", new Item {Name="Platemail", Price=102, Armour=5, Damage=0}},
    };
    private static Dictionary<string, Item> rings = new Dictionary<string, Item>()
    {
        {"Nothing", new Item {Name="Nothing", Price=0, Damage=0, Armour=0}},
        {"Nothing 2", new Item {Name="Nothing 2", Price=0, Damage=0, Armour=0}},
        {"Damage +1", new Item {Name="Damage +1", Price=25, Damage=1, Armour=0}},
        {"Damage +2", new Item {Name="Damage +2", Price=50, Damage=2, Armour=0}},
        {"Damage +3", new Item {Name="Damage +3", Price=100, Damage=3, Armour=0}},
        {"Defense +1", new Item {Name="Defense +1", Price=20, Armour=1, Damage=0}},
        {"Defense +2", new Item {Name="Defense +2", Price=40, Armour=2, Damage=0}},
        {"Defense +3", new Item {Name="Defense +3", Price=80, Armour=3, Damage=0}},
    };

    static TextParser<Char> parser =
        (from _ in Span.Length(12)
         from hp in Character.Digit.AtLeastOnce()
         from __ in Span.Length(9)
         from dmg in Character.Digit.AtLeastOnce()
         from ___ in Span.Length(8)
         from def in Character.Digit.AtLeastOnce()
         select (new Char(int.Parse(dmg), int.Parse(def), int.Parse(hp)))
        );

    public static void Run(string Path)
    {
        int p1 = 0;
        int p2 = 0;

        var itemComb = AllItems();

        Char boss = parser.Parse(File.ReadAllText(Path));
        Char player = new Char(0, 0, 100, "Player");

        while (p1 == 0)
        {
            foreach (var (w, a, r1, r2, c) in itemComb)
            {
                boss.Reset();
                player.Reset();
                player.ApplyBuffs((w, a, r1, r2));

                string winner = Combat(player, boss);
                if (winner == "Player" && p1 == 0)
                {
                    p1 = c;
                }

                if (winner == "Boss")
                {
                    if (c > p2)
                        p2 = c;
                }
            }
        }
        Console.WriteLine($"Part 1: {p1}\nPart 2: {p2}");
    }

    private static string Combat(Char player, Char boss)
    {
        while (true)
        {
            //player goes first
            boss.HP -= (Math.Max(0, player.Attack - boss.Armour));
            if (boss.HP <= 0)
                return player.Name;

            // boss next
            player.HP -= (Math.Max(0, boss.Attack - player.Armour));
            if (player.HP <= 0)
                return boss.Name;
        }
    }

    private static List<(Item, Item, Item, Item, int)> AllItems()
    {
        string[] weps = weapons.Keys.ToArray();
        string[] armors = armor.Keys.ToArray();
        var _rings = new Combinations<string>(rings.Keys.ToList(), 2).ToList();

        var items = new List<(Item, Item, Item, Item, int)>();

        foreach (string w in weps)
        {
            foreach (string a in armors)
            {
                foreach (List<string> v in _rings)
                {
                    int cost = weapons[w].Price;
                    cost += armor[a].Price;
                    cost += rings[v[0]].Price;
                    cost += rings[v[1]].Price;
                    items.Add((weapons[w], armor[a], rings[v[0]], rings[v[1]], cost));
                }
            }
        }
        return items.OrderBy(v => v.Item5).ToList();
    }
}

public class Item
{
    public string? Name { get; set; }
    public int Price { get; set; }
    public int Damage { get; set; }
    public int Armour { get; set; }
}

public class Char
{
    public string Name;
    public int Attack;
    private int _att;
    public int Armour;
    private int _arm;
    public int HP;
    private int _hp;

    public Char(int dmg, int def, int hp, string name = "Boss")
    {
        Name = name;
        HP = hp;
        _hp = hp;
        Armour = def;
        _arm = def;
        Attack = dmg;
        _att = dmg;
    }

    public void ApplyBuffs((Item, Item, Item, Item) items)
    {
        (Item w, Item a, Item r1, Item r2) = items;
        Attack += (w.Damage + a.Damage + r1.Damage + r2.Damage);
        Armour += (w.Armour + a.Armour + r1.Armour + r2.Armour);
    }

    public void Reset()
    {
        Attack = _att;
        Armour = _arm;
        HP = _hp;
    }
}