import movie
import fresh_tomatoes

toy_story = movie.Movie("Toy Story",
                        "Story of a boy and his toy who come to life",
                        "http://www.imagespourtoi.com/lesimages/toy-story/images-toy-story-13.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")
#print (toy_story.storyline)

avatar = movie.Movie("Avatar",
                        "A marine on an alien planet",
                        "http://www.impawards.com/2009/posters/avatar_xlg.jpg",
                        "https://www.youtube.com/watch?v=d1_JBMrrYw8")
#print (avatar.storyline)
#avatar.show_trailer()

#creating a aray list of movie 
movies = [toy_story, avatar]


fresh_tomatoes.open_movies_page(movies)

#impression de la doc
print(movie.Movie.__doc__)
