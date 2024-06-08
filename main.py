from fastapi import FastAPI, APIRouter
from config.configdb import client
from routes.routes import root


app = FastAPI()
app.include_router(root)


# I created one post, so the next step is created the route to get all rows 