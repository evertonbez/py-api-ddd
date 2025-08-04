from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


def make_fastapi_app():
    app = FastAPI(
        title="Dataseed API",
        description="Dataseed API is a RESTful API for the test project",
        version="0.1.0",
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    apply_routes_config(app)

    return app
