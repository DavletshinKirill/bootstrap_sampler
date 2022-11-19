import os


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY')
    CSRF_ENABLE = bool(os.getenv("CSRF_ENABLE"))

    @staticmethod
    def init_app(app):
        pass
