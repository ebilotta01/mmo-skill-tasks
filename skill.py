

class Skill:
    def __init__(self, name, xp, level):
        self.name = name
        self.xp = xp
        self.level = level

    def addXp(self, val):
        self.xp += val
        self.updateLevel()

    def updateLevel(self):
        self.level = (self.xp - 1)/4


#s1 = Skill("Technomancy", 0, 1)
#print(s1.name)
#s1.addXp(37)
#print(s1.level)

