import random
import time
movesDragonite=['Outrage', 'Fly', 'Earthquake', 'Waterfall']
movesLugia=['Aeroblast', 'Toxic', 'Roost', 'Psychic']

f= open("battleLog.txt","w+")

for i in range(0,30):
    x=random.randint(1,12)
    y=random.randint(1,2)

    if (y==1):
        pokemon='Dragonite'
        moves=movesDragonite
    else:
        pokemon='Lugia'
        moves=movesLugia
    if(x==1 or x==2 or x==3 or x==4):
        f.write('%s used %s\n' %(pokemon,moves[0]))
    elif(x==5 or x==6 or x==7 or x==8):
        f.write('%s used %s\n' %(pokemon,moves[1]))
    elif(x==9 or x==10):
        f.write('%s used %s\n' %(pokemon,moves[2]))
    else:
        f.write('%s used %s\n' %(pokemon,moves[3]))