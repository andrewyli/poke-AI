from pokemon import Pokemon


def read_from_movesets():
    pokemon = []

    f = open("movesets.txt", "r")
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
        for moveset_i in range(4):
            move_info = lines[index].split()
            movestring = move_info[1]
            for i in range(2, len(move_info)):
                movestring += " " + move_info[i]
            moveset.append(movestring)
            # print movestring
            index += 1

        pokemon.append(Pokemon(name, item, ability, nature, moveset, evs))

        while index < len(lines) and lines[index] == "\n":
            index += 1

    return pokemon


def main():
    pokemon = read_from_movesets()
    enemy_team = []
    print "Enter the names of the opposing pokemon: "

    for i in range(6):
        print "Pkmn " + i + ": "
        pkmn = raw_input()
        enemy_team.append(pkmn)
        print enemy_team[i]
main()
