import urllib.request,json
from .models import Movie
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

#Movie = movie.Movie
# Getting api key
api_key = None