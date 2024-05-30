# SQL_ALCHEMY_DATABASE_URL = "sqlite:///./db_app.db"


# #check_same_thread is required for SQLite only.
# engine = create_engine(
# 	SQL_ALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
# )

# # Each instance of SessionLocal will be a db session
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# # Used to create each of the db models or classes
# Base = declarative_base()
from sqlmodel import SQLModel, Session, create_engine

db_name = "database.db"
db_url = f"sqlite:///{db_name}"

# setting echo=True, prints all the SQL statements to aid debugging
engine = create_engine(db_url, echo=True)


# from src.config import settings
# connect_args = {"check_same_thread": False} maybe not necessary

# engine = create_engine(settings.DATABASE_URI, echo=True, connect_args= connect_args)

# creates the database.db file and creates the users table in the db file
# metadata = contains all the tables
# create_all(): takes an engine and uses it to create the db and all the tables registered in MetaData object


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

    # refactor with llogger
    # return "db has been initialized"


# should a function always return a value?


def get_session():
    with Session(engine) as session:
        yield session
