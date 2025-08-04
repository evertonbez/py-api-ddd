from app.shared.contracts.dto import InputData


class SignUpDto(InputData):
    name: str
    email: str
    password: str
