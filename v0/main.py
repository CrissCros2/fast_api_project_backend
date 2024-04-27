from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi import status

app = FastAPI()


@app.get("/")
async def root():
    """
    Redirects the user to the docs page
    """
    return RedirectResponse(url="/docs")
