def my_fav_movie(*movies):
    print(movies)
    movies = list(movies)
    print(movies)
    print(f"My favorite movies are:")
    for movie in movies:
        print(f"    - {movie.title()}")
my_movies = ['garden state', 'into the wild', 'the secret life of walter mitty', 'green mile', 'inception']

my_fav_movie(*my_movies)
