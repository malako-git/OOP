class Haus():
    farbe = None
    adresse = None
    baujahr = None
    wohnflaeche = None
    zimmer = None
    preis = None
    grundstueckgroesse = None
    badezimmer = None
    heizart = None
    besitzer = None

    def fillEntitiy(self, list):
        self.farbe = list[0]
        self.adresse = list[1]
        self.baujahr = list[2]
        self.wohnflaeche = list[3]
        self.zimmer = list[4]
        self.preis = list[5]
        self.grundstueckgroesse = list[6]
        self.badezimmer = list[7]
        self.heizart = list[8]
        self.besitzer = list[9]
