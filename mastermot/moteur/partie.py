from ..utils import récupérer_mot_aléatoire
class Partie:
    def __init__(self):
        self.mot = récupérer_mot_aléatoire()
        self.progrès = [0, 0, 0, 0, 0]

    def tester_mot(self, mot):
        mot.replace("é", "e").replace("è", "e").replace("ê", "e").replace("à", "a").replace("â", "a").replace("ù", "u").replace("û", "u").replace("ç", "c")
        if mot == self.mot:
            return True
        else:
            for i in range(5):
                if mot[i] == self.mot[i]:
                    self.progrès[i] = 2
                elif mot[i] in self.mot:
                    self.progrès[i] = 1
                else:
                    self.progrès[i] = 0
            return False
