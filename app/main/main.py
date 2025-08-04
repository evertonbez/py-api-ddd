"""Main Module"""

from dotenv import load_dotenv

from app.presentation.fastapi.configs.config import make_fastapi_app

load_dotenv()

app = make_fastapi_app()
