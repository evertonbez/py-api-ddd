from dotenv import load_dotenv

from app.presentation.fastapi.configs.app_factory import make_fastapi_app

load_dotenv()

app = make_fastapi_app()
