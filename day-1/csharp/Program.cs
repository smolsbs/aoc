using System;
using System.Collections.Generic;
using System.IO;

namespace c_
{
    class Program
    {
        static void Main()
        {
            string file = Path.Combine(Directory.GetParent(Directory.GetCurrentDirectory()) + "\\input");
            string[] aux = File.ReadAllText(file).Trim().Split('\n');
            
            Console.WriteLine(Part1(aux));
            Console.WriteLine(Part2(aux));   
        }

        static int Part1(string[] inp){
            int freq = 0;

            foreach (string s in inp){
                freq += int.Parse(s);
            }
            return freq;
        }

        static int Part2(string[] inp){
            var s = new HashSet<int>();
            int freq = 0;
            bool twice = false;

            while (!twice){
                foreach(string n in inp){
                    freq += int.Parse(n);
                    if(s.Contains(freq)){
                        twice = true;
                        break;
                    }else{s.Add(freq);}
                }
            }
            return freq;
        }
    }
}
