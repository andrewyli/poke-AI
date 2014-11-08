class Pokemon(object):
    def __init__(self, name, item, ability, nature, moveset, evs):
        self.name = name
        self.item = item
        self.ability = ability
        self.nature = nature
        self.moveset = moveset
        self.evs = evs

    def update_information(self, type, info):
        if type == "name":
            self.name = info
        if type == "item":
            self.item = info
        if type == "nature":
            self.nature = info
        if type == "ability":
            self.ability = info
        if type == "moveset":
            self.moveset = info
        if type == "evs":
            self.evs = info
