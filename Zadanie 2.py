class Movie:
    def __init__(self, title, year, rating):
        self.title = title
        self.year = year
        self.rating = rating

# Tworzenie listy filmów
movies = [
    Movie("Skazani na Shawshank", 1994, 8.7),
    Movie("Nietykalni", 2011, 8.6),
    Movie("Zielona mila", 1999, 8.7),
    Movie("Ojciec chrzestny", 1972, 8.5),
    Movie("Dwunastu gniewnych ludzi", 1957, 8.9),
    Movie("Lista Schindlera", 1993, 8.3),
    Movie("Władca Pierścieni: Powrót króla", 2003, 8.9),
    Movie("Pulp Fiction", 1994, 8.2),
    Movie("Forrest Gump", 1994, 8.8),
    Movie("Lot nad kukułczym gniazdem", 1975, 8.4)
]

# Sortowanie listy wg roku
movies_sorted_by_year = sorted(movies, key=lambda x: x.year)

# Sortowanie listy wg tytułu
movies_sorted_by_title = sorted(movies, key=lambda x: x.title)

# Sortowanie listy wg oceny, malejąco
movies_sorted_by_rating_desc = sorted(movies, key=lambda x: x.rating, reverse=True)

# Sortowanie listy wg oceny, rosnąco
movies_sorted_by_rating_asc = sorted(movies, key=lambda x: x.rating)

# Sortowanie listy wg roku, a następnie tytułu
movies_sorted_by_year_and_title = sorted(movies, key=lambda x: (x.year, x.title))

# Wypisanie posortowanej listy
print("Posortowane wg roku:")
for movie in movies_sorted_by_year:
    print(movie.title, movie.year, movie.rating)
print()

print("Posortowane wg tytułu:")
for movie in movies_sorted_by_title:
    print(movie.title, movie.year, movie.rating)
print()

print("Posortowane wg oceny, malejąco:")
for movie in movies_sorted_by_rating_desc:
    print(movie.title, movie.year, movie.rating)
print()

print("Posortowane wg oceny, rosnąco:")
for movie in movies_sorted_by_rating_asc:
    print(movie.title, movie.year, movie.rating)
print()

print("Posortowane wg roku, a następnie tytułu:")
for movie in movies_sorted_by_year_and_title:
    print(movie.title, movie.year, movie.rating)
print()
