#!/usr/bin/python3
from re import findall
from collections import defaultdict

from pprint import pprint

def makeAllRecipes(ings):
    recipes = []
    for a in range(100,0, -1):
        for b in range(1, 101-a):
            for c in range(1, 101-(a+b)):
                for d in range(1, 101-(a+b+c)):
                    if (a+b+c+d) == 100:
                        recipes.append({ings[0]:a, ings[1]:b, ings[2]:c, ings[3]:d})
                        
    return recipes

def scores(ing_props, recipes):
    scores = []
    for r in recipes:
        # print(r)
        recipe_score = 1
        for prop_i in range(1,4):
            prop_score = 0
            for ing,amt in r.items():
                # print(f'{prop_i} {ing} {ing_props[ing][prop_i]}*{amt}')
                prop_score += ing_props[ing][prop_i]*amt
            recipe_score *= max(0, prop_score)
            # print(recipe_score)
        scores.append(recipe_score)
    print(len(scores))
    return scores
        

def main():

    ing_props = defaultdict(list)
    ings = list()
    with open('input') as fp:
        for line in fp.read().strip().split('\n'):
            # get ingredient name and all the properties and
            # stores them into a dict
            ing = line.split(':')[0]
            ing_props[ing] = list(map(int, findall(r'-?\d+', line)))
            ings.append(ing)
    
    for a in ing_props.values():
        print(a)
    # recipes = makeAllRecipes(ings)
    # a = scores(ing_props, recipes)
    # print(sorted(a, reverse=True)[0])
    # pprint(recipes)


if __name__ == '__main__':
    main()
    # main(500)
