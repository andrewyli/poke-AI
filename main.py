from pokemon import Pokemon
from move import Move


def main():
    # runs the main calculator/predictor
    pokemon = read_from_sets("movesets")
    moves = read_from_movelist()
    stats = read_from_statlist()
    typedict = read_from_pokemon()
    typechart = read_from_typechart()
    enemy_team = read_enemy_team()
    poss_team = lookup_sets(pokemon, enemy_team)  # the first of the outputs of lookup_sets
    your_team = read_from_sets("team")  # this is not actually a list of strings (it's pokes)

    for i in range(6):
        enemy_temp = enemy_team[i]
        enemy_team[i] = Pokemon(enemy_temp, None, None, None, [], [0, 0, 0, 0, 0, 0], True)

    while True:

        print "Their Pokemon (enter \"quit\" to quit): "
        e_pkmn = raw_input().lower()
        if e_pkmn == "quit":
            break
        print "Your Pokemon: "
        y_pkmn = raw_input().lower()
        print "info_type (moveset, item, ability): "
        itype = raw_input().lower()
        print "info: "
        info = raw_input().lower()

        find_p = [p for p in enemy_team if p.name.lower() == e_pkmn.lower()]
        index = enemy_team.index(find_p[0])
        
        potential = []
        enemy_team[index].update_info(itype, info)
        print enemy_team[index].moveset
        for p in poss_team[index]:
            if compare_pkmn(enemy_team[index], p):
                potential.append(p)

        index = your_team.index(y_pkmn)

        for p in potential:
            for m in p.moveset:
                if m.mtype == "N/A":
                    continue
                elif m.mstyle == "SpA":
                    mod = 1
                    for t in typedict[p]:
                        numarr = [x for x in typechart[t.lower()] if x[0] == typedict[y_pkmn]]
                        if numarr[0][1] == 0:
                            mod *= 1
                        elif numarr[0][1] == 1:
                            mod *= 2
                        elif numarr[0][1] == 2:
                            mod *= 0.5
                        elif numarr[0][1] == 3:
                            mod *= 0
                    if typedict[p] == m.mtype:
                        mod *= 1.5
                    dmg = ((2 * 100 + 10) / 250 * (141 + 2 * stats[e_pkmn][3] + 63) / (141 + 2 * stats[y_pkmn][4] + your_team[index].evs[4]) * m.mdmg + 2) * 0.85
                    print dmg


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
        index = 2
        pname = p[index].lower()
        if pname == "mr." or pname == "mime":
            pname += " " + p[index + 1].lower()
            index += 1
        if p[3].lower() == pname:
            index += 1
        ptype = []
        ptype.append(p[index].lower())
        if len(p) > index + 1:
            ptype.append(p[index + 1].lower())
        typings[pname] = ptype
    return typings


def read_from_statlist():
    f = open("statlist.txt", "r")
    slist = f.readlines()
    stats = {}
    for sstr in slist:
        s = sstr.split()
        index = 2
        sname = s[index].lower()
        if sname == "mr." or sname == "mime":
            sname += " " + s[index + 1].lower()
            index += 1
        index += 1
        if s[index][0] == "(":
            leftindex = sstr.index("(")
            rightindex = sstr.index(")")
            sname = sstr[leftindex + 1:rightindex].lower()
            # print sname
            while not is_number(s[index]):
                index += 1
                # print s[index]

        base_stats = [int(s[index]), int(s[1 + index]), int(s[2 + index]), int(s[3 + index]), int(s[4 + index]), int(s[5 + index])]
        stats[sname] = base_stats
    return stats


def read_from_typechart():
    f = open("typechart.txt", "r")
    typechart = {}
    for i in range(18):
        tname = f.readline().split()[0].lower()
        tarr = []
        for j in range(18):
            ttemp = f.readline().lower()
            ttemp2 = ttemp.split()
            tarr.append(ttemp2)
        typechart[tname] = tarr
        f.readline()
    return typechart


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

main()
