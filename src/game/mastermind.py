from random import choices

LISTE_COULEURS = ("B", "J", "V", "R", "N")


class Mastermind:

    def __init__(self, tries: int = 8):
        self.tries = tries
        self.guesses = 0
        self.solution = []

    def generate_solution(self):
        self.solution = choices(LISTE_COULEURS, k=4)

    def compare(self, guess) -> list[str]:
        retour = []

        for i in range(len(guess)):
            if self.solution[i] == guess[i]:
                retour.append("o")
            elif self.solution[i] in guess:
                retour.append("-")
            else:
                retour.append("x")

        return retour

    def test_win(self, guess: list[str]) -> bool:
        return self.compare(guess) == ["o", "o", "o", "o"]

    def ask_guess(self) -> list[str]:
        guess = input('Proposition (ex : BJNJ) :').upper()

        assert len(guess) == 4, "La proposition doit être de 4 couleurs"
        assert all([c in LISTE_COULEURS for c in guess]), "La proposition doit être composée de couleurs valides" + str(
            LISTE_COULEURS)

        return list(guess)

    def play(self):
        self.generate_solution()

        while self.guesses < self.tries:
            guess = self.ask_guess()

            self.guesses += 1
            print(self.compare(guess))

            print("-----------------------------------------------")

            if self.test_win(guess):
                print("Bravo vous avez gagné en {} tours !".format(self.guesses))
                return
        print("Vous avez perdu... La solution était {} !".format(self.solution))


if __name__ == "__main__":
    mastermind = Mastermind()
    mastermind.play()
