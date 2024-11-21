import os
class Configuration:
    SECRET_KEY= os.getenv("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI= os.getenv("SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    print("Configuration loaded with URI:", SQLALCHEMY_DATABASE_URI)
