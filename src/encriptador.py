import random
from string import ascii_letters, digits


class Encriptador:
    def __init__(self, seed:int):
        random.seed(seed)
        self.alfabeto = (ascii_letters + digits)
        self.alfabetoenc = []
        while len(self.alfabetoenc) < len(self.alfabeto):
            letra = random.choice(self.alfabeto)
            if letra not in self.alfabetoenc:
                self.alfabetoenc.append(letra)
    

    def encriptar(self, frase:str):
        nova_frase = ""
        for letra in frase:
            try:
                if letra != " ":
                    letra_nova = self.alfabeto.index(letra)
                    nova_frase += self.alfabetoenc[letra_nova]
                else:
                    nova_frase += " "
            except ValueError:
                nova_frase += letra
        return nova_frase
    

    def decriptar(self, frase:str):
        nova_frase = ""
        for letra in frase:
            try:
                if letra != " ":
                    letra_nova = self.alfabetoenc.index(letra)
                    nova_frase += self.alfabeto[letra_nova]
                else:
                    nova_frase += " "
            except ValueError:
                nova_frase += letra
        return nova_frase
