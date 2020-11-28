import os

class Config:
    ""
    ""
    NEWS_SOURCES_BASE_URL ='https://newsapi.org/v2/sources?apiKey=5a5e0803fbd240e48afd3f5cf5443e22'
    ARTICLES_BASE_URL = 'https://newsapi.org/v2/everything?q=bitcoin&apiKey=5a5e0803fbd240e48afd3f5cf5443e22'
    API_KEY = os.environ.get('API_KEY') 
    SECRET_KEY = os.environ.get('SECRET_KEY')
    @staticmethod
    def init_app(app):
            pass

class ProdConfig(Config):
    '''
    Production  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass

class DevConfig(Config):
    '''
    Development  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    DEBUG = True
    
config_options = {
'development':DevConfig,
'production':ProdConfig
}