from main import app
from events import events as events_router


app.include_router(events_router)
