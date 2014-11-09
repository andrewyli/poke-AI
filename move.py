class Move(object):

    def __init__(self, mname, mtype, mstyle, mdmg, macc, mpp):
        self.mname = mname
        self.mtype = mtype
        self.mstyle = mstyle
        self.mdmg = mdmg
        self.macc = macc
        self.mpp = mpp

    def print_info(self):
        print "Name: ", self.mname
        print "Type: ", self.mtype
        print "Category: ", self.mstyle
        print "Damage: ", self.mdmg
        print "Accuracy: ", self.macc
        print "PP: ", self.mpp

