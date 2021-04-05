import os

class Config:
    APP_ENV = os.environ.get("APP_ENV")
    APP_DEBUG_MODE = os.environ.get("APP_DEBUG_MODE")