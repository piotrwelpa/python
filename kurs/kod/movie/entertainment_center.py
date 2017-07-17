import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toy that come to life",
                        "http://www.gstatic.com/tv/thumb/movieposters/17420/p17420_p_v8_ab.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")


avatar = media.Movie("Avatar",
                     "A marine on an alein planet",
                     "http://www.impawards.com/2009/posters/avatar_xlg.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")


matrix = media.Movie("Matrix",
                     "Hacker figured out that he lives in simulation",
                     "https://s-media-cache-ak0.pinimg.com/originals/b2/3a/7a/b23a7a293e5b2ba15c48d8320cdeeed8.jpg",
                     "https://www.youtube.com/watch?v=vKQi3bBA1y8")

school_of_rock = media.Movie("School of Rock",
                             "Using rock music to learn",
                             "https://images-na.ssl-images-amazon.com/images/I/81m0ywBJ67L._SY445_.jpg",
                             "https://www.youtube.com/watch?v=5afGGGsxvEA")

midnight_in_paris = media.Movie("Midnight in Paris",
                                "Going back in time to meet authors",
                                "http://is1.mzstatic.com/image/thumb/Video/v4/e0/0f/d2/e00fd25b-be6a-c6a1-f1b3-e05b4dc1f2e7/source/1200x630bb.jpg",
                                "https://www.youtube.com/watch?v=FAfR8omt-CY")


hunger_games = media.Movie("Hunger Games",
                           "A really real reality show",
                           "http://cdn.collider.com/wp-content/uploads/the-hunger-games-poster.jpg",
                           "https://www.youtube.com/watch?v=mfmrPu43DF8")

movies = [toy_story, avatar, matrix, school_of_rock, midnight_in_paris, hunger_games]
#fresh_tomatoes.open_movies_page(movies)
#print(media.Movie.VALID_RATINGS)
print(media.Movie.__module__)
