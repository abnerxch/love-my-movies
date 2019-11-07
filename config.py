import os


class Config:
    MOVIE_API_BASE_URL ='https://api.themoviedb.org/3/movie/{}?api_key={}'
    MOVIE_API_KEY = '332ad6279a4d4f18eafb966735435f21'
    SECRET_KEY = '550'

# simple mde  configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True
    

class ProdConfig(Config):

    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")


class DevConfig(Config):

    DEBUG = True


config_options = {
'development': DevConfig,
'production': ProdConfig
}
