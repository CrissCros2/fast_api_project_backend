from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware

from db.database import engine, Base
from v0.events import events as events_router
from v0.persons import persons as persons_router

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(events_router, prefix="/events", tags=["events"])
app.include_router(persons_router, prefix="/persons", tags=["persons"])

origins = [
    "http://localhost",
    "http://localhost:3000",
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    """
    Redirects the user to the docs page
    """
    return RedirectResponse(url="/docs")


@app.get("/health")
async def health():
    """
    Health check endpoint
    """
    return {"status": "ok"}
