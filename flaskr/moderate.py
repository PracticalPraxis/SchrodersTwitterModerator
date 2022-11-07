from dataclasses import dataclass
import random
import os


@dataclass
class Moderate:
    message: str

    def __call__(self):

        print(os.getcwd())
        words = self.message.split(" ")

        return " ".join([self.moderate_word(w) for w in words])

    def moderate_word(self, word):
        with open("./flaskr/data/films.csv") as f:
            films = f.readlines()

        with open("./flaskr/data/badwords.txt") as f:
            bad = [x.strip() for x in f.readlines()]

        if word.lower() in [b.lower() for b in bad]:
            return random.choice(films)

        return word
