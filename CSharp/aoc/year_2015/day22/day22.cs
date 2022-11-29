namespace Year2015.Day21;
public class Day22
{

    private class Chara
    {
        public string Name;
        public int Mana;
        public int Attack;
        public int Armor;
        public int HP;

        public Chara(int mana, int def, int hp, int dmg, string name)
        {
            Name = name;
            HP = hp;
            Attack = dmg;
            Armor = def;
            Mana = mana;
        }


    }
    private List<Spell> spells = new List<Spell>
    {
        new Spell("Magic Missile", 53, 4),
        new Spell("Drain", 73, 2),
        new Spell("Shield", 113, Armor:7, Timer:6 ),
        new Spell("Poison", 173, Attack:2, Timer:6 ),
        new Spell("Recharge", 229, Recharge:101, Timer:5)
    };


    private static void Battle(Chara player, Chara boss, string[] plays)
    {
        foreach (string play in plays)
        {

        }
    }

    public static void Run()
    {
        Chara boss = new Chara(0, 0, 55, 8, "Boss");
        Chara player = new Chara(500, 0, 50, 0, "Player");
        // string[] plays;



    }
}


public record Spell(string Name, int Cost, int Attack = 0, int Recharge = 0, int Armor = 0, int Timer = 0);

