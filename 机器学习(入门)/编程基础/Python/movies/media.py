import webbrowser

class Movie():
    def __init__(self,movie_title,movie_storyline,year,poster_image,trailer_url):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_url = trailer_url
        self.year = year

    def show_trailer(self):
        webbrowser.open(self.trailer_url)