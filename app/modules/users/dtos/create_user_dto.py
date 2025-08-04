from app.shared.contracts.dto import InputData


class CreatUserDto(InputData):
    name: str
    email: str
    is_active: bool
    password: str
