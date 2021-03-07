""" SQLAlchemy objects """

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from disco_dan import settings

if settings.USE_SEARCH_CACHE:
    engine = create_engine(settings.DISCO_DAN_CONNECTION_STRING)
    Session = sessionmaker()
    Session.configure(bind=engine)
else:
    engine, Session = None, None
