from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .objorm import *
import os
from .base import Base
import sqlite3

database_path = "meu_banco.db"
connection_string = f"sqlite:///{database_path}"

engine = create_engine(connection_string)

Base.metadata.create_all(engine)