# db/__init__.py

from .database import MastermindDB, setup_db, connect_db

__all__ = ['MastermindDB', 'setup_db', 'connect_db']