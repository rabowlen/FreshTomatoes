import webbrowser


class Movie():
    """This class stores and displays movie-related information"""
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

# Shows the user a trailer for the movie when the poster is clicked on.
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

