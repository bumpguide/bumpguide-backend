# from contextlib import asynccontextmanager
from contextlib import asynccontextmanager
from fastapi import FastAPI
from crud import users_router

# from pydantic import BaseModel
# import models
import database
# from api.config import Settings
# from api.database import create_db_and_tables
# from api.public import api as public_api
# from api.utils.logger import logger_config
# from api.utils.mock_data_generator import create_heroes_and_teams

# import logging


# def logger_config(module):
#     """
#     Logger function. Extends Python loggin module and set a custom config.
#     params: Module Name. e.i: logger_config(__name__).
#     return: Custom logger_config Object.
#     """
#     formatter = logging.Formatter("%(asctime)s %(levelname)s %(message)s")
#     handler = logging.StreamHandler()
#     handler.setFormatter(formatter)

#     custom_logger = logging.getLogger(module)
#     custom_logger.setLevel(logging.DEBUG)

#     custom_logger.addHandler(handler)

#     return custom_logger


# logger = logger_config(__name__)

# @asynccontextmanager
# async def lifespan(app: FastAPI):
# 	# Init DB
# 	logger.info("startup: triggered")

# 	await database.create_db_and_tables()
# 	yield

# 	logger.info("shutdown: triggered")

# def get_session():
#     with Session(engine) as session:
#         yield session


# APP_NAME = "BumpGuide"
# DB_PORT = 5432
# APP_ENV = "development"
# PROD_API_KEY = "API_KEY"
# PROD_DB_URL = "proddb.amazonaws.com"
# DEV_API_KEY = ""
# DEV_DB_URL = "localhost"
# VERSION = 1
# DESCRIPTION = ""
# DEBUG = True
# DB_USER = "Tes"
# DB_PASS = "pswd"
# DB_HOST = "localhost"
# DB_NAME = "appdb"
# DB_URL = ""


# # Production API key
# PROD_API_KEY = os.environ['PROD_API_KEY']

# # Development API key
# DEV_API_KEY = os.environ['DEV_API_KEY']

# current_env = os.environ("APP_ENV", "staging")

# if current_env == "production":
# 	api_key = PROD_API_KEY
# else:
# 	api_key = DEV_API_KEY

# # Now, Initialize API client with the appropriate API key

# # db.connect(db_host, db_name, api_key)

# app = FastAPI(
# 	title=APP_NAME,
# 	version=VERSION,
# 	docs_url="/",
# 	description=DESCRIPTION,
# 	lifespan=lifespan)


# app = FastAPI()
@asynccontextmanager
async def lifespan(_: FastAPI):
    database.create_db_and_tables()
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(users_router, prefix="/users")


@app.get("/")
def read():
    return "index works"


if __name__ == "__main__":
    database.create_db_and_tables()
