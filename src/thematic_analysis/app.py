from fastapi import FastAPI

from thematic_analysis.routes import router

app = FastAPI(
    title="Thematic Analysis API",
    description="API for analyzing themes in text responses",
    version="0.1.0",
)

app.include_router(router)
