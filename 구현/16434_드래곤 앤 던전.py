import math


class Hero:
    def __init__(self, maxHp,hp, att):
        self.maxHp = maxHp
        self.hp = hp
        self.att = att

class Monster:
    def __init__(self, maxHp, hp, att):
        self.maxHp = maxHp
        self.hp = hp
        self.att = att

def battle(hero, monster):
        N = math.ceil( monster.hp / hero.att )
        hero.hp -= (N-1) * monster.att
        return


minHP = 1
numRoom, initialAtt = map(int,input().split())
nowHero = Hero(0,0,initialAtt)
for i in range(numRoom):
    x,y,z = map(int,input().split())
    if x == 1:
        monsterAtt = y
        monsterHp = z
        nowMonster = Monster(z,z,y)
        battle(nowHero,nowMonster)
        if minHP > nowHero.hp:
            minHP = nowHero.hp
    if x == 2:
        increasingAtt = y
        increasingHp = z
        nowHero.hp = min(0, nowHero.hp + z )
        nowHero.att += y

print(minHP*(-1) + 1)