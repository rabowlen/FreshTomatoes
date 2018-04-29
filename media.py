import webbrowser


class Movie():
    """This class stores and displays movie-related information

    Note:
        Do not include the `self` parameter in the ``Args`` section.

    Args:
        movie_title (str): The movie's full title.
        movie_storyline (str): A short description of the plot.
        poster_image (str): A url for the movie's poster.
        trailer_youtube (str): A url for the movie's trailer.

    Attributes:
        title (str): The movie's full title.
        storyline (str): A short description of the plot.
        poster_image_url (str): A url for the movie's poster.
        trailer_youtube_url (str): A url for the movie's trailer.

    Methods:
        show_trailer(): shows user a trailer for the movie on image click.
    """
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

