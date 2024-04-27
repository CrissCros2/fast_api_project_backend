from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from v0.events import events as events_router

app = FastAPI()
app.include_router(events_router, prefix="/events", tags=["events"])


@app.get("/")
async def root():
    """
    Redirects the user to the docs page
    """
    return RedirectResponse(url="/docs")
