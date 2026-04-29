"""FastAPI app entry point for Troy Portfolio."""
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from .config import settings
from .routes import router

app = FastAPI(title="Troy Portfolio", description="Personal portfolio of 涂炎钊")

app.mount("/static", StaticFiles(directory=str(settings.static_dir)), name="static")
app.include_router(router, prefix="")


@app.get("/")
async def root():
    """Redirect root to index route."""
    return {"message": "Troy Portfolio — visit /index to see the site"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("src.main:app", host="0.0.0.0", port=5173, reload=True)