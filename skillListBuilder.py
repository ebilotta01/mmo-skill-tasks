import skill
import json
import os

def buildSkillList():
    skillList = json.load(open("skillList.json"))
    return skillList

def get_key(dictionary, n=0):
    if n < 0:
        n += len(dictionary)
    for i, key in enumerate(dictionary.keys()):
        if i == n:
            return key
    raise IndexError("dictionary index out of range") 

def get_val(dictionary, n=0):
    if n < 0:
        n += len(dictionary)
    for i, val in enumerate(dictionary.values()):
        if i == n:
            return val
    raise IndexError("dictionary index out of range") 


def storeSkillList():
    skills = {
        'Technomancy': { 
            'Level': 1, 
            'Xp': 0
        },
        'Virtuosity': {
            'Level': 1, 
            'Xp': 0
        },   
        'Physicality': 
        {
            'Level': 1, 
            'Xp': 0
        },
        'Scholarship': {
            'Level': 1, 
            'Xp': 0
        }
    }
    filename = 'skillList.json'
    with open(filename, 'w') as file_object:
        json.dump(skills, file_object)

if(os.stat("skillList.json").st_size == 0):
    print("skill list empty")
else:
    buildSkillList()

skLst = buildSkillList()
