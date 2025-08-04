from pydantic import BaseModel


class BaseClassConfig:
    populate_by_name = True


class InputData(BaseModel):
    class Config(BaseClassConfig):
        pass
