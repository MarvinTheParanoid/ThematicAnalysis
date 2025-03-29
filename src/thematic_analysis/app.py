import logging

from contextlib import asynccontextmanager

from fastapi import FastAPI

from thematic_analysis.routes import router

logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Starting up Thematic Analysis API")
    yield
    logger.info("Shutting down Thematic Analysis API")


app = FastAPI(
    title="Thematic Analysis API",
    description="API for analyzing themes in text responses",
    version="0.1.0",
    lifespan=lifespan,
)

app.include_router(router)
