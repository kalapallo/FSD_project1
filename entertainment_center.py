import media
import fresh_tomatoes

# initialize movies array
movies = []

# create individual movie objects with their attributes
movies.append(media.Movie("Inception", 
	"https://www.youtube.com/watch?v=YoHD9XEInc0",
	"http://cdn.collider.com/wp-content/uploads/Inception-movie-poster-7.jpg"))
movies.append(media.Movie("Arrival", 
	"https://www.youtube.com/watch?v=AMgyWT075KY",
	"http://cdn2-www.comingsoon.net/assets/uploads/gallery/arrival/cp8v8n0vmaadzn6-jpg-large.jpg"))  # NOQA
movies.append(media.Movie("Altered States", 
	"https://www.youtube.com/watch?v=2YfdpZdugBM",
	"https://alchetron.com/cdn/Altered-States-images-f74bbb61-ca26-4169-ab2e-6f1d20a78b6.jpg"))  # NOQA

# create content
content = fresh_tomatoes.create_movie_tiles_content(movies)

# open movies page
fresh_tomatoes.open_movies_page(movies)
