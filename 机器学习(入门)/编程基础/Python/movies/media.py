# This Python file uses the following encoding: utf-8
import webbrowser


class Movie():
    def __init__(self, title, storyline, year, poster, trailer_url):
        """Init Movie Instance

        Keyword arguments:
        title -- movie title
        storyline -- movie storyline
        year -- movie release year
        poster -- movie poster image
        trailer_url -- movie trailer url
        """

        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster
        self.trailer_url = trailer_url
        self.year = year

    def show_trailer(self):
        """Open Web Browser And Play Video"""

        webbrowser.open(self.trailer_url)
