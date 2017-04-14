class Movie:
	"""Class for representing a movie.
    
    Attributes:
        title (str): Title of the movie
        trailer_youtube_url (str): URL to the movie youtube trailer
        poster_url (str): URL to the movie poster
    
    """
	def __init__(self, title, trailer_youtube_url, poster_url):
		self.title = title
		self.trailer_youtube_url = trailer_youtube_url
		self.poster_image_url = poster_url
