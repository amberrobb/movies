import webbrowser

class Movie():
    """ This class provides a wa to store movie related information """ # comment will be shown with __doc__
    VALID_RATINGS = ["G", "PG", "PG-13", "R"] # class variable declared outside of def

    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title # instance variable
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):     # self is always needed
        webbrowser.open(self.trailer_youtube_url)
