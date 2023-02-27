
def roll_call_dwarves(dwarfs):
    # for dwarf in dwarfs:
    #     print (dwarfs[dwarf])
    for i in range(len(dwarfs)):
        print(f"{i+1}. {dwarfs[i]}")

def summon_captain_planet(elements):
    newlist = []
    for element in elements:
        newlist.append(element[0].upper() + element[1:]
                       + "!")
    return newlist

def long_planeteer_calls(words):
    for word in words:
        if(len(word) > 4):
            return True
    return False

# def long_planeteer_calls(words):
#     words = [word for word in words if len(word) > 4 ]
#     return len(words) > 0


def find_the_cheese(list):
    for i in range(len(list)):
        if list[i]  == 'cheddar' or list[i] == 'gouda' or list[i] == 'camembert':
            return list[i]
    return None




# test = summon_captain_planet(["feaea","feafe","fe", "fe", "fe"])
# print(test)
