# this class contains the information for each pokemon set.


class Pokemon(object):
    def __init__(self, name, item, ability, nature, moveset, evs, indb):
        self.name = name
        self.item = item
        self.ability = ability
        self.nature = nature
        self.moveset = moveset
        self.evs = evs
        self.indb = indb

    def update_info(self, itype, info):
        if itype.lower() == "name":
            self.name = info
        if itype.lower() == "item":
            self.item = info
        if itype.lower() == "nature":
            self.nature = info
        if itype.lower() == "ability":
            self.ability = info
        if itype.lower() == "moveset":
            if len(self.moveset) < 4:
                self.moveset.append(info)
            else:
                print "Tried to add too many moves."
        if itype == "evs":
            self.evs = info
        if itype == "indb":
            self.indb = info

    def get_info(self, itype):
        if itype == "name":
            return self.name
        if itype == "item":
            return self.item
        if itype == "nature":
            return self.nature
        if itype == "ability":
            return self.ability
        if itype == "moveset":
            return self.moveset
        if itype == "evs":
            return self.evs

    def print_info(self):
        print "Name: ", self.name
        print "Item: ", self.item
        print "Ability: ", self.ability
        print "Nature: ", self.nature
        print "Moveset: ", self.moveset
        print "EVs: ", self.evs
