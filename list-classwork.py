#!/usr/bin/env python3
import pprint
pp = pprint.PrettyPrinter(width=41, compact=True)
#create 3 different lists of food items
list1 = ["wings", "popcorn", "gara-su"]
list2 = ["skittles", "snickers", "twix"]
list3 = ["chorizo", "pancakes", "blackberry"]


#superlist = list1.extend(list2)

#combine lists
list1.append(list2)
list1.append(list3)

#print the combination of lists
print(list1)
#print favorite food item
print(f"My favorite food to eat are: {list1[0]}",end="\n")
real_heroes = {
        "Thanos" : {
        "strength" : "99",
        "intel" : "99",
        "line" : "You Couldn't Live with Your Own Failure, Where Did that Bring You? Back to Me"
        },

        "Darkseid" :  {
        "strength" : "99",
        "intel" : "99",
        "line" : "YOU DARE"
        },
        "Lex_Luthor" :{
        "Strength" : "25",
        "intel" : "100",
        "line" : "Most of the League dies...And Superman's beloved city is vaporized...I console the masses by offering to rebuild it. In my own image of cou-unn..."
        }
}

#pp.pprint(real_heroes["Thanos"],real_heroes["Darkseid"])
#print(real_heroes.keys(), end="\n")
#print(real_heroes.values(), end="\n")
#print(Thanos)
#print(Darkseid)
#print(Lex_Luthor)
pp.pprint(real_heroes)
