from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import app.presentation.fastapi.routes as routes


def apply_routes_config(app: FastAPI):
    route_definitions = [
        getattr(routes, variable)
        for variable in dir(routes)
        if not variable.startswith("__")
    ]

    for route_definition in route_definitions:
        try:
            app.include_router(route_definition)
        except Exception:
            pass


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
