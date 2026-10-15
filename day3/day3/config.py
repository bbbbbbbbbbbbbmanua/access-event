import os


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev-secret-key")

    if os.environ.get("TESTING"):
        SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    else:
        _db_url = os.environ.get("DATABASE_URL", "sqlite:///accessevent.db")
        if _db_url.startswith("postgresql://"):
            _db_url = _db_url.replace("postgresql://", "postgresql+psycopg://", 1)
        SQLALCHEMY_DATABASE_URI = _db_url

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_EXPIRATION_HOURS = 24
