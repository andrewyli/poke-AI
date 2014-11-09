from pokemon import Pokemon
from move import Move


def main():
    # runs the main calculator/predictor
    pokemon = read_from_sets("movesets")
    moves = read_from_movelist()
    stats = read_from_statlist()
    print stats
    typedict = read_from_pokemon()
    enemy_team = read_enemy_team()
    poss_team = lookup_sets(pokemon, enemy_team)  # the first of the outputs of lookup_sets
    your_team = read_from_sets("team")  # this is not actually a list of strings (it's pokes)

    for i in range(6):
        enemy_temp = enemy_team[i]
        enemy_team[i] = Pokemon(enemy_temp, None, None, None, [], [0, 0, 0, 0, 0, 0], True)
    elimination(poss_team, enemy_team, your_team)


def elimination(poss_team, enemy_team, your_team):
    while True:
        print "Pokemon (enter \"quit\" to quit): "
        pkmn = raw_input()
        if pkmn == "quit":
            break
        print "info_type (moveset, item, ability): "
        itype = raw_input()
        print "info: "
        info = raw_input()
        
        find_p = [p for p in enemy_team if p.name.lower() == pkmn.lower()]
        index = enemy_team.index(find_p[0])

        potential = []
        enemy_team[index].update_info(itype, info)
        print enemy_team[index].moveset
        for p in poss_team[index]:
            if compare_pkmn(enemy_team[index], p):
                potential.append(p)
        for p in potential:
            for m in p.moveset:
                
        """
        for p in potential:
            p.print_info()
        """


def compare_pkmn(p1, p2):
    # compares p1 to p2 (not commutative): p2 is the database version p1 is the enemy's version
    if not (p1.name is None or p1.name.lower() == p2.name.lower()):
        print "name"
        return False
    if not (p1.item is None or p1.item.lower() == p2.item.lower()):
        print "item"
        return False
    if not (p1.ability is None or p1.ability.lower() == p2.ability.lower()):
        print "ability"
        return False
    if not (p1.nature is None or p1.nature.lower() == p2.nature.lower()):
        print "nature"
        return False
    for m in p1.moveset:
        if m not in p2.moveset:
            print "moveset"
            return False
    if not (p1.indb is None or p1.indb == p2.indb):
        print "indb"
        return False
    return True


def lookup_sets(pokemon, enemy_team):
    # will return a double list
    poss_team = []
    for pkmn in enemy_team:
        matching = [p for p in pokemon if p.name.lower() == pkmn.lower()]
        poss_team.append(matching)
    return poss_team


def read_enemy_team():
    # setup file, reads in enemy names
    enemy_team = []
    print "Enter the names of the opposing pokemon: "

    for i in range(6):
        print "Pkmn " + str(i + 1) + ": "
        pkmn = raw_input()
        enemy_team.append(pkmn.lower())
    return enemy_team


def read_from_sets(file_name):
    # reads from my database of smogon "approved" sets
    pokemon = []

    f = open(file_name + ".txt", "r")
    lines = f.readlines()

    index = 0
    while index < len(lines):
        name_info = lines[index].split()
        name = name_info[0]
        item = name_info[2]
        for i in range(3, len(name_info)):
            item += " " + name_info[i]
        # print "Name: " + name
        # print "Item: " + item

        index += 1
        if lines[index][0:7] == "Ability":
            ability_info = lines[index].split()
            ability = ability_info[1]
            for i in range(2, len(ability_info)):
                ability += " " + ability_info[i]
            # print ability
        else:
            ability = "?"
            # print ability
            index -= 1

        index += 1
        evs_info = lines[index].split()
        evs = [0, 0, 0, 0, 0, 0]
        evs_i = 1
        while evs_i < len(evs_info):
            if evs_info[evs_i + 1] == "HP":
                evs[0] = evs_info[evs_i]
            if evs_info[evs_i + 1] == "Atk":
                evs[1] = evs_info[evs_i]
            if evs_info[evs_i + 1] == "Def":
                evs[2] = evs_info[evs_i]
            if evs_info[evs_i + 1] == "SpA":
                evs[3] = evs_info[evs_i]
            if evs_info[evs_i + 1] == "SpD":
                evs[4] = evs_info[evs_i]
            if evs_info[evs_i + 1] == "Spe":
                evs[5] = evs_info[evs_i]
            evs_i += 3
        # print evs

        index += 1
        nature_info = lines[index].split()
        nature = nature_info[0]
        # print nature

        moveset = []
        index += 1
        if lines[index][0:2] == "IV":
            index += 1
        for moveset_i in range(4):
            move_info = lines[index].split()
            movestring = move_info[1]
            for i in range(2, len(move_info)):
                movestring += " " + move_info[i]
            moveset.append(movestring.lower())
            # print movestring
            index += 1

        pokemon.append(Pokemon(name.lower(), item.lower(), ability.lower(), nature.lower(), moveset, evs, True))

        while index < len(lines) and lines[index] == "\n":
            index += 1

    return pokemon


def read_from_movelist():
    f = open("movelist.txt", "r")
    mlist = f.readlines()
    moves = []
    for m in mlist:
        n = m.split()
        mname = n[0].lower()
        i = 0
        if n[1].upper() != n[1]:
            i = 1
            mname += " " + n[1].lower()
        mtype = n[i + 1].lower()
        mpp = n[i + 2]
        mdmg = n[i + 3]
        macc = n[i + 4]
        mstyle = n[i + 5].lower()
        move = Move(mname, mtype, mstyle, mdmg, macc, mpp)
        moves.append(move)
        # move.print_info()
    return moves


def read_from_pokemon():
    f = open("types.txt", "r")
    plist = f.readlines()
    typings = {}
    for pstr in plist:
        p = pstr.split()
        pname = p[2].lower()
        i = 0
        if p[3].lower() == pname:
            i = 1
        ptype = []
        ptype.append(p[3 + i].lower())
        if len(p) > 4 + i:
            ptype.append(p[4 + i].lower())
        typings[pname] = ptype
    return typings


def read_from_statlist():
    f = open("statlist.txt", "r")
    slist = f.readlines()
    stats = {}
    for sstr in slist:
        s = sstr.split()
        sname = p[2].lower()
        i = 0
        if s[3][0] == "(":
            i = 1
            sname = s[3][1:len(s[3])].lower(0)
        base_stats = [int(s[3 + i]), int(s[4 + i]), int(s[5 + i]), int(s[6 + i]), int(s[7 + i]), int(s[8 + i])]
        stats[sname] = base_stats

main()
