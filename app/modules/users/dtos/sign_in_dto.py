from app.shared.contracts.dto import InputData


class SignInDto(InputData):
    email: str
    password: str
