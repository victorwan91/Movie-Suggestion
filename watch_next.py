# Import spacy
import spacy

# Load "en_core_web_md" and store in variable "nlp".
nlp = spacy.load("en_core_web_md")

# Open "movies.txt" in "file" and use .readlines() to read the movies in the file in "movies". Then, close the file.
file = open("movies.txt", "r")
movies = file.readlines()
file.close()


# Define function "movie_to_watch" with "description" as the parameter.
def movie_to_watch(description):
    nlp_description = nlp(description)

    # Set 0 in variable "most_similar" and an empty string in "movie_suggestion".
    most_similar = 0
    movie_suggestion = ""

    print(f"Similarities of the movies:")
    # Loop through movie list and print all the similarity of the movies.
    for movie in movies:
        similarity = nlp(movie).similarity(nlp_description)
        print(f"{movie[:7]} - {similarity}")

        # Use if statement to find the movie that has the highest similarity.
        if similarity > most_similar:
            most_similar = similarity
            movie_suggestion = movie

    # Return the name of the suggested movie.
    return movie_suggestion


# Put the movie description of Planet Hulk in variable "movie_description".
movie_description = "Will he save their world or destroy it? When the Hulk becomes " \
                    "too dangerous for the Earth, the Illuminati trick Hulk into a " \
                    "shuttle and launch him into space to a planet where the Hulk " \
                    "can live in peace. Unfortunately, Hulk land on the planet " \
                    "Sakaar where he is sold into slavery and trained as a " \
                    "gladiator. "

# Print the movie that is suggested the user to watch (the highest similarity).
print(f"\nYou should watch:\n{movie_to_watch(movie_description)}")
