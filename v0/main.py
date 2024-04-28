from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from db import engine, Base
from v0.events import events as events_router
from v0.persons import persons as persons_router

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(events_router, prefix="/events", tags=["events"])
app.include_router(persons_router, prefix="/persons", tags=["persons"])


@app.get("/")
async def root():
    """
    Redirects the user to the docs page
    """
    return RedirectResponse(url="/docs")
