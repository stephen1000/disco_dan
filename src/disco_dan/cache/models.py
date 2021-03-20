""" Database models for the cache """
import logging

from disco_dan.db import engine
from sqlalchemy import Column, DateTime, Integer, Sequence, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


logger = logging.getLogger("disco_dan")


class YoutubeQuery(Base):
    __tablename__ = "youtube_query"

    query_id = Column(Integer, Sequence("youtube_query_id_seq"), primary_key=True)
    youtube_id = Column(String)
    query_text = Column(String)
    url = Column(String)
    created_at = Column(DateTime)

    def __repr__(self):
        return f"<YoutubeQuery(query_id={self.query_id}, youtube_id={self.youtube_id}, query_text={self.query_text})>"


def create_objects(db_engine=None):
    if db_engine is None:
        Base.metadata.create_all(engine)
    else:
        logger.info("Creating tables for all models...")
        Base.metadata.create_all(db_engine)
