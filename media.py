import webbrowser
   
# class movie
class Movie():
   #initializes titel, storyline, poster image and trailer url variables
   def __init__(self,title, movie_storyline, poster_image, trailer_youtube):
       self.title = title
       self.storyline = movie_storyline
       self.poster_image_url = poster_image
       self.trailer_youtube_url = trailer_youtube

   #method to open a new browser window to the specified url and play    
   def show_trailer(self):
       webbrowser.open(self.youtube_trailer_url)

