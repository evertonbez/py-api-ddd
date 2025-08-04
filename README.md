my_project/
├── app/
│ ├── **init**.py
│ ├── main.py # FastAPI app (ou ponto de entrada)
│
│ ├── domain/ # Regras de negócio (Entidades, ValueObjects, interfaces)
│ │ ├── **init**.py
│ │ ├── models/
│ │ │ └── account.py # Entidade
│ │ └── services/
│ │ └── transfer_service.py # Lógica de negócio
│
│ ├── application/ # Casos de uso (Application Layer)
│ │ ├── **init**.py
│ │ └── use_cases/
│ │ └── transfer_funds.py
│
│ ├── infrastructure/ # Implementações técnicas (DB, external APIs)
│ │ ├── **init**.py
│ │ ├── database/
│ │ │ └── repositories.py # Repo concretos
│ │ └── services/
│ │ └── external_api.py
│
│ ├── presentation/ # API, Controllers, Serializers
│ │ ├── **init**.py
│ │ ├── fastapi/
│ │ │ ├── routes/
│ │ │ │ └── transfer.py
│ │ │ └── configs/
│ │ │ └── app_factory.py
│
│ └── shared/ # Tipos comuns, utilitários, exceptions
│ ├── **init**.py
│ └── utils.py
│
├── tests/
│ ├── domain/
│ ├── application/
│ └── presentation/
│
├── pyproject.toml
└── README.md
