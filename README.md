# Documentação Detalhada do Projeto Flask

## Visão Geral

Este projeto é uma aplicação Flask que fornece uma API para autenticação de usuários e interação com a API do Pipefy para criação e gerenciamento de cards. A aplicação permite registrar e autenticar usuários, além de criar cards no Pipefy com dados fornecidos pelo usuário.

## Estrutura do Projeto

A estrutura do projeto é organizada da seguinte forma:

```
backendMaps/
│
├── app/
│   ├── models/
│   │   ├── _init_.py
│   │   └── user.py
│   │   └── card.py
│   │
│   ├── services/
│   │   ├── _init_.py
│   │   └──auth_service.py
│   │   └── pipefy_service.py
│   │
│   ├── controllers/
│   │   ├── _init_.py
│   │   └── card_controller.py
│   │
│   ├── routes/
│   │   ├── _init_.py
│   │   └── auth_routes.py
│   │   └── card_routes.py
│   │
│   │
│   │
│   ├── _init_.py
│   └── config.py
│
├── migrations/
├── venv/
│
├── config.py
├── run.py
└── requirements.txt
```

- `app/`
  - `__init__.py`: Inicializa a aplicação e suas configurações.
  - `models/`: Modelos do banco de dados.
  - `services/`: Lógica de negócios e serviços externos.
  - `controllers/`: Lógica de controle entre as rotas e os serviços.
  - `routes/`: Rotas da API.
- `config.py`: Configurações globais da aplicação.
- `run.py`: Arquivo principal para executar a aplicação Flask.

### Configurações (`config.py`)

Este arquivo contém as configurações centrais da aplicação, incluindo:

- `SECRET_KEY`: Utilizada para a criptografia de tokens JWT e outros mecanismos de segurança.
- `SQLALCHEMY_DATABASE_URI`: URI de conexão com o banco de dados PostgreSQL.
- `SQLALCHEMY_TRACK_MODIFICATIONS`: Desabilita as notificações de modificação do SQLAlchemy para performance.

### Ponto de Entrada (`run.py`)

Responsável por iniciar a aplicação Flask. Configura a aplicação para rodar em modo de depuração durante o desenvolvimento.

### Aplicação Flask (`app/__init__.py`)

Inicializa a aplicação Flask, suas configurações, e registra os blueprints das rotas definidas.

## Modelos (`app/models/`)

### `user.py`

Define o modelo `User`, representando os usuários na aplicação, incluindo campos como `id`, `username`, `password`, `email`, `cpf` e `cnpj`.

### `cards.py`

Define o modelo `Card`, representando os cards criados pelos usuários. Inclui informações como `id`, `person_type`, `name`, `cpf`, `marital_status`, `phone`, `email`, `monthly_income`, `property_type`, `cep`, `address`, `number`, `neighborhood`, `city`, `state`, `property_value`, `loan_value`, e `payment_term`.

## Rotas

### Autenticação (`app/routes/auth_routes.py`)

- **`/register`**: Permite a criação de novos usuários.
- **`/login`**: Autentica um usuário e retorna um token JWT.

### Cards (`app/routes/cards_routes.py`)

- **`/cards`**: Rota para a criação de novos cards que serão registrados tanto na base de dados local quanto no Pipefy via integração API.

## Serviços

### Autenticação (`app/services/auth_services.py`)

Implementa as funções `register_user` e `login_user`, responsáveis por registrar novos usuários no sistema e autenticar usuários existentes, respectivamente.

### Pipefy (`app/services/pipefy_services.py`)

Contém a lógica para a criação de cards no Pipefy utilizando a API GraphQL do Pipefy.

## Controladores (`app/controllers/`)

### `card_controller.py`

Intermedia a criação de cards entre as rotas e os serviços, recebendo dados da requisição, invocando o serviço de criação do Pipefy e armazenando o card no banco de dados.

## Segurança e Boas Práticas

- Utilize variáveis de ambiente para armazenar informações sensíveis, como chaves de API e credenciais de banco de dados.
- Garanta a segurança das senhas dos usuários utilizando hashes.
- Valide e sanitize as entradas do usuário para prevenir injeções SQL e outros ataques.

## Executando o Projeto

Para executar o projeto, instale as dependências utilizando `pip install -r requirements.txt` e execute o arquivo `run.py`.
