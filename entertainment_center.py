import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar",
                     "Smurfs in space",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

prometheus = media.Movie("Prometheus",
                         "Charlice Theron and an Alien in Space",
                         "https://upload.wikimedia.org/wikipedia/en/a/a3/Prometheusposterfixed.jpg",
                         "https://www.youtube.com/watch?v=R5j1Y8EGWnc")

school_of_rock = media.Movie("School of Rock",
                         "Jack Black is a teacher with a guitar",
                         "https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                         "https://www.youtube.com/watch?v=3PsUJFEBC74")

midnight_in_paris = media.Movie("Midnight in Paris",
                         "Woody Allens surreal story set in the french capital",
                         "https://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
                         "https://www.youtube.com/watch?v=FAfR8omt-CY")

hunger_games = media.Movie("Hunger Games",
                         "Only one can survive the hunger games",
                         "https://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",
                         "https://www.youtube.com/watch?v=mfmrPu43DF8")

movies = [toy_story, avatar, prometheus, school_of_rock, midnight_in_paris, hunger_games]

fresh_tomatoes.open_movies_page(movies)
#print(media.Movie.VALID_RATINGS)
#print(media.Movie.__doc__)
#print(media.Movie.__module__)
#print(media.Movie.__name__s)
