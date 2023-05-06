class Samochod:
    def __init__(self, marka, model, rok_produkcji, przebieg):
        self.marka = marka
        self.model = model
        self.rok_produkcji = rok_produkcji
        self.przebieg = przebieg

    def __str__(self):
        return f"{self.marka} {self.model} ({self.rok_produkcji}), przebieg: {self.przebieg} km"

    def __lt__(self, other):
        return self.przebieg < other.przebieg


s1 = Samochod("Skoda", "Fabia", 2003, 134000)
s2 = Samochod("Toyota", "Yaris", 2015, 76000)

print(s1)
print(s2)

print(s1 < s2)
print(s2 < s1)
