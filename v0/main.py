from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi import status

app = FastAPI()


@app.get("/", status_code=status.HTTP_301_MOVED_PERMANENTLY)
async def root():
    """
    Redirects the user to the docs page
    """
    return RedirectResponse("/docs")
