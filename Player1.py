class joueur1:
    def __init__(self, type):
        self.type = type
        self.insulte = ""
        
        if type == "Paysan":
            self.name = "Paysan"
            self.loquacite_lvl = 3
            self.repartie_lvl = 7

        if type == "Seigneur":
            self.name = "Seigneur"
            self.loquacite  = 7
            self.repartie  = 5

        if type == "Chevalier":
            self.name = "Chevalier"
            self.loquacite_lvl = 10
            self.repartie_lvl = 3

        if type == "Bourgeois":
            self.name = "Bourgeois"
            self.loquacite_lvl = 8
            self.repartie_lvl = 4





