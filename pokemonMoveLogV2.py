import random
import time

pocket_monsters = {"Dragonite":['Outrage', 'Fly', 'Earthquake', 'Waterfall'],
"Lugia":['Aeroblast', 'Toxic', 'Roost', 'Psychic'],
"Aegislash":['Shadow Ball','Flash Cannon','King\'s Shield','Toxic'],
"Porygon2":['Conversion2','Thunderbolt','Trick','Tri Attack'],
"Ho-Oh":['Sacred Fire', 'Brave Bird', 'Roost', 'Flame Charge'],
"Flabébé":['Energy Ball', 'Aromatherapy', 'Charm','Draining Kiss'],
"Mime Jr.":['Psychic', 'Dazzling Gleam', 'Hypnosis', 'Barrier'],
"Type: Null":['Return', 'Shadow Claw', 'Rest','Tackle'],
"Kommo-o":['Clanging Scales','Close Combat','Autotomize','Poison Jab'], 
"Gourgeist":['Trick-or-Treat', 'Leech Seed','Bullet Seed', 'Trick']}


monster_name=list(pocket_monsters.keys())
#moves=['','','','']

f= open("battleLog.txt","w+")

for i in range(0,101):
    pokemon = monster_name[random.randint(0,len(pocket_monsters)-1)]
    f.write('%s used %s\n' %(pokemon,pocket_monsters[pokemon][random.randint(0,3)]))
    print('%s used %s\n' %(pokemon,pocket_monsters[pokemon][random.randint(0,3)]))