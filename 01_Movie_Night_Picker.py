def find_movie(movies, wanted):

    for movie in movies:
        if movie.lower().strip() == wanted.lower().strip():
            return f"Movie found: {movie}"
        
    return "Movie not found!"         
        

wanted = input("Enter movie name: ")
movies = ["Inception", "Interstellar", "Coco", "Batman", "Dune"]

result = find_movie(movies,wanted)
print(result)