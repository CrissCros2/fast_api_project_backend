from v0.main import app
from v0.events import events as events_router


app.include_router(events_router)
