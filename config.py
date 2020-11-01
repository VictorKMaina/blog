import os

class Config:
    """
    Class for app configuration
    """
    # WTForms configurations
    SECRET_KEY = os.environ.get("SECRET_KEY")

    # Set location for Flask Uploads
    UPLOADED_PHOTOS_DEST = "app/static/images"

    # API Key configurations
    QUOTES_API_KEY = os.environ.get("QUOTES_API_KEY")
    QUOTES_BASE_URL = os.environ.get("QUOTES_BASE_URL")

    # Mail configurations
    MAIL_SERVER = "smpt.gmail.com"
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

    # SimpleMDE Configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USER_CDN = True
    

class DevConfig(Config):
    """
    Class for development configurations. Child of class Config.
    """
    psql_username = "victormainak"
    psql_password = "password"
    SQLALCHEMY_DATABASE_URI = f"postgresql+psycopg2://{psql_username}:{psql_password}@localhost/blog_app"

class TestConfig(Config):
    """
    Class for testing configurations. Child of class Config.
    """
    psql_username = "victormainak"
    psql_password = "password"
    SQLALCHEMY_DATABASE_URI = f"postgresql+psycopg2://{psql_username}:{psql_password}@localhost/blog_app_test"

class ProdConfig(Config):
    """
    Class for production configurations. Child of class Config.
    """
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

config_options = {
    "development": DevConfig,
    "test": TestConfig,
    "production": ProdConfig
}