from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base


Base = declarative_base()
database_url = "sqlite:///./pfm.db"
engine = create_engine(database_url)
sessionlocal = sessionmaker(bind=engine)


def get_db():
    db = sessionlocal()
    try:
        yield db
    finally:
        db.close()
        
